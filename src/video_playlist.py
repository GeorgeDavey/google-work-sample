"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name: str):
        self.name = name
        self.videos = []
