from PySide6.QtCore import QObject, Signal, Slot

from services.pipeline_service import PipelineService


class ProcessingWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    status = Signal(str)
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
                    f"Procesando {song.name}"
                )

                self.pipeline.process(song, callback=self.status.emit)
                percentage = int(index / total * 100)
                self.progress.emit(percentage)
                
            except Exception as e:
                self.error.emit(str(e))

        self.finished.emit()