from faster_whisper import WhisperModel

from config import WHISPER_MODEL
from models.song import Song


class WhisperService:

    def __init__(self):

        self.model = WhisperModel(
            WHISPER_MODEL,
            device="cpu",
            compute_type="int8"
        )

    def transcribe(self, song: Song):

        segments, info = self.model.transcribe(
            str(song.vocals_path),
            beam_size=5,
            vad_filter=True
        )

        song.language = info.language
        song.language_probability = info.language_probability
        song.segments = list(segments)