def make_album(artist, album, tracks_number=0):
    """Describe the music album by library"""
    if tracks_number == 0:
        album_library = {'Artist': artist.title(), 'Album': album.title()}
    else:
        album_library = {'Artist': artist.title(), 'Album': album.title(), 'Number of tracks': tracks_number}
    return album_library


print('You can stop program anytime just wrote "exit"')
while True:
    artist = input('Artist name: ')
    if artist == 'exit':
        break
    album = input('Album name: ')
    if album == 'exit':
        break
    tracks_number = input('Tracks number(write "skip" to skip): ')
    if tracks_number == 'exit':
        break
    if tracks_number == 'skip':
        print(make_album(artist, album))
    else:
        print(make_album(artist, album, int(tracks_number)))
