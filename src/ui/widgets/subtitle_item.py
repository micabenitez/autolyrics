from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QDoubleSpinBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from models.subtitle import Subtitle

class SubtitleItem(QWidget):

    def __init__(self, subtitle: Subtitle):

        super().__init__()

        self.subtitle = subtitle

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        self.index_label = QLabel(
            f"Subtítulo #{self.subtitle.index}"
        )

        layout.addWidget(self.index_label)

        time_layout = QHBoxLayout()

        self.start_spin = QDoubleSpinBox()
        self.start_spin.setRange(0, 99999)
        self.end_spin = QDoubleSpinBox()
        self.end_spin.setRange(0, 99999)

        self.start_spin.setDecimals(3)
        self.end_spin.setDecimals(3)

        self.start_spin.setValue(self.subtitle.start)
        self.end_spin.setValue(self.subtitle.end)

        time_layout.addWidget(QLabel("Inicio"))
        time_layout.addWidget(self.start_spin)

        time_layout.addWidget(QLabel("Fin"))
        time_layout.addWidget(self.end_spin)

        layout.addLayout(time_layout)

        layout.addWidget(QLabel("Texto"))

        self.text_edit = QTextEdit()

        self.text_edit.setPlainText(
            self.subtitle.text
        )

        layout.addWidget(self.text_edit)

        self.remove_button = QPushButton(
            "Eliminar"
        )

        layout.addWidget(self.remove_button)
        self.setStyleSheet("""
            SubtitleItem {
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                padding: 8px
            }
        """)

    def update_subtitle(self):

        self.subtitle.start = self.start_spin.value()

        self.subtitle.end = self.end_spin.value()

        self.subtitle.text = (
            self.text_edit.toPlainText().strip()
        )