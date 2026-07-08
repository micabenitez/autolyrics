import subprocess
from pathlib import Path

from config import DEMUCS_MODEL, TEMP_DIR, VOCALS_FILENAME
from models.song import Song


def isolate_voice(song: Song):

    TEMP_DIR.mkdir(exist_ok=True)

    command = [
        "demucs",
        "-n",
        DEMUCS_MODEL,
        "--two-stems",
        "vocals",
        "-o",
        str(TEMP_DIR),
        str(song.path)
    ]

    print(f"\n separando voz: {song.path.name}")

    subprocess.run(command, check=True)

    vocals_path = (
        TEMP_DIR
        / DEMUCS_MODEL
        / song.name
        / VOCALS_FILENAME
    )

    if not vocals_path.exists():
        raise FileNotFoundError(vocals_path)

    song.vocals_path = vocals_path