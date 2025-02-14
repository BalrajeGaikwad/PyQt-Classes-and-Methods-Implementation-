import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class FileDialogExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        self.setWindowTitle("QFile Dialog Example")
        self.setGeometry(100, 100, 400, 300)

        self.button=QPushButton("open file", self)
        self.button.clicked.connect(self.openfile)
        self.button.setGeometry(150, 150, 100, 30)

    def openfile(self):
        file_dialog=QFileDialog(self)
        file_dialog.setWindowTitle("open file")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        #file_dialog.setViewMode(QFileDialog.viewMode.Detail)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)


        if file_dialog.exec():
            selected_file=file_dialog.selectedFiles()
            print("selected file:", selected_file[0])

def main():
   app = QApplication(sys.argv)
   window = FileDialogExample()
   window.show()
   sys.exit(app.exec())

if __name__ == "__main__":
   main()        