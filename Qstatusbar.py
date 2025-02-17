 
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton)
from PyQt5.QtCore import Qt
class MyWindow(QMainWindow):
   def __init__(self):
      super().__init__()

      self.setWindowTitle("QStatusBar")
      self.setFixedSize(500, 300)

      # Create a status bar
      self.status_bar = self.statusBar()

      # Permanent label (Caps Lock indicator)
      self.caps_lock_label = QLabel("Caps Lock: OFF")
      self.status_bar.addPermanentWidget(self.caps_lock_label)

      # Normal label (Current Page)
      self.page_label = QLabel("Current Page: 1")
      self.status_bar.addWidget(self.page_label)

      # Button to create a temporary messages
      self.show_message_button = QPushButton("Show Temporary Message")
      self.show_message_button.clicked.connect(self.show_temporary_message)
      self.setCentralWidget(self.show_message_button)
   def show_temporary_message(self):
      self.status_bar.showMessage("This message disappears in 4 seconds", 4000)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = MyWindow()
   window.show()
   sys.exit(app.exec())