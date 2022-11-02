from logging.config import _RootLoggerConfiguration


def make_album(artist_name, album_title):
    return {artist_name: album_title}

dict0 = make_album("The Beatles", "Abbey Road")
dict1 = make_album("The Beatles", "Let It Be")
dict2 = make_album("The Beatles", "Sgt. Pepper's Lonely Hearts Club Band")
