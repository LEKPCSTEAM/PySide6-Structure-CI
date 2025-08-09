from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel


class StatusBar(QWidget):
    def __init__(self):
        super().__init__()
        lay = QHBoxLayout(self)
        lay.setContentsMargins(8, 4, 8, 4)
        self.left = QLabel("Ready")
        self.right = QLabel()
        self.right.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        lay.addWidget(self.left, 1)
        lay.addWidget(self.right, 0)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)
        self._timer.start(1000)
        self._tick()

    def _tick(self):
        self.right.setText(QTime.currentTime().toString("HH:mm:ss"))
