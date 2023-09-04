from genius.api import Genius
import genius.utils as utils

genius = Genius()
query = genius.perform_query("Swat me mabye")
for response in query.responses:
    if(response.is_song):
        print("-"*50)
        print("SONG_ID:    ", response.id)
        print("SONG_NAME:  ", response.title)
        print("SONG_AUTHOR:", response.artist_names)
        print("STREAM_URL: ", utils.get_song_url_from_id(response.id))
print("-"*50)
