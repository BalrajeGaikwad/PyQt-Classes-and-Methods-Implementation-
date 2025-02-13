import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt label widget")
        self.setGeometry(100,100,320,210)

        label=QLabel("This is a Qlabel")
        pixmap = QPixmap(r'C:\Users\Admin\Pictures\tanishka ppt things')
        label.setPixmap(pixmap)

        layout=QVBoxLayout()
        layout.addWidget(label)

        self.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())