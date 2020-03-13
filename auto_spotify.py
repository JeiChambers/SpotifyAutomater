"""
Step 1: Log into YouTube
Step 2: Grab Our Liked Videos
Step 3: Create a New Playlist
Step 4: Search for the Song
Step 5: Add this song into the new Spotify Playlist
"""
import json
import requests
from secrets import spotify_user_id, spotify_token

class CreatePlaylist:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    #Step 1: Login to YT
    def get_youtube_client(self):
        pass
    #Step 2: Grab our liked videos
    def get_liked_videos(self):
        pass
    #Step 3: Create a new playlist
    def create_playlist(self):

        request_body = json.dumps({
            "name": "Youtube Liked Vids",
            "description": "All Liked YouTube Videos",
            "public": "True"
        })
        query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization": "Bearer {}"
            }
        )
        response_json = response.json()

        #playlist id
        return response_json["id"]

    #Step 4: Search for the song
    def get_spotify_url(self, song_name, artist):
        
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20"
    #Step 5: Add this song to the new playlst
    def add_song_to_playlist(self):
        pass

    