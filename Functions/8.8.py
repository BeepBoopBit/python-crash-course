from logging.config import _RootLoggerConfiguration


def make_album(artist_name, album_title, number_of_tracks = None):
    if number_of_tracks:
        return {artist_name: {album_title: number_of_tracks}}
    return {artist_name: album_title}


while True:
    artist = input("Give me the artist name: ")
    if artist == 'q':
        break
    title = input("Give me the album title: ")
    if artist == 'q':
        break
    title = input("Give me the number of tracks: ")
    if artist == 'q':
        break
    if title == '0':
        title = None
    print(make_album(artist, title, title))
    