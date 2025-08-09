from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy


class SideNav(QWidget):
    item_clicked = Signal(int)

    def __init__(self, items: list[tuple[str, int]], on_item_clicked=None):
        super().__init__()
        self._compact = False
        self._buttons: list[QPushButton] = []
        self._build(items)
        if on_item_clicked:
            self.item_clicked.connect(on_item_clicked)

    def _build(self, items):
        lay = QVBoxLayout(self)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(6)
        for text, idx in items:
            btn = QPushButton(text)
            btn.setObjectName("SideNavButton")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda _, i=idx: self.item_clicked.emit(i))
            lay.addWidget(btn)
            self._buttons.append(btn)
        lay.addStretch(1)

    def set_compact(self, compact: bool):
        if self._compact == compact:
            return
        self._compact = compact
        for btn in self._buttons:
            if compact:
                btn.setMinimumHeight(32)
            else:
                btn.setMinimumHeight(44)
