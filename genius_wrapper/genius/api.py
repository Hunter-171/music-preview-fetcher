from . import utils
import requests

QUERY_URL = "https://genius.com/api/search/multi?q="

class Genius:
    def perform_query(self, query):
        res = requests.get(QUERY_URL+query)
        query = utils.parse_query(res.json())
        return query
