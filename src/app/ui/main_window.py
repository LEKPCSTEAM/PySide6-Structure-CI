from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget,
    QSplitter, QSizePolicy
)
from app.ui.widgets.header_bar import HeaderBar
from app.ui.widgets.side_nav import SideNav
from app.ui.widgets.status_bar import StatusBar
from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.settings_page import SettingsPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("structure Ui UI")
        self._init_ui()

    def _init_ui(self):
        central = QWidget()
        root = QVBoxLayout(central)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(12)

        self.header = HeaderBar(title="structure Ui UI")
        root.addWidget(self.header)

        self.stack = QStackedWidget()
        self.page_dashboard = DashboardPage()
        self.page_settings = SettingsPage()
        self.stack.addWidget(self.page_dashboard)
        self.stack.addWidget(self.page_settings)

        self.sidenav = SideNav(
            items=[("Dashboard", 0), ("Settings", 1)],
            on_item_clicked=self._goto_index,
        )
        self.sidenav.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.sidenav)
        splitter.addWidget(self.stack)
        splitter.setSizes([240, 1040])
        splitter.setChildrenCollapsible(False)

        body = QWidget()
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.addWidget(splitter)

        root.addWidget(body, 1)

        self.status = StatusBar()
        root.addWidget(self.status)

        self.setCentralWidget(central)
        self._apply_adaptive_spacing()

    def resizeEvent(self, event):
        self._apply_adaptive_spacing()
        return super().resizeEvent(event)

    def _apply_adaptive_spacing(self):
        width = self.width()
        if width < 900:
            self.header.set_compact(True)
            self.sidenav.set_compact(True)
        else:
            self.header.set_compact(False)
            self.sidenav.set_compact(False)

    def _goto_index(self, idx: int):
        self.stack.setCurrentIndex(idx)
