from PySide6.QtCore import QObject, Signal, Slot
from services.pipeline_service import PipelineService


class ProcessingWorker(QObject):
    finished = Signal()
    status = Signal(object, str)
    song_progress = Signal(object, int)
    global_progress = Signal(int)
    error = Signal(str)

    def __init__(self, songs):
        super().__init__()

        self.songs = songs
        self.pipeline = PipelineService()

    @Slot()
    def run(self):
        total = len(self.songs)

        for index, song in enumerate(self.songs, start=1):
            try:
                self.status.emit(
                    song,
                    f"Procesando {song.name}"
                )

                self.pipeline.process(
                    song,
                     callback=lambda status, progress: (
                        self.status.emit(song, status),
                        self.song_progress.emit(song, progress)
                    )
                )
                percentage = int(index / total * 100)
                self.song_progress.emit(song, 100)
                self.global_progress.emit(percentage)
                
            except Exception as e:
                self.error.emit(str(e))

        self.finished.emit()