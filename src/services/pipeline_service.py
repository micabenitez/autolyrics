from models.song import Song

from services.demucs_service import isolate_voice
from services.whisper_service import WhisperService
from services.export_service import export_srt


class PipelineService:

    def __init__(self):
        self.whisper = WhisperService()
        
    def process(self, song: Song, callback=None):

        if callback:
            callback("Separando voz...", 20)

        isolate_voice(song)

        if callback:
            callback("Transcribiendo...", 60)

        self.whisper.transcribe(song)

        if callback:
            callback("Exportando...", 90)

        export_srt(song)

        if callback:
            callback("Finalizado.", 100)