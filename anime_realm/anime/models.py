from datetime import datetime
from decimal import Decimal
from common.utils import JsonSerializable

# jm2527 11/26/2023
class anime(JsonSerializable):
    def __init__(
        self, 
        anime_id: int, 
        name: str, 
        studios: str, 
        description: str,
        status: str, 
        episodes: str, 
        aired: str, 
        duration: str, 
        rating: str,
        created: datetime = None, 
        modified: datetime = None
        ):
        self.anime_id = anime_id
        self.name = name
        self.studios = studios
        self.description = description
        self.status = status
        self.episodes = episodes
        self.aired = aired
        self.duration = duration
        self.rating = rating
        self.created = created
        self.modified = modified
