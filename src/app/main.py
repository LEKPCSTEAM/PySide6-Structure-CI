from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
import sys
from app.ui.main_window import MainWindow
from app.core.theme import load_qss
from app.core.config import settings

def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    QCoreApplication.setOrganizationName("MyOrg")
    QCoreApplication.setApplicationName(settings.app_title)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon())

    qss = load_qss()
    if qss:
        app.setStyleSheet(qss)

    win = MainWindow()
    win.resize(1280, 800)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
