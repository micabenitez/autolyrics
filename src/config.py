from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
TEMP_DIR = BASE_DIR / "temp"

SUPPORTED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".ogg",
    ".m4a"
}

DEMUCS_MODEL = "mdx_extra"
WHISPER_MODEL = "small"
VOCALS_FILENAME = "vocals.wav"