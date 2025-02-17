import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class FileDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("save file example")
        self.setGeometry(100, 100, 400 , 300)

        self.button=QPushButton("save file", self)
        self.button.clicked.connect(self.saveFileDilog)
        self.button.setGeometry(150, 150 ,100,30)

    def saveFileDilog(self):
        file_dialog=QFileDialog(self)
        file_dialog.setWindowTitle("save file")

        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)


        if file_dialog.exec():
            selected_file=file_dialog.selectedFiles()[0]
            print("selected file for saving :",selected_file)

def main():
    app=QApplication(sys.argv)
    window=FileDialog()
    window.show()
    sys.exit(app.exec())


if __name__=="__main__":
    main()
