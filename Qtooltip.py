import sys
from PyQt5.QtWidgets import QApplication, QPushButton

"""def main():
   app = QApplication(sys.argv)

   button = QPushButton('Hover Me')
   button.setToolTip('This is a QPushButton')

   button.show()
   sys.exit(app.exec())

if __name__ == '__main__':
   main()"""

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip
from PyQt5.QtGui import QFont

def main():
   app = QApplication(sys.argv)

   button = QPushButton('Hover Me')
   button.setToolTip('This is a QPushButton')

   QToolTip.setFont(QFont('Arial', 12))

   button.show()
   sys.exit(app.exec())

if __name__ == '__main__':
   main()