import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QVBoxLayout, QPushButton,QInputDialog

class SimpleMessage(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Meaasge Box")

        layout=QVBoxLayout()
        self.setLayout(layout)

        self.button=QPushButton("Get Input", self)
        self.button.clicked.connect(self.get_input)
        layout.addWidget(self.button)

    def get_input(self):
        text, ok =QInputDialog.getText(self, "Input Dialog", "Enter your Name:")
        if ok:
            print("Your name is :",text)

        """msg_box=QMessageBox()
        msg_box.setText("Hello PyQt")
        msg_box.exec()
"""

if __name__=="__main__":
    app=QApplication(sys.argv)
    dialog=SimpleMessage()
    dialog.exec()
    sys.exit(app.exec())