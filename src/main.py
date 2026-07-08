from services.demucs_service import isolate_voice
from utils.file_utils import load_songs


def main():

    songs = load_songs()

    if not songs:
        print("No se encontraron canciones.")
        return

    print(f"Se encontraron {len(songs)} canciones\n")

    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song.path.name}")

    first_song = songs[0]

    print(f"\nProcesando {first_song.name}")

    vocals = isolate_voice(first_song)
    
    print(f"\nVoz guardada en:")
    print(vocals)


if __name__ == "__main__":
    main()