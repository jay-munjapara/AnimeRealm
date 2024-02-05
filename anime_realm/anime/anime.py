from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from sql.db import DB
from anime.forms import animeForm, animeFetchForm, animeSearchForm, adminAnimeSearchForm, animeAssocForm
from roles.permissions import admin_permission
from flask_login import login_user, login_required, logout_user, current_user
from utils.lazy import DictToObject

anime = Blueprint('anime', __name__, url_prefix='/anime', template_folder='templates')

# jm2527 12/08/2023
def get_status():
    results = DB.selectAll("SELECT DISTINCT status as label FROM IS601_anime WHERE status != ''")
    r = []
    if results.status and results.rows:
        r = results.rows
    return r

# jm2527 12/08/2023
def get_rating():
    results = DB.selectAll("SELECT DISTINCT rating as label FROM IS601_anime WHERE rating != ''")
    r = []
    if results.status and results.rows:
        r = results.rows
    return r

insert_query = """INSERT INTO IS601_anime 
                    (anime_id, name, studios, description, status, episodes, aired, duration, rating)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    name = VALUES(name),
                    studios = VALUES(studios),
                    description = VALUES(description),
                    status = VALUES(status),
                    episodes = VALUES(episodes),
                    aired = VALUES(aired),
                    duration = VALUES(duration),
                    rating = VALUES(rating)
                """

def get_total(partial_query, args={}):
    total = 0
    try:
        print("\n", "\nTotal QUERY -->", "SELECT count(1) as total FROM "+partial_query)
        result = DB.selectOne("SELECT count(1) as total FROM "+partial_query, args)
        print("\n", "\n Total ->", result)
        if result.status and result.row:
            total = int(result.row["total"])
    except Exception as e:
        print("\n", f"Error getting total {e}")
        total = 0
    return total

# jm2527 11/26/2023
@anime.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = animeFetchForm()
    if form.validate_on_submit():
        try:
            from utils.AnimeMangaNovels import AnimeAPI
            
            # Create a new anime record in the database
            # result = AnimeAPI().get_anime(form.anime_id.data)
            # print("\n", "\n\ntry result -> ", result)
            
            
            # Assuming 'form' is an object with attributes 'anime_id', 'page_number', and 'page_size'
            # anime_id = form.anime_id.data
            page_number = form.page_number.data
            page_size = form.page_size.data
            # page_number = 1
            # page_size = 100

            # Get a list of anime with pagination
            result_anime_list = AnimeAPI().get_anime_list(page=page_number, page_size=page_size)
            
            count = 0
            # print("\n", "\n\ntry result_anime_api -> ", result_anime_list)
            # Assuming result_anime_list['items'] is a list of dictionaries
            for anime_data in result_anime_list['items']:
                # print("\n", "\n\ntry anime_data -> ", anime_data)
                if anime_data:
                    result = DictToObject(anime_data)
                    print("\n", "\nafter lazy.py\n",result)
                    # In the 'fetch' route
                    result = DB.insertOne(
                        """INSERT INTO IS601_anime 
                        (anime_id, name, studios, description, status, episodes, aired, duration, rating)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE
                            name = VALUES(name),
                            studios = VALUES(studios),
                            description = VALUES(description),
                            status = VALUES(status),
                            episodes = VALUES(episodes),
                            aired = VALUES(aired),
                            duration = VALUES(duration),
                            rating = VALUES(rating)""",
                        result.animeId, result.name, result.studios, result.description, result.status, 
                        result.episodes, result.aired, result.duration, result.rating
                    )
                    if result.status:
                        count += 1
            flash(f"Loaded {count} anime records.", "success")
            
        except Exception as e:
            flash(f"Error loading anime records: {e}", "danger")
    return render_template("anime_fetch.html", form=form)

