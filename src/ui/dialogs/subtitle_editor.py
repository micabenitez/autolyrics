from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
)

from models.song import Song
from services.export_service import export_srt
from ui.widgets.subtitle_item import SubtitleItem


class SubtitleEditorDialog(QDialog):
    
    def __init__(self, song: Song):

        super().__init__()

        self.song = song

        self.subtitle_items = []

        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle(
            f"Editar subtítulos - {self.song.name}"
        )

        self.resize(900,700)

        layout = QVBoxLayout(self)

        title = QLabel(self.song.name)

        title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        scroll = QScrollArea()

        scroll.setWidgetResizable(True)

        container = QWidget()

        self.content_layout = QVBoxLayout(container)

        scroll.setWidget(container)

        layout.addWidget(scroll)

        for subtitle in self.song.subtitles:

            item = SubtitleItem(subtitle)

            self.subtitle_items.append(item)

            self.content_layout.addWidget(item)

        buttons = QHBoxLayout()

        buttons.addStretch()

        cancel = QPushButton("Cancelar")

        save = QPushButton("Guardar")

        cancel.clicked.connect(self.reject)

        save.clicked.connect(self.save)

        buttons.addWidget(cancel)

        buttons.addWidget(save)

        layout.addLayout(buttons)

    def save(self):
        for item in self.subtitle_items:
            item.update_subtitle()

        export_srt(self.song)
        self.accept()