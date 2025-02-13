import sys
from PyQt5.QtWidgets import *
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("pyqt QVBoxLayout")

        layout=QVBoxLayout()
        self.setLayout(layout)

        layout.addStretch()

        title=['A','B','C','D','E']
        buttons=[QPushButton(t) for t in title]
        for button in buttons:
            layout.addWidget(button)

        layout.addStretch()

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec_())