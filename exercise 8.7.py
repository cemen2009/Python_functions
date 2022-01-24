def make_album(artist, album, tracks_number=0):
    """Describe the music album by library"""
    if tracks_number == 0:
        album_library = {'Artist': artist.title(), 'Album': album.title()}
    else:
        album_library = {'Artist': artist.title(), 'Album': album.title(), 'Number of tracks': tracks_number}
    return album_library


print(make_album('sanya', 'xuy sosi'))
print(make_album('all egg', 'xuynia'))
print(make_album('lil nasral', 'zalupa penis'))
print(make_album(artist='valera', album='i love suck some dick', tracks_number=12))
