from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QFrame, QSizePolicy


def _card(title: str) -> QFrame:
    f = QFrame()
    f.setObjectName("Card")
    f.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    lay = QGridLayout(f)
    lay.setContentsMargins(16, 16, 16, 16)
    t = QLabel(title)
    t.setObjectName("CardTitle")
    t.setWordWrap(True)
    lay.addWidget(t, 0, 0)
    return f


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout(self)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(12)
        grid.addWidget(_card("Sales Overview"), 0, 0)
        grid.addWidget(_card("Active Sessions"), 0, 1)
        grid.addWidget(_card("System Health"), 1, 0)
        grid.addWidget(_card("Recent Activities"), 1, 1)
