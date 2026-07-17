from PySide6.QtCore import QThread
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QProgressBar,
    QVBoxLayout,
    QWidget,
)
from models.song import Song
from ui.widgets.drop_area import DropArea
from ui.workers.processing_worker import ProcessingWorker
from ui.widgets.song_card import SongCard
from ui.dialogs.subtitle_editor import SubtitleEditorDialog

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.cards = {}
        self.songs = []
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("AutoLyrics")
        self.resize(600, 650)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        title = QLabel("🎵 AutoLyrics")
        layout.addWidget(title)
        
        self.drop_area = DropArea()
        self.drop_area.filesDropped.connect(self.add_files)
        layout.addWidget(self.drop_area)
        
        self.song_list = QListWidget()
        layout.addWidget(self.song_list)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        self.status = QLabel("Esperando...")
        layout.addWidget(self.status)

        self.generate_button = QPushButton(
            "Generar subtítulos"
        )

        self.generate_button.clicked.connect(
            self.process_songs
        )

        layout.addWidget(self.generate_button)

    def add_files(self, files):

        for file in files:
            if any(song.path == file for song in self.songs):
                continue

            song = Song(file)
            self.songs.append(song)

            card = SongCard(song)
            card.editRequested.connect(self.open_editor)
            
            item = QListWidgetItem()
            item.setSizeHint(card.sizeHint())
            self.song_list.addItem(item)
            self.song_list.setItemWidget(item, card)
            self.cards[song.path] = card
            
    def process_songs(self):

        if not self.songs:
            self.status.setText("No hay canciones.")
            return

        self.generate_button.setEnabled(False)
        self.thread = QThread()

        self.worker = ProcessingWorker(self.songs)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.song_progress.connect(
            self.update_song_progress
        )

        self.worker.global_progress.connect(
            self.progress.setValue
        )

        self.worker.status.connect(
            self.update_song_status
        )

        self.worker.error.connect(
            self.on_error
        )

        self.worker.finished.connect(
            self.on_finished
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.worker.finished.connect(
            self.worker.deleteLater
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()

    def on_finished(self):
        self.status.setText("Finalizado")
        self.generate_button.setEnabled(True)

    def on_error(self, message):
        self.status.setText(message)
    
    def update_song_status(self, song, status):
        card = self.cards.get(song.path)

        if card:
            card.set_status(status)

        self.status.setText(
            f"{song.name} - {status}"
        )
        
    def update_song_progress(self, song, value):
        card = self.cards.get(song.path)

        if card:
            card.set_progress(value)

            if value == 100:
                card.mark_completed()
    
    def open_editor(self, song):
        dialog = SubtitleEditorDialog(song)
        dialog.exec()