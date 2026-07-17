from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QProgressBar,
)
from PySide6.QtCore import Signal


class SongCard(QWidget):
    editRequested = Signal(object)
    
    def __init__(self, song):
        super().__init__()

        self.song = song
        self.setup_ui()

    def setup_ui(self):

        main_layout = QHBoxLayout(self)
        content = QVBoxLayout()

        self.title_label = QLabel(self.song.path.name)
        self.status_label = QLabel("⏳ Pendiente")
        self.path_label = QLabel(str(self.song.path))
        self.remove_button = QPushButton("🗑")
        self.edit_button = QPushButton("✏️")

        self.edit_button.clicked.connect(
            lambda: self.editRequested.emit(self.song)
        )

        self.title_label.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
        """)

        self.path_label.setStyleSheet("""
            color:gray;
            font-size:11px;
        """)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        content.addWidget(self.title_label)
        content.addWidget(self.status_label)
        content.addWidget(self.path_label)
        content.addWidget(self.progress_bar)

        main_layout.addLayout(content)
        main_layout.addStretch()
        main_layout.addWidget(self.remove_button)

        self.setStyleSheet("""
            QWidget{
                background:#2d2d30;
                border-radius:10px;
            }

            QLabel{
                color:white;
            }

            QPushButton{
                border:none;
                background:transparent;
                font-size:18px;
            }
        """)

    def set_status(self, text):
        self.status_label.setText(text)

    def mark_completed(self):
        self.status_label.setText("✅ Finalizado")
        self.progress_bar.setValue(100)
    
    def set_progress(self, value: int):
        self.progress_bar.setValue(value)