# jm2527 12/09/2023
@anime.route("/list", methods=["GET"])
# @admin_permission.require(http_exception=403)
def list():
    form = animeSearchForm(request.args)
    query = """
    SELECT id, anime_id, name, studios, description, status, episodes, aired, duration, rating,
    IFNULL((SElECT count(1) FROM IS601_Anime_Watchlist WHERE user_id = %(user_id)s and anime_id = IS601_anime.id), 0) as 'is_assoc' 
    FROM IS601_anime
    WHERE 1 = 1
    """
    args = {"user_id":current_user.id}
    
    status = [(k["label"],k["label"]) for k in get_status()]
    status = [('', 'Not Selected')] + status
    form.status.choices = status
    
    rating = [(k["label"],k["label"]) for k in get_rating()]
    rating = [('', 'Not Selected')] + rating
    form.rating.choices = rating
    
    # ["name", "studios", "description", "status", "episodes", "aired", "duration", "rating"]
    allowed_columns = ["name", "studios", "status", "rating"]
    form.sort.choices = [(k,k.title().replace("_", " ")) for k in allowed_columns]
    
    if form.name.data:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{form.name.data}%"
        
    if form.studios.data:
        query += " AND studios LIKE %(studios)s"
        args["studios"] = f"%{form.studios.data}%"
        
    # if form.description.data:
    #     query += " AND description LIKE %(description)s"
    #     args["description"] = f"%{form.description.data}%"
        
    if form.status.data:
        query += " AND status LIKE %(status)s"
        args["status"] = f"%{form.status.data}%"
    
    # if form.episodes.data:
    #     query += " AND episodes LIKE %(episodes)s"
    #     args["episodes"] = f"%{form.episodes.data}%"
        
    # if form.aired.data:
    #     query += " AND aired LIKE %(aired)s"
    #     args["aired"] = f"%{form.aired.data}%"
        
    # if form.duration.data:
    #     query += " AND duration LIKE %(duration)s"
    #     args["duration"] = f"%{form.duration.data}%"
        
    if form.rating.data:
        query += " AND rating LIKE %(rating)s"
        args["rating"] = f"%{form.rating.data}%"
    
    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        query += f" ORDER BY {form.sort.data} {form.order.data}"
    
    if form.limit.data:
        if form.limit.data >100 or form.limit.data<1:
            form.limit.data = 10
            query += f" LIMIT 10"
        else:
            query += f" LIMIT {form.limit.data}"
    else:
        query += f" LIMIT 10"

    print("\n", "->", query, args)
    rows = []
    try:
        result = DB.selectAll(query, args)
        if result.status and result.rows:
            rows = result.rows
        
        total_records = get_total(""" IS601_anime""")
        
    except Exception as e:
        print("\n", e)
        flash("Error getting anime records", "danger")
    # return render_template("anime_list.html", rows=rows, form=form)
    return render_template("anime_list.html", rows=rows, form=form, total_records=total_records)

# jm2527 12/10/2023
@anime.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = animeForm()

    status = [(k["label"], k["label"]) for k in get_status()]
    status = [('', 'Not Selected')] + status
    form.status.choices = status

    rating = [(k["label"], k["label"]) for k in get_rating()]
    rating = [('', 'Not Selected')] + rating
    form.rating.choices = rating

    if form.validate_on_submit():
        try:
            # Check for an existing record in IS601_anime
            query = """
                SELECT name, status, rating
                FROM IS601_anime
                WHERE LOWER(name) = %(name)s
                  AND LOWER(status) = %(status)s
                  AND rating = %(rating)s
            """
            existing_result = DB.selectAll(query, {
                'name': form.name.data.lower(),
                'status': form.status.data.lower(),
                'rating': form.rating.data
            })

            if existing_result.status and existing_result.rows:
                flash("Anime record already exists", "warning")
            else:
                # Create a new anime record in the database
                insert_query = """
                    INSERT INTO IS601_anime 
                    (name, studios, description, status, episodes, aired, duration, rating) 
                    VALUES (%(name)s, %(studios)s, %(description)s, %(status)s, %(episodes)s, %(aired)s, %(duration)s, %(rating)s)
                    ON DUPLICATE KEY UPDATE
                        name = VALUES(name),
                        studios = VALUES(studios),
                        description = VALUES(description),
                        status = VALUES(status),
                        episodes = VALUES(episodes),
                        aired = VALUES(aired),
                        duration = VALUES(duration),
                        rating = VALUES(rating)
                """
                insert_data = {
                    'name': form.name.data,
                    'studios': form.studios.data,
                    'description': form.description.data,
                    'status': form.status.data,
                    'episodes': form.episodes.data,
                    'aired': form.aired.data,
                    'duration': form.duration.data,
                    'rating': form.rating.data
                }

                result = DB.insertOne(insert_query, insert_data)

                if result.status:
                    flash(f"Created anime record for {form.name.data}", "success")

        except Exception as e:
            flash(f"Error: {e}", "danger")

    return render_template("anime_form.html", form=form, type="Create")

