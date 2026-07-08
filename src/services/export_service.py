from pathlib import Path

from config import OUTPUT_DIR
from models.song import Song


def format_timestamp(seconds: float) -> str:

    milliseconds = int((seconds % 1) * 1000)

    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"


def export_srt(song: Song):

    OUTPUT_DIR.mkdir(exist_ok=True)

    output_file = OUTPUT_DIR / f"{song.name}.srt"

    with output_file.open("w", encoding="utf-8") as file:

        for index, segment in enumerate(song.segments, start=1):

            file.write(f"{index}\n")

            file.write(
                f"{format_timestamp(segment.start)} --> "
                f"{format_timestamp(segment.end)}\n"
            )

            file.write(segment.text.strip())

            file.write("\n\n")

    song.srt_path = output_file