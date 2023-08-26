from bs4 import BeautifulSoup
import requests
import json
import re

class Response:
    def __init__(self, data):
        self.data = data
        self.parse_data()

    def parse_data(self):
        data = self.data
        self.index_type = data['index']
        self.type = data['type']
        self.is_song = self.type == "song"

        if not self.is_song: return

        # Parse result object

        res = data['result']

        self.artist_names = res['artist_names']
        self.title_with_featured = res['title_with_featured']
        self.full_title = res['full_title']
        self.title = res['title']

        self.header_image_thumbnail_url = res['header_image_thumbnail_url']
        self.header_image_url = res['header_image_url']

        self.id = res['id']

        self.instrumental = res['instrumental']

        self.lyrics_owner_id = res['lyrics_owner_id']
        self.lyrics_state = res['lyrics_state']
        self.last_lyrics_update = res['lyrics_updated_at']
        self.last_update = res['updated_by_human_at']

        self.release_date_components = res['release_date_components']
        self.release_date = res['release_date_for_display']
        self.release_date_with_abbreviated_month_for_display = res['release_date_with_abbreviated_month_for_display']

        self.song_art_image_thumbnail_url = res['song_art_image_thumbnail_url']
        self.song_art_image_url = res['song_art_image_url']

        self.stats = res['stats']

        self.url = res['url']
        
        self.featured_artists = res['featured_artists']
        self.primary_artist = res['primary_artist']

class Query:
    def __init__(self, data):
        self.data = data
        self.parse_data()

    def parse_data(self):
        pd = self.data
        self.status_code = pd['meta']['status']

        # Parse response.sections object
        
        responses = pd['response']['sections']
        self.raw_responses = responses

        self.responses = []
        hits = set()

        for response in responses:
            for hit in response['hits']:
                if str(hit) in hits: continue
                self.responses.append(Response(hit))
                hits.add(str(hit))

def get_song_url_from_id(song_id):
    url = f"https://genius.com/songs/{song_id}/apple_music_player?react=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # Find the iTunes preview link using BeautifulSoup and regex
    itunes_link = soup.find('link', href=re.compile(r'.*itunes.*'))
    if itunes_link:
        return itunes_link['href']

    return None

def parse_query(data):
    return Query(data)