from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy


class HeaderBar(QWidget):
    def __init__(self, title: str):
        super().__init__()
        self._compact = False

        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 8, 16, 8)
        layout.setSpacing(12)

        self.title_lbl = QLabel(title)
        self.title_lbl.setObjectName("HeaderTitle")

        self.right_btn = QPushButton("Action")
        self.right_btn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)

        layout.addWidget(self.title_lbl, 1, Qt.AlignVCenter)
        layout.addWidget(self.right_btn, 0, Qt.AlignRight)

    def set_compact(self, compact: bool):
        if self._compact == compact:
            return
        self._compact = compact
        m = (8, 4, 8, 4) if compact else (16, 8, 16, 8)
        self.layout().setContentsMargins(*m)
