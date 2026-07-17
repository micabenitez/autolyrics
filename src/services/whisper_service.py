from faster_whisper import WhisperModel

from config import WHISPER_MODEL
from models.song import Song
from models.subtitle import Subtitle


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
        
        song.subtitles = []

        for index, segment in enumerate(segments, start=1):
            
            subtitle = Subtitle(
                index=index,
                start=segment.start,
                end=segment.end,
                text=segment.text.strip()
            )

            song.subtitles.append(subtitle)