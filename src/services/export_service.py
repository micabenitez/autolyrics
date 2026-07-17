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

        for subtitle in song.subtitles:

            file.write(f"{subtitle.index}\n")

            file.write(
                f"{format_timestamp(subtitle.start)} --> "
                f"{format_timestamp(subtitle.end)}\n"
            )

            file.write(subtitle.text.strip())

            file.write("\n\n")

    song.srt_path = output_file