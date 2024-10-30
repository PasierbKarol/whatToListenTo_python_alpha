import secrets
import string
import webbrowser
import spotipy
import configurations.config
from spotipy.oauth2 import SpotifyOAuth
from models import Album, Artist
from utility import *

#methods
def generate_random_number(maximum):
    return 1 if maximum == 1 else secrets.choice(range(1, maximum))
    # Use a probability to determine whether to generate 1-9 or 10-19
    # if secrets.randbelow(10) < 7:  # 70% chance to generate 1-9
    #     return secrets.choice(range(1, 10))  # Random number between 1 and 9
    # else:  # 20% chance to generate 10-19
    #     return secrets.choice(range(10, 20))  # Random number between 10 and 19

def generate_band_letter():
    alphabet = string.ascii_uppercase
    return ''.join(secrets.choice(alphabet) for _ in range(1))

def get_all_artists():
    artists_map = {}
    total = configurations.config.maximum_artists
    current_length = 0
    after = None
    while(current_length <= total):
        # Get current user's artists
        artists_current_batch = sp.current_user_followed_artists(limit=50, after=after)
        after = artists_current_batch['artists']['cursors']['after']
        total = artists_current_batch['artists']['total']
        current_length += 50

        #get a map of artist ids
        for artist in artists_current_batch['artists']['items']:
            artists_map[artist['name']] = convert_to_artist(artist)
    return artists_map

def get_index(total):
    return generate_random_number(total)
    #return random_number if random_number <= total else (total if random_number % total == 0 else random_number % total)

def get_albums(band_to_play_albums_response, available_abums):
    album_to_play_index = get_index(int(available_abums))
    band_to_play_albums = convert_to_albums(band_to_play_albums_response['items'])
    return band_to_play_albums[album_to_play_index - 1]

# Case-insensitive filter for artists whose names start with a specified letter
def sort_artists_by_letter(letter, artists_map):
    return sorted({name: artist.id for name, artist in artists_map.items() if name.lower().startswith(letter.lower())})

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=configurations.config.client_id,
                                               client_secret=configurations.config.client_secret,
                                               redirect_uri=configurations.config.redirect_uri,
                                               scope=configurations.config.scope))

def randomize_an_album():
    #main
    band_letter = generate_band_letter()

    artists_map = get_all_artists()
    print('Total artists: ' + str(len(artists_map)))

    #get band to play
    bands_by_letter = sort_artists_by_letter(band_letter, artists_map)
    band_to_play_index = get_index(len(bands_by_letter))
    band_to_play_name = bands_by_letter[band_to_play_index]

    #get all the details about band to play
    band_to_play_details = sp.artist(artists_map[band_to_play_name].id)
    band_to_play_albums_response = sp.artist_albums(artists_map[band_to_play_name].id, 'album')
    band_to_play_releases_response = sp.artist_albums(artists_map[band_to_play_name].id)
    available_albums = int(band_to_play_albums_response['total'])
    if (available_albums == 0):
        available_releases = int(band_to_play_releases_response['total'])
        releaase_to_play = get_albums(band_to_play_releases_response, available_releases)
    #get all albums by the band to play
    album_to_play = get_albums(band_to_play_albums_response, available_albums)
    album_to_play_href = album_to_play.external_urls.spotify

    print('Today you will listen to "' + album_to_play.name + '", by "' + band_to_play_name + '".')
    #open url in spotify
    webbrowser.open(album_to_play_href)
    return album_to_play_href
