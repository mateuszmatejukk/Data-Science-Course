class Song:
    """
    >>> song = Song(title="Mamamia", artist="Abba")
    >>> print(song)
    Abba - Mamamia
    """
    ...


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
    >>> # same as: playlist = playlist + Song("Mamamia", "ABBA")
    >>> # same as: playlist = playlist.__add__(Song("Mamamia", "ABBA"))
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
    ...

# TODO: finish this module
