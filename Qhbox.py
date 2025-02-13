from PyQt5.QtWidgets import *
import sys

class MainWinddow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        box1=QPushButton("A", self)
        box2=QPushButton("B", self)
        box3=QPushButton("C", self)

        h_box=QHBoxLayout()
        h_box.addWidget(box1)
        h_box.addWidget(box2)
        h_box.addWidget(box3)

        self.setLayout(h_box)


        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QHBoxLayout')
        self.show()



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MainWinddow()
   sys.exit(app.exec())
