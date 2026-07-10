from models.song import Song

from services.demucs_service import isolate_voice
from services.whisper_service import WhisperService
from services.export_service import export_srt


class PipelineService:

    def __init__(self):

        self.whisper = WhisperService()

    def process(self, song: Song, callback=None):
        if callback:
            callback(f"Separando voz...")
        isolate_voice(song)
        
        if callback:
            callback(f"Transcribiendo...")
        self.whisper.transcribe(song)

        if callback:
            callback(f"Exportando...")
        export_srt(song)
        
        if callback:
            callback(f"Finalizado.")