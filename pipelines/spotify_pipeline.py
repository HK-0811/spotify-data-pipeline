from spotipy import Spotify
from etls.spotify_etl import connect_spotify,extract_track_info,transform_data,load_to_csv
from utils.constants import SPOTIFY_CLIENT_ID,SPOTIFY_SECRET_KEY,OUTPUT_PATH
import os


def spotify_pipeline(file_name:str,playlist_link:str):

    # Connect to spotify API
    sp = connect_spotify(SPOTIFY_CLIENT_ID,SPOTIFY_SECRET_KEY)
    

    # Extract track info from the playlist
    data = extract_track_info(sp,playlist_link)

    # Transfroming data
    songs_df, album_df, artist_df = transform_data(data)
    
    # Load data to csv
    songs_file_path = f'{OUTPUT_PATH}/songs_{file_name}.csv'
    album_file_path = f'{OUTPUT_PATH}/album_{file_name}.csv'
    artist_file_path = f'{OUTPUT_PATH}/artist_{file_name}.csv'
    load_to_csv(songs_df,songs_file_path)
    load_to_csv(album_df,album_file_path)
    load_to_csv(artist_df,artist_file_path)

    return songs_file_path, album_file_path, artist_file_path
    
    