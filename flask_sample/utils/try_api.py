# jm2527 11/26/2023
import requests

url = "https://anime-manga-and-novels-api.p.rapidapi.com/anime"

querystring = {"page":"1","pageSize":"10"}

headers = {
	"X-RapidAPI-Key": "1f67de259cmsh1770794f0c1afd3p1a0878jsn07c78719dbe5",
	"X-RapidAPI-Host": "anime-manga-and-novels-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())



# d = {'items': 
#     [
#         {'animeId': 15, 'name': 'Shingeki no Kyojin: The Final Season - Kanketsu-hen', 'slug': 'shingeki-no-kyojin-the-final-season-kanketsu-hen', 'description': 'shingeki-no-kyojin-the-final-season-kanketsu-hen', 'background': None, 'image': '', 'status': 'Not yet aired', 'locale': 'en_US', 'episodes': 'Unknown', 'aired': 'Mar 4, 2023 to ?', 'premiered': '', 'broadcast': '', 'licensors': None, 'studios': 'MAPPA', 'demographic': 'Shounen', 'duration': 'Unknown', 'rating': 'R - 17+ (violence & profanity)', 'related': {'adaptation': ['Shingeki no Kyojin'], 'prequel': ['Shingeki no Kyojin']}, 'alternativeNames': {'synonyms': ['Shingeki no Kyojin'], 'japanese': '進撃の巨人 The Final Season完結編', 'english': 'Attack on Titan'}}, 
#         {'animeId': 19, 'name': '.hack//G.U. Returner', 'slug': 'hackgu-returner', 'description': 'hackgu-returner', 'background': None, 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '1', 'aired': 'Jan 18, 2007', 'premiered': '', 'broadcast': '', 'licensors': None, 'studios': 'Bee Train', 'demographic': '', 'duration': '24 min.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'alternativeVersion': ['.hack//Sign'], 'parentStory': ['.hack//Roots'], 'prequel': ['.hack//G.U. Trilogy']}, 'alternativeNames': {'japanese': '.HACK//G.U. RETURNER'}},
#         {'animeId': 20, 'name': '.hack//G.U. Trilogy', 'slug': 'hackgu-trilogy', 'description': 'hackgu-trilogy', 'background': None, 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '1', 'aired': 'Dec 22, 2007', 'premiered': '', 'broadcast': '', 'licensors': 'Funimation, Bandai Entertainment', 'studios': 'CyberConnect2', 'demographic': '', 'duration': '1 hr. 33 min.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'prequel': ['.hack//Roots'], 'sequel': ['.hack//G.U. Returner'], 'sideStory': ['.hack//G.U. Trilogy'], 'other': ['Daitai 3-pun de Wakaru .hack History']}, 'alternativeNames': {'japanese': '.hack//G.U. Trilogy', 'english': '.hack//G.U. Trilogy', 'french': '.hack // G.U. Trilogy'}}, 
#         {'animeId': 21, 'name': '.hack//G.U. Trilogy: Parody Mode', 'slug': 'hackgu-trilogy-parody-mode', 'description': 'hackgu-trilogy-parody-mode', 'background': '', 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '1', 'aired': 'Mar 25, 2008', 'premiered': '', 'broadcast': '', 'licensors': None, 'studios': 'None found, add some', 'demographic': '', 'duration': '6 min.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'parentStory': ['.hack//G.U. Trilogy']}, 'alternativeNames': {'japanese': '.hack//G.U. Trilogy', 'english': '.hack//G.U. Trilogy'}}, {'animeId': 22, 'name': '.hack//Gift', 'slug': 'hackgift', 'description': 'hackgift', 'background': '', 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '1', 'aired': 'Nov 16, 2003', 'premiered': '', 'broadcast': '', 'licensors': 'Bandai Entertainment', 'studios': 'Bee Train', 'demographic': '', 'duration': '26 min.', 'rating': 'R+ - Mild Nudity', 'related': {'parentStory': ['.hack//Sign', ' .hack//Tasogare no Udewa Densetsu']}, 'alternativeNames': {'japanese': '.hack//GIFT', 'english': '.hack//Gift'}}, 
#         {'animeId': 23, 'name': '.hack//Intermezzo', 'slug': 'hackintermezzo', 'description': 'hackintermezzo', 'background': '', 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '1', 'aired': 'Mar 28, 2003', 'premiered': '', 'broadcast': '', 'licensors': 'Bandai Entertainment', 'studios': 'Bee Train', 'demographic': '', 'duration': '24 min.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'prequel': ['.hack//Sign']}, 'alternativeNames': {'synonyms': ['.hack//Another Story', '.hack//SIGN Episode 27']}}, {'animeId': 24, 'name': '.hack//Liminality', 'slug': 'hackliminality', 'description': 'hackliminality', 'background': '', 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '4', 'aired': 'Jun 20, 2002 to Apr 10, 2003', 'premiered': '', 'broadcast': '', 'licensors': 'Bandai Entertainment', 'studios': 'Bee Train', 'demographic': '', 'duration': '33 min. per ep.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'alternativeSetting': ['.hack//Sign']}, 'alternativeNames': {'synonyms': ['Hack OVA'], 'japanese': '.hack//LIMINALITY', 'english': '.hack//Liminality'}}, 
#         {'animeId': 25, 'name': '.hack//Quantum', 'slug': 'hackquantum', 'description': 'hackquantum', 'background': '', 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '3', 'aired': 'Jan 28, 2011 to Apr 7, 2011', 'premiered': '', 'broadcast': '', 'licensors': 'Funimation', 'studios': 'Kinema Citrus', 'demographic': '', 'duration': '26 min. per ep.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'adaptation': ['.hack//Quantum+'], 'other': ['.hack//Sign', ' .hack//Tasogare no Udewa Densetsu', ' .hack//Roots'], 'sideStory': ['.hack//Quantum']}, 'alternativeNames': {'japanese': '.hack//Quantum'}}, 
#         {'animeId': 26, 'name': '.hack//Quantum: Sore ike! Bokura no Chimuchimu-chan!!', 'slug': 'hackquantum-sore-ike-bokura-no-chimuchimu-chan', 'description': 'hackquantum-sore-ike-bokura-no-chimuchimu-chan', 'background': '', 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '3', 'aired': 'Jan 28, 2011 to Apr 7, 2011', 'premiered': '', 'broadcast': '', 'licensors': None, 'studios': 'Kinema Citrus', 'demographic': '', 'duration': '3 min. per ep.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'parentStory': ['.hack//Quantum']}, 'alternativeNames': {'synonyms': ['.hack//Quantum Specials'], 'japanese': '.hack//Quantum 映像特典 それいけ！ぼくらのチムチムちゃん！！', 'english': '.hack//Quantum'}}, 
#         {'animeId': 27, 'name': '.hack//Roots', 'slug': 'hackroots', 'description': 'hackroots', 'background': '', 'image': '', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '26', 'aired': 'Apr 6, 2006 to Sep 28, 2006', 'premiered': 'Spring 2006', 'broadcast': 'Thursdays at 01', 'licensors': 'Funimation, Bandai Entertainment', 'studios': 'Bee Train', 'demographic': '', 'duration': '24 min. per ep.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'prequel': ['.hack//Sign', ' .hack//Tasogare no Udewa Densetsu'], 'sequel': ['.hack//G.U. Trilogy'], 'other': ['.hack//Quantum']}, 'alternativeNames': {'japanese': '.hack//Roots', 'english': '.hack//roots'}}
#         ], 
#     'meta': {'totalItems': 1006, 'itemCount': 10, 'itemsPerPage': '10', 'totalPages': 101, 'currentPage': '1'}}

# anime = {'animeId': 15, 'name': 'Shingeki no Kyojin: The Final Season - Kanketsu-hen', 'slug': 'shingeki-no-kyojin-the-final-season-kanketsu-hen', 'description': 'shingeki-no-kyojin-the-final-season-kanketsu-hen', 'background': None, 'image': '', 'status': 'Not yet aired', 'locale': 'en_US', 'episodes': 'Unknown', 'aired': 'Mar 4, 2023 to ?', 'premiered': '', 'broadcast': '', 'licensors': None, 'studios': 'MAPPA', 'demographic': 'Shounen', 'duration': 'Unknown', 'rating': 'R - 17+ (violence & profanity)', 'related': {'adaptation': ['Shingeki no Kyojin'], 'prequel': ['Shingeki no Kyojin']}, 'alternativeNames': {'synonyms': ['Shingeki no Kyojin'], 'japanese': '進撃の巨人 The Final Season完結編', 'english': 'Attack on Titan'}}
# # anime = {'animeId': 26, 'name': '.hack//Quantum: Sore ike! Bokura no Chimuchimu-chan!!', 'slug': 'hackquantum-sore-ike-bokura-no-chimuchimu-chan', 'description': 'hackquantum-sore-ike-bokura-no-chimuchimu-chan', 'background': '', 'image': '', 'source': 'myanimelist.net', 'status': 'Finished Airing', 'locale': 'en_US', 'episodes': '3', 'aired': 'Jan 28, 2011 to Apr 7, 2011', 'premiered': '', 'broadcast': '', 'licensors': None, 'studios': 'Kinema Citrus', 'demographic': '', 'duration': '3 min. per ep.', 'rating': 'PG-13 - Teens 13 or older', 'related': {'parentStory': ['.hack//Quantum']}, 'alternativeNames': {'synonyms': ['.hack//Quantum Specials'], 'japanese': '.hack//Quantum 映像特典 それいけ！ぼくらのチムチムちゃん！！', 'english': '.hack//Quantum'}}

# print(type(anime))

# # Get the keys
# keys = anime.keys()

# # Convert the keys to a list if needed
# keys_list = list(keys)

# # Print the keys
# print(keys_list, "\n")

# for item, value in anime.items():
#     if value:
#         print(item, value)