# jm2527 12/10/2023
@anime.route("/edit", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def edit():
    id = request.args.get("id")
    if not id:
        flash("Missing ID", "danger")
        return redirect(url_for("anime.list"))
    
    form = animeForm()
    
    status = [(k["label"],k["label"]) for k in get_status()]
    form.status.choices = status
    
    rating = [(k["label"],k["label"]) for k in get_rating()]
    form.rating.choices = rating
    
    if form.validate_on_submit():
        data = form.data
        # convert form data into query args dict
        del data["submit"]
        del data["csrf_token"]
        
        try:
            # print("\n", form.title.data.lower(), form.title_type.data.lower(), form.release_date.data)
            query = """
                    SELECT anime_id, name, studios, description, status, episodes, aired, duration, rating
                    FROM IS601_anime 
                    WHERE LOWER(name) = %(name)s
                    AND LOWER(studios) = %(studios)s
                    AND LOWER(description) = %(description)s
                    AND LOWER(status) = %(status)s
                    AND episodes = %(episodes)s
                    AND LOWER(aired) = %(aired)s
                    AND LOWER(duration) = %(duration)s
                    AND LOWER(rating) = %(rating)s
                """
                
            query_params = {
                'name': form.name.data.lower(),
                'studios': form.studios.data.lower(),
                'description': form.description.data.lower(),
                'status': form.status.data.lower(),
                'episodes': form.episodes.data,
                'aired': form.aired.data.lower(),
                'duration': form.duration.data.lower(),
                'rating': form.rating.data.lower(),
            }
            
            print("\n", query)
            result = DB.selectAll(query, query_params)
            # print("\n", result)
            if result.status and result.rows[0]:
                flash("Anime record already exists","warning")
        except Exception as e:
            print("\n", e)      
            try:
                result = DB.insertOne("""
                    UPDATE IS601_anime 
                    SET name = %s, studios = %s, description = %s, status = %s, 
                    episodes = %s, aired = %s, duration = %s, rating = %s 
                    WHERE id = %s""",
                    form.name.data, form.studios.data, form.description.data, form.status.data, 
                    form.episodes.data, form.aired.data, form.duration.data, form.rating.data, 
                    id
                ) 
                if result.status:
                    flash(f"Updated anime record for {form.name.data}", "success")
            except Exception as e:
                flash(f"Error updating anime record: {e}", "danger")
    
    else:
        print("\n", "Form Errors:", form.errors)
        if len(form.errors) >0:
            return render_template("anime_form.html", form=form, type="Edit")
                    
    try:
        result = DB.selectOne("""
            SELECT anime_id, name, studios, description, status, episodes, aired, duration, rating
            FROM IS601_anime 
            WHERE id = %s""",
            id
        )
        if result.status and result.row:
            data = DictToObject(result.row)
            form.process(obj=data)
        print("\n", f"Loaded form: {form.data}")
    except Exception as e:
        flash("Error fetching anime record", "danger")
        
    return render_template("anime_form.html", form=form, type="Edit")

# jm2527 12/10/2023
@anime.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    if not id:
        flash("Missing ID", "danger")
    else:
        args = {**request.args}
        print("\n", "->",args)
        del args["id"]
        result = DB.delete("DELETE FROM IS601_anime WHERE id = %s", id)
        if result.status:
            flash("Deleted anime record", "success")
    return redirect(url_for("anime.list", **args))

# jm2527 11/27/2023
@anime.route("/view", methods=["GET"])
@login_required
def view():
    id = request.args.get("id")
    args = {**request.args}
    if not id:
        flash("Missing ID", "danger")
        return redirect(url_for("anime.list"))

    try:
        result = DB.selectOne("""
            SELECT anime_id, name, studios, description, status, episodes, aired, duration, rating,
            IFNULL((SElECT count(1) FROM IS601_Anime_Watchlist WHERE user_id = %(user_id)s and anime_id = IS601_anime.id), 0) as 'is_assoc' 
            FROM IS601_anime WHERE id = %(anime_id)s""",
            {"user_id": current_user.id, "anime_id": id}
        )

        if result.status and result.row:
            return render_template("anime_view.html", anime=result.row)
        else:
            flash("Anime record not found", "danger")
    except Exception as e:
        print("\n", f"Anime error {e}")
        flash("Error viewing anime record", "danger")

    return redirect(url_for("anime.list", **args))

# jm2527 12/11/2023
@anime.route("/track", methods=["GET"])
@login_required
def track():
    id = request.args.get("id")
    args = {**request.args}
    del args["id"]
    if not id:
        flash("Missing id parameter", "danger")
    else:
        params = {"user_id": current_user.id, "anime_id": id}
        try:
            try:
                result = DB.insertOne("INSERT INTO IS601_Anime_Watchlist (anime_id, user_id) VALUES (%(anime_id)s, %(user_id)s)", params)  # Update table name
                if result.status:
                    flash("Added anime to your watch list", "success")
            except Exception as e:
                print("\n", f"Should just be a duplicate exception and can be ignored {e}")
                result = DB.delete("DELETE FROM IS601_Anime_Watchlist WHERE anime_id = %(anime_id)s AND user_id = %(user_id)s", params)  # Update table name
                if result.status:
                    flash("Removed anime from your watch list", "success")
        except Exception as e:
            print("\n", f"Error doing something with 'Add to Watchlist'/'Remove from Watchlist' {e}")
            flash("An unhandled error occurred please try again", "danger")
    # if "source" in args and args["source"] == "view":
    #     args["id"] = id
    #     del args["source"]
    #     return redirect(url_for("anime.view", **args))
    # return redirect(url_for("anime.list", **args))
    url = request.referrer
    if url:
        from urllib.parse import urlparse
        url_stuff = urlparse(url)
        watchlist_url = url_for("anime.watchlist")
        print("\n", f"Parsed url {url_stuff} {watchlist_url}")
        if url_stuff.path == url_for("anime.watchlist"):
            return redirect(url_for("anime.watchlist", **args))
        elif url_stuff.path == url_for("anime.view"):
            args["id"] = id
            return redirect(url_for("anime.view", **args))
    return redirect(url_for("anime.list", **args))

# jm2527 12/11/2023
@anime.route("/watchlist", methods=["GET"])
@login_required
def watchlist():
    id = request.args.get("id", current_user.id)
    args = {**request.args}
    
    form = animeSearchForm(request.args)
    
    query = """
    SELECT a.id, name, studios, description, status, episodes, aired, duration, rating, 1 as 'is_assoc'
    FROM IS601_anime a JOIN IS601_Anime_Watchlist w ON a.id = w.anime_id
    WHERE w.user_id = %(user_id)s
    """
    
    args = {"user_id": id}
    
    status = [(k["label"],k["label"]) for k in get_status()]
    status = [('', 'Not Selected')] + status
    form.status.choices = status
    
    rating = [(k["label"],k["label"]) for k in get_rating()]
    rating = [('', 'Not Selected')] + rating
    form.rating.choices = rating
    
    # ["name", "studios", "description", "status", "episodes", "aired", "duration", "rating"]
    allowed_columns = ["name", "studios", "status", "rating"]
    form.sort.choices = [(k,k.title().replace("_", " ")) for k in allowed_columns]
    
    if form.name.data:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{form.name.data}%"
        
    if form.studios.data:
        query += " AND studios LIKE %(studios)s"
        args["studios"] = f"%{form.studios.data}%"
        
    if form.status.data:
        query += " AND status LIKE %(status)s"
        args["status"] = f"%{form.status.data}%"
    
    if form.rating.data:
        query += " AND rating LIKE %(rating)s"
        args["rating"] = f"%{form.rating.data}%"
    
    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        query += f" ORDER BY {form.sort.data} {form.order.data}"
    
    if form.limit.data:
        if form.limit.data >100 or form.limit.data<1:
            form.limit.data = 10
            query += f" LIMIT 10"
        else:
            query += f" LIMIT {form.limit.data}"
    else:
        query += f" LIMIT 10"

    print("\n", "->", query, args)
    rows = []
    try:
        result = DB.selectAll(query, args)
        if result.status and result.rows:
            rows = result.rows
        total_records = get_total(""" IS601_anime a JOIN IS601_Anime_Watchlist w ON a.id = w.anime_id WHERE w.user_id = %(user_id)s""", {"user_id": id})
        print("\n", "total_records->",total_records)

    except Exception as e:
        print("\n", e)
        flash(f"Error getting anime records: {e}", "danger")
    return render_template("anime_list.html", rows=rows, form=form, title="Watchlist", total_records=total_records)

# jm2527 12/11/2023
@anime.route("/clear", methods=["GET"])
@login_required
def clear():
    id = request.args.get("id")
    args = {**request.args}
    if "id" in args:
        del args["id"]
    if not id:
        flash("Missing id", "danger")
    else:
        # print()
        if id == current_user.get_id() or id == current_user.has_role("Admin"):
            try:
                result = DB.delete("DELETE FROM IS601_Anime_Watchlist WHERE user_id = %(user_id)s", {"user_id":id})
                if result.status:
                    flash("Cleared watchlist", "success")
            except Exception as e:
                print("\n", f"Error clearing watchlist {e}")
                flash("Error clearing watchlist","danger");
        

    return redirect(url_for("anime.watchlist", **args))
# jm2527 12/11/2023
@anime.route("/associations", methods=["GET"])
@admin_permission.require(http_exception=403)
def associations():
    id = request.args.get("id", current_user.id)
    # args = {**request.args}
    
    form = adminAnimeSearchForm(request.args)
    
    query = """
    SELECT u.id as user_id, username, a.id, name, studios, description, status, episodes, aired, duration, rating
    FROM IS601_anime a JOIN IS601_Anime_Watchlist w ON a.id = w.anime_id LEFT JOIN IS601_Users u on u.id = w.user_id
    WHERE 1=1
    """
    
    args = {}
    
    status = [(k["label"],k["label"]) for k in get_status()]
    status = [('', 'Not Selected')] + status
    form.status.choices = status
    
    rating = [(k["label"],k["label"]) for k in get_rating()]
    rating = [('', 'Not Selected')] + rating
    form.rating.choices = rating
    
    # ["name", "studios", "description", "status", "episodes", "aired", "duration", "rating"]
    allowed_columns = ["name", "studios", "status", "rating"]
    form.sort.choices = [(k,k.title().replace("_", " ")) for k in allowed_columns]
    
    if form.username.data:
        args["username"] = f"%{form.username.data}%"
        query += " AND username LIKE %(username)s"
        
    if form.name.data:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{form.name.data}%w"
        
    if form.studios.data:
        query += " AND studios LIKE %(studios)s"
        args["studios"] = f"%{form.studios.data}%"
        
    if form.status.data:
        query += " AND status LIKE %(status)s"
        args["status"] = f"%{form.status.data}%"
        
    if form.rating.data:
        query += " AND rating LIKE %(rating)s"
        args["rating"] = f"%{form.rating.data}%"
    
    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        query += f" ORDER BY {form.sort.data} {form.order.data}"
    
    if form.limit.data:
        if form.limit.data >100 or form.limit.data<1:
            form.limit.data = 10
            query += f" LIMIT 10"
        else:
            query += f" LIMIT {form.limit.data}"
    else:
        query += f" LIMIT 10"

    print("\n", "ASSOCIATIONS->", query, args)
    rows = []
    # total_records = 0
    try:
        total_records = get_total(""" IS601_anime a JOIN IS601_Anime_Watchlist w ON a.id = w.anime_id WHERE w.user_id = %(user_id)s """, {"user_id": id})
        print("\n", "::::::::::::::::",query,args)
        result = DB.selectAll(query, args)
        
        print("\n", "result query associations->", result)
        if result.status and result.rows:
            rows = result.rows
        

    except Exception as e:
        print("\n", e)
        flash("Error getting anime records", "danger")
    # return render_template("anime_list.html", rows=rows, form=form, total_records=total_records)
    return render_template("anime_list.html", rows=rows, form=form, title="Associations", total_records=total_records)

# jm2527 12/12/2023
@anime.route("/unwatched", methods=["GET"])
@login_required
def unwatched():
    id = request.args.get("id", current_user.id)
    # args = {**request.args}
    
    form = animeSearchForm(request.args)
    
    query = """
    SELECT a.id, name, studios, description, status, episodes, aired, duration, rating,
    IFNULL((SElECT count(1) FROM IS601_Anime_Watchlist WHERE user_id = %(user_id)s and anime_id = a.id), 0) as 'is_assoc' 
    FROM IS601_anime a
    WHERE a.id not in (SELECT DISTINCT anime_id FROM IS601_Anime_Watchlist)
    """
    
    args = {"user_id": id}
    
    status = [(k["label"],k["label"]) for k in get_status()]
    status = [('', 'Not Selected')] + status
    form.status.choices = status
    
    rating = [(k["label"],k["label"]) for k in get_rating()]
    rating = [('', 'Not Selected')] + rating
    form.rating.choices = rating
    
    # ["name", "studios", "description", "status", "episodes", "aired", "duration", "rating"]
    allowed_columns = ["name", "studios", "status", "rating"]
    form.sort.choices = [(k,k.title().replace("_", " ")) for k in allowed_columns]
    
    if form.name.data:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{form.name.data}%"
        
    if form.studios.data:
        query += " AND studios LIKE %(studios)s"
        args["studios"] = f"%{form.studios.data}%"
        
    if form.status.data:
        query += " AND status LIKE %(status)s"
        args["status"] = f"%{form.status.data}%"
        
    if form.rating.data:
        query += " AND rating LIKE %(rating)s"
        args["rating"] = f"%{form.rating.data}%"
    
    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        query += f" ORDER BY {form.sort.data} {form.order.data}"
    
    if form.limit.data:
        if form.limit.data >100 or form.limit.data<1:
            form.limit.data = 10
            query += f" LIMIT 10"
        else:
            query += f" LIMIT {form.limit.data}"
    else:
        query += f" LIMIT 10"

    print("\n", "\nUNWATCHED (QUERY, ARGS)->", query, args)
    rows = []
    # total_records = 0
    try:
        total_records = get_total(""" IS601_anime a WHERE a.id not in (SELECT DISTINCT anime_id FROM IS601_Anime_Watchlist)""")
        
        result = DB.selectAll(query, args)
        print("\n", "\nresult query unwatched->", result)
        
        if result.status and result.rows:
            rows = result.rows
        
    except Exception as e:
        print("\n", e)
        flash("Error getting anime records", "danger")
        
    return render_template("anime_list.html", rows=rows, form=form, title="Anime UnWatched", total_records=total_records)

# jm2527 12/12/2023
@anime.route("/manage", methods=["GET"])
@admin_permission.require(http_exception=403)
def manage():
    id = request.args.get("id", current_user.id)
    args = {**request.args}
    
    form = animeAssocForm(request.args)
    
    users = []
    animes = []
    
    username = form.username.data
    anime_name = form.anime.data
    
    if username and anime_name:
        result = DB.selectAll("SELECT id, username FROM IS601_Users WHERE username like %(username)s LIMIT 25",{"username":f"%{username}%"})
        if result.status and result.rows:
            users = result.rows
        result = DB.selectAll("SELECT id, name FROM IS601_anime WHERE name like %(anime)s LIMIT 25", {"anime":f"%{anime_name}%"})
        if result.status and result.rows:
            animes = result.rows
            
    print(f"Users {users}")
    print(f"animes {animes}")
    
    return render_template("anime_association.html", users=users, animes=animes, form=form)

# jm2527 12/12/2023
@anime.route("/manage_assoc", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def manage_assoc():
    users = request.form.getlist("users[]")
    animes = request.form.getlist("animes[]")
    
    print("\n users, animes -->", users, animes)
    
    args = {**request.args}
    
    if users and animes: # we need both for this to work
        mappings = []
        for user in users:
            for anime in animes:
                mappings.append({"user_id":user, "anime_id":anime})
        if len(mappings) > 0:
            for mapping in mappings:
                print(f"mapping {mapping}")
                try:
                    result = DB.insertOne("INSERT INTO IS601_Anime_Watchlist (user_id, anime_id) VALUES(%(user_id)s, %(anime_id)s)", mapping)
                    if result.status:
                        pass
                        #flash(f"Successfully enabled/disabled roles for the user/role {len(mappings)} mappings", "success")
                except Exception as e:
                    print(f"Insert error {e}")
                    result = DB.delete("DELETE FROM IS601_Anime_Watchlist WHERE user_id = %(user_id)s and anime_id = %(anime_id)s",mapping)
            flash("Successfully applied mappings", "success")
        else:
            flash("No user/anime mappings", "danger")

    if "users" in args:
        del args["users"]
    if "animes" in args:
        del args["animes"]
    return redirect(url_for("anime.manage", **args))
