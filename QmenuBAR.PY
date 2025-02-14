"""import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QAction

class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()

      self.initUI()

   def initUI(self):
      menubar = self.menuBar()
      file_menu = menubar.addMenu('File')

      exit_action = QAction('Exit', self)
      exit_action.triggered.connect(self.close)
      file_menu.addAction(exit_action)

      self.setWindowTitle('QMenuBar Example')
      self.setGeometry(300, 300, 400, 300)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from PyQt5.QtGui import QAction

class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self.initUI()

   def initUI(self):
      menubar = self.menuBar()
      file_menu = menubar.addMenu('File')

      edit_menu = menubar.addMenu('Edit')
      edit_submenu = QMenu('Submenu', self)
      edit_menu.addMenu(edit_submenu)

      exit_action = QAction('Exit', self)
      exit_action.triggered.connect(self.close)
      file_menu.addAction(exit_action)

      self.setWindowTitle('QMenu Example')
      self.setGeometry(300, 300, 400, 300)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())