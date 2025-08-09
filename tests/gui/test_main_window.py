from PySide6.QtCore import Qt
from app.ui.main_window import MainWindow

def test_main_window_smoke(qtbot):
    win = MainWindow()
    qtbot.addWidget(win)
    win.show()
    assert win.isVisible()
    assert win.windowTitle()

def test_nav_switch(qtbot):
    win = MainWindow()
    qtbot.addWidget(win)
    win.show()
    qtbot.mouseClick(win.sidenav._buttons[1], Qt.LeftButton)
    assert win.stack.currentIndex() == 1
