"""A video player class."""
from video_playlist import Playlist
from .video_library import VideoLibrary
import random

playlists =[]

class VideoPlayer:
    """A class used to represent a Video Player."""
    current_video = ""
    videoState = "STOPPED"

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        sorted_videos = sorted(self._video_library.get_all_videos(), key=lambda x: x.title)
        for video in sorted_videos:
            tag_string = "[]"
            if video.tags:
                tag_string = f"[{video.tags[0]} {video.tags[1]}]"
            print(f"{video.title} ({video.video_id}) {tag_string}")

    def play_video(self, video_id):

        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        try:
            next_video = self._video_library.get_video(video_id)
            if next_video.title:
                if self.current_video == "":
                    self.current_video = next_video
                else:
                    print(f"Stopping video: {self.current_video.title} ")

            else:
                raise Exception("Video does not exist.")

            self.current_video = next_video
            self.videoState = "PLAYING"

            print(f"Playing video: {self.current_video.title} ")
        except:
            print("Cannot play video: Video does not exist.")

    def stop_video(self):
        """Stops the current video."""

        if self.current_video == "":
            print("Cannot stop video: No video is currently playing")
        else:

            print(f"Stopping video: {self.current_video.title}")
        self.videoState = "STOPPED"
        self.current_video = ""

    def play_random_video(self):
        """Plays a random video from the video library."""

        if self.current_video != "":
            print(f"Stopping video: {self.current_video.title}")

        self.current_video = random.choice(self._video_library.get_all_videos())
        self.videoState = "PLAYING"

        print(f"Playing video: {self.current_video.title}")

    def pause_video(self):
        """Pauses the current video."""
        if self.videoState == "STOPPED":
            print("Cannot pause video: No video is currently playing")
        elif self.videoState == "PAUSED":
            print(f"Video already paused: {self.current_video.title}")
        else:
            print(f"Pausing video: {self.current_video.title}")
            self.videoState = "PAUSED"


    def continue_video(self):
        """Resumes playing the current video."""
        if self.videoState == "PLAYING":
            print("Cannot continue video: Video is not paused")
            return
        elif self.videoState == "STOPPED":
            print("Cannot continue video: No video is currently playing")
            return
        print(f"Continuing video: {self.current_video.title}")
        self.videoState = "PLAYING"





    def show_playing(self):
        """Displays video currently playing."""
        if self.videoState == "STOPPED":
            print("No video is currently playing.")
            return
        tag_string = "[]"
        if self.current_video.tags:
            tag_string = f"[{self.current_video.tags[0]} {self.current_video.tags[1]}]"
        if self.videoState == "PAUSED":
            print(f"Currently playing: {self.current_video.title} ({self.current_video.video_id}) {tag_string} - PAUSED")
            return


        print(f"Currently playing: {self.current_video.title} ({self.current_video.video_id}) {tag_string}")




    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
         """

        # https://stackoverflow.com/questions/598398/searching-a-list-of-objects-in-python

        for x in playlists:
            if x.name.upper() == playlist_name.upper():
                print("Cannot create playlist: A playlist with the same name already exists")

                return



        playlist = Playlist(playlist_name)
        playlists.append(playlist)
        print(f"Successfully created new playlist: {playlist_name}")





    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """


        print("add_to_playlist needs implementation")


def show_all_playlists(self):
    """Display all playlists."""

    print("show_all_playlists needs implementation")


def show_playlist(self, playlist_name):
    """Display all videos in a playlist with a given name.

    Args:
        playlist_name: The playlist name.
    """
    print("show_playlist needs implementation")


def remove_from_playlist(self, playlist_name, video_id):
    """Removes a video to a playlist with a given name.

    Args:
        playlist_name: The playlist name.
        video_id: The video_id to be removed.
    """
    print("remove_from_playlist needs implementation")


def clear_playlist(self, playlist_name):
    """Removes all videos from a playlist with a given name.

    Args:
        playlist_name: The playlist name.
    """
    print("clears_playlist needs implementation")


def delete_playlist(self, playlist_name):
    """Deletes a playlist with a given name.

    Args:
        playlist_name: The playlist name.
    """
    print("deletes_playlist needs implementation")


def search_videos(self, search_term):
    """Display all the videos whose titles contain the search_term.

    Args:
        search_term: The query to be used in search.
    """
    print("search_videos needs implementation")


def search_videos_tag(self, video_tag):
    """Display all videos whose tags contains the provided tag.

    Args:
        video_tag: The video tag to be used in search.
    """
    print("search_videos_tag needs implementation")


def flag_video(self, video_id, flag_reason=""):
    """Mark a video as flagged.

    Args:
        video_id: The video_id to be flagged.
        flag_reason: Reason for flagging the video.
    """
    print("flag_video needs implementation")


def allow_video(self, video_id):
    """Removes a flag from a video.

    Args:
        video_id: The video_id to be allowed again.
    """
    print("allow_video needs implementation")
