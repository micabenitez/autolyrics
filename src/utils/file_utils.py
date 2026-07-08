from models.song import Song
from config import INPUT_DIR, SUPPORTED_EXTENSIONS


def load_songs():

    songs = []

    for file in INPUT_DIR.iterdir():
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
            songs.append(Song(path=file))

    return sorted(songs, key=lambda song: song.name.lower())