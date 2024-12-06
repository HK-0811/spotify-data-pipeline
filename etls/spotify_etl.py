from spotipy import Spotify
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


def connect_spotify(client_id,secret_key):
    auth_manager = SpotifyClientCredentials(client_id,secret_key)
    try:
        sp = Spotify(auth_manager=auth_manager)
        print("Connection Successfull")
        return sp

    except Exception as e:
        print(e)
        sys.exit(1)


def extract_track_info(sp:Spotify,playlist_link:str):
    playlist_uri = playlist_link.split("/")[-1]
    track_data = sp.playlist_tracks(playlist_uri)
    
    song_list = []
    album_list = []
    artists_list = []

    for item in track_data['items']:
            if 'track' in item:
                track = item['track']

                # Song Details
                song_dict = {
                    'song_id': track['id'],
                    'song_name': track['name'],
                    'song_duration': track['duration_ms'],
                    'song_url': track['external_urls']['spotify'],
                    'popularity_score': track['popularity'],
                    'album_id': track['album']['id'],
                    'artist_ids': [artist['id'] for artist in track['artists']]
                }
                song_list.append(song_dict)

                # Album Details
                album = track['album']
                album_dict = {
                    'album_id': album['id'],
                    'album_name': album['name'],
                    'release_date': album['release_date'],
                    'total_tracks': album['total_tracks'],
                    'album_url': album['external_urls']['spotify'],
                    'images': album['images'][0]['url'] if album['images'] else None
                }
                if album_dict not in album_list:  # Avoid duplicates
                    album_list.append(album_dict)

                # Artist Details
                for artist in track['artists']:
                    artist_dict = {
                        'artist_id': artist['id'],
                        'artist_name': artist['name'],
                        'artist_url': artist['external_urls']['spotify']
                    }
                    if artist_dict not in artists_list:  # Avoid duplicates
                        artists_list.append(artist_dict)
        
    return {
        'songs': song_list,
        'albums': album_list,
        'artists': artists_list
        }

        
def transform_data(data:dict):
    songs_df = pd.DataFrame(data['songs'])
    album_df = pd.DataFrame(data['albums'])
    artist_df = pd.DataFrame(data['artists'])

    songs_df['popularity_score'] = songs_df['popularity_score'].astype('int')
    songs_df['song_duration'] = songs_df['song_duration'].astype('int')
    songs_df['album_id'] = songs_df['album_id'].astype('str')


    
    # If there are items with only year, pd.datetime() will throw error
    album_df['release_date'] = album_df['release_date'].apply(lambda x: str(x.year) if isinstance(x, pd.Timestamp) else x)
    album_df['total_tracks'] = album_df['total_tracks'].astype('int')

    return songs_df, album_df, artist_df

def load_to_csv(data:pd.DataFrame,path):
    data.to_csv(path, index=False)
    









    
