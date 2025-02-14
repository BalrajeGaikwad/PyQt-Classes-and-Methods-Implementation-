import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        chaeckbox=QCheckBox('Enable Feature', self)
        chaeckbox.setChecked(True)
        chaeckbox.stateChanged.connect(self.check_box_changed)

        self.setCentralWidget(chaeckbox)

    def check_box_changed(self, state):
        if state == 2:
            print("Featured enabled")
        else:
            print("Feature Disabled")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())