from bs4 import BeautifulSoup
import requests
import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

CLIENT_ID = "5158fc7f76794a119f50a8d2b5ea8958"
CLIENT_SECRET = "ad6683a84e4e43c691e75a27e081bf12"
SPOTIFY_END_POINT = "https://accounts.spotify.com/authorize"
billboard_uri = "spotify:user:billboard.com"

date = input("Enter date in YYYY-MM-DD format: ")
# year, month, day = map(int, date.split('-'))
# date = datetime.date(year, month, day)
# print(date)


response = requests.get(url="https://www.billboard.com/charts/hot-100/" + date)
bill_board_page = response.text

soup = BeautifulSoup(bill_board_page, "html.parser")
song_name = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
songs = []
for song in song_name:
    top_song = song.getText()
    songs.append(top_song)

#
# parameters = {
#     "client_id": CLIENT_ID,
#     "response_type": "code",
#     "redirect_uri": "http://127.0.0.1:5500/"
# }
# spotify_response = requests.get(url=SPOTIFY_END_POINT, params=parameters)
# spotify_response.raise_for_status()
# data = spotify_response.text
# print(data)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:5500/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uri = []
year = date.split("-")[0]

for music in songs:
    results = sp.search(q=f"track: {music}, year: {year}", type="track")

    try:
        uri = results["tracks"]["items"][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f"{music} is not found in spotify. Skipped")

playlist = sp.user_playlist_create(
    user=user_id,
    name="Top-100 playlist of your's",
    public=False,
    collaborative=False
)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uri)

