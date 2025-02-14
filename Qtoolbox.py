import sys
from PyQt5.QtWidgets import QApplication, QToolBox, QTextEdit


class DocumentViewer(QToolBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Document viewer")


        self.document1=QTextEdit()
        self.document2=QTextEdit()

        self.addItem(self.document1,"Document 1")
        self.addItem(self.document2,"Document 2")


def main():
    app=QApplication(sys.argv)
    viewer=DocumentViewer()
    viewer.show()
    sys.exit(app.exec())

if __name__ == "__main__":
   main()
