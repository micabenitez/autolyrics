from services.pipeline_service import PipelineService
from utils.file_utils import load_songs


def main():

    songs = load_songs()

    if not songs:
        print("No hay canciones.")
        return

    pipeline = PipelineService()

    for song in songs:

        print(f"Procesando {song.name}")

        pipeline.process(song)

        print(f" {song.srt_path}")


if __name__ == "__main__":
    main()