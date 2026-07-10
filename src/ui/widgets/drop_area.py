from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QMouseEvent
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QFrame,
    QVBoxLayout
)

AUDIO_EXTENSIONS = {".mp3", ".wav", ".flac", ".ogg", ".m4a"}


class DropArea(QFrame):

    filesDropped = Signal(list)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        self.setAcceptDrops(True)

        self.setStyleSheet("""
        QFrame{
            border:2px dashed #777;
            border-radius:10px;
            padding:30px;
        }
        """)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon = QLabel("📂")
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon.setStyleSheet("font-size:24px;")

        text = QLabel(
            "Arrastrá canciones aquí\n\n"
            "o hacé click para seleccionarlas"
        )

        text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(icon)
        layout.addWidget(text)

    def dragEnterEvent(self, event: QDragEnterEvent):

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):

        files = []

        for url in event.mimeData().urls():

            path = Path(url.toLocalFile())

            if path.suffix.lower() in AUDIO_EXTENSIONS:
                files.append(path)

        self.filesDropped.emit(files)

    def mousePressEvent(self, event: QMouseEvent):

        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Seleccionar canciones",
            "",
            "Audio (*.mp3 *.wav *.flac *.ogg *.m4a)"
        )

        if files:
            self.filesDropped.emit([Path(file) for file in files])

        super().mousePressEvent(event)