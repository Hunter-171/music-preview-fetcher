<p align="center">
    <img src="https://repository-images.githubusercontent.com/683483523/1389a73d-31d8-4f2b-a68d-40691d80d09d"/>
    <p/>
Gets music previews from apple music through genius.com as a developer friendly python API. Can be used to add music previews to your own applications, examples include music guessing games and lyrical encyclopedias.
<hr/>

## Example

**example.py**
```py
from genius.api import Genius
import genius.utils as utils

genius = Genius()
query = genius.query("Swat me mabye")
for response in query.responses:
    if(response.is_song):
        print("-"*50)
        print("SONG_ID:    ", response.id)
        print("SONG_NAME:  ", response.title)
        print("SONG_AUTHOR:", response.artist_names)
        print("STREAM_URL: ", utils.get_song_url_from_id(response.id))
print("-"*50)
```
**ouptut**
```
--------------------------------------------------
SONG_ID:     61305
SONG_NAME:   Just Me
SONG_AUTHOR: Huey Mack
STREAM_URL:  None
--------------------------------------------------
SONG_ID:     6837904
SONG_NAME:   Swat me maybe
SONG_AUTHOR: James bandz
STREAM_URL:  https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/95/2b/bf/952bbf18-64fd-bf24-4301-ceeb5c2a5ab9/mzaf_13468711367530704937.plus.aac.p.m4a
--------------------------------------------------
SONG_ID:     8495294
SONG_NAME:   That Mf Dog Off A perc
SONG_AUTHOR: James bandz
STREAM_URL:  https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/c3/62/1c/c3621c62-91ee-df19-081a-dbff14beb432/mzaf_7158316744441465691.plus.aac.p.m4a
--------------------------------------------------
SONG_ID:     4206177
SONG_NAME:   Impossible
SONG_AUTHOR: Ej Barretta
STREAM_URL:  https://audio-ssl.itunes.apple.com/apple-assets-us-std-000001/AudioPreview124/v4/3c/f2/06/3cf20694-15e0-84bf-2fd0-376fcbcf3264/mzaf_7530286406808849022.plus.aac.p.m4a
--------------------------------------------------
```
