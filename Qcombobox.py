import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCOMBO BOX")
        self.setGeometry(200,200,300,200)


        combobox=QComboBox(self)
        combobox.addItem("option 1")
        combobox.addItem("option 2")
        combobox.addItem("option 3")
        combobox.move(50,50)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())