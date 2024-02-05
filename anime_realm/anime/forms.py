from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange, URL

# jm2527 11/26/2023
class animeFetchForm(FlaskForm):
    page_number = IntegerField('Page Number', [validators.NumberRange(min=1)], default=1)
    page_size = IntegerField('Page Size', [validators.NumberRange(min=1, max=1000)], default=10) 
    submit = SubmitField("Fetch")

# jm2527 11/26/2023
class animeForm(FlaskForm):
    # anime_id = IntegerField('Anime ID', render_kw={'readonly': True})
    name = StringField('Name', [validators.Length(min=1, max=255)])
    studios = StringField('Studios', [validators.Length(min=1, max=255)])
    description = StringField('Description', [validators.Length(max=255)])
    status = SelectField('Status', [validators.Length(max=50)])
    episodes = StringField('Episodes', [validators.Length(max=20)])
    aired = StringField('Aired', [validators.Length(max=50)])
    duration = StringField('Duration', [validators.Length(max=20)])
    rating = SelectField('Rating', [validators.Length(max=50)])
    submit = SubmitField("Save")

# jm2527 11/26/2023
class animeSearchForm(FlaskForm):
    class Meta:
        csrf = False
    # anime_id = IntegerField('Anime ID', render_kw={'readonly': True})
    name = StringField('Name', [validators.Length(min=1, max=255)])
    studios = StringField('Studios', [validators.Length(min=1, max=255)])
    # description = StringField('Description', [validators.Length(max=255)])
    status = SelectField('Status', [validators.Length(max=50)])
    # episodes = StringField('Episodes', [validators.Length(max=20)])
    # aired = StringField('Aired', [validators.Length(max=50)])
    # duration = StringField('Duration', [validators.Length(max=20)])
    rating = SelectField('Rating', [validators.Length(max=50)])
    sort = SelectField("Sort")
    order = SelectField("Order", [Optional()], choices=[("asc","Low to High"), ("desc","High to Low")])
    limit = IntegerField("Limit", [NumberRange(min=1,max=100)],default=10)
    submit = SubmitField("Filter ")
    
class adminAnimeSearchForm(animeSearchForm):
    username = StringField("Username")
    
class animeAssocForm(FlaskForm):
    class Meta:
        # This overrides the value from the base form.
        csrf = False
    username = StringField("Username")
    anime = StringField("Anime Name")
    submit = SubmitField("Filter")