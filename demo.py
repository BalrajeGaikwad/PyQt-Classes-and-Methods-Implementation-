import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow,QPushButton,QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PyQt major class demo")

        label=QLabel("hello , PyQt")


        button=QPushButton("click me")
        button.clicked.connect(self.onButtonClick)


        layout=QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        central_widget=QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def onButtonClick(self):
        print("button clicked")



if __name__=="__main__":

    app=QApplication(sys.argv)
    window=MainWindow()
    window.setWindowTitle("hello")
    window.show()
    sys.exit(app.exec_())

