class Song:
    """
    >>> song = Song(title="Mamamia", artist="Abba")
    >>> print(song)
    Abba - Mamamia
    """

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"{self.artist} - {self.title}"


class Playlist:
    """
    >>> playlist = Playlist(title="My favourite songs", songs=[Song("Mamamia", "Abba")])
    >>> print(playlist)
    My favourite songs:
    Abba - Mamamia
    >>> playlist = Playlist(title="My favorite songs")
    >>> print(playlist)
    My favorite songs:
    <BLANKLINE>
    >>> playlist += Song("Mamamia", "Abba")
    >>> print(playlist)
    My favorite songs:
    Abba - Mamamia
    >>> playlist += Song("Waterloo", "ABBA")
    >>> print(playlist)
    My favorite songs:
    ABBA - Mamamia
    ABBA - Waterloo
    >>> other_playlist = Playlist(title="Other songs", songs=[Song("Dancing Queen", "ABBA")])
    >>> playlist += other_playlist
    >>> print(playlist)
    My favorite songs:
    ABBA - Mamamia
    ABBA - Waterloo
    ABBA - Dancing Queen
    """

    def __init__(self, title, songs=None):
        self.title = title

        if songs is None:
            self.songs = []
        else:
            self.songs = songs

    def __str__(self):
        if len(self.songs) == 0:
            return self.title + ":\n"

        text = self.title + ":\n"

        for song in self.songs:
            text += str(song) + "\n"

        return text.rstrip("\n")

    def add_song(self, song):
        for old_song in self.songs:
            if old_song.artist.lower() == song.artist.lower():
                old_song.artist = song.artist

        self.songs.append(song)

    def __iadd__(self, other):
        if isinstance(other, Song):
            self.add_song(other)

        elif isinstance(other, Playlist):
            for song in other.songs:
                self.add_song(song)

        return self

    def __add__(self, other):
        self += other
        return self
