from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QCheckBox

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        form = QFormLayout(self)
        self.name = QLineEdit()
        self.email = QLineEdit()
        self.dark = QCheckBox("Dark mode")
        form.addRow("Name", self.name)
        form.addRow("Email", self.email)
        form.addRow("", self.dark)
