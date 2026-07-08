from models.song import Song

from services.demucs_service import isolate_voice
from services.whisper_service import WhisperService
from services.export_service import export_srt


class PipelineService:

    def __init__(self):

        self.whisper = WhisperService()

    def process(self, song: Song):

        isolate_voice(song)

        self.whisper.transcribe(song)

        export_srt(song)