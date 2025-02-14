import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QInputDialog

class ItemSelectionExample(QWidget):
   def __init__(self):
      super().__init__()

      self.initUI()

   def initUI(self):
      layout = QVBoxLayout()

      self.btn = QPushButton('Choose Color', self)
      self.btn.clicked.connect(self.getColor)
      layout.addWidget(self.btn)

      self.color_edit = QLineEdit(self)
      layout.addWidget(self.color_edit)

      self.setLayout(layout)

   def getColor(self):
      items = ['Red', 'Green', 'Blue']
      item, okPressed = QInputDialog.getItem(self, "Select Color", "Choose a color:", items, 0, False)
      if okPressed and item:
         self.color_edit.setText(item)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = ItemSelectionExample()
   ex.show()
   sys.exit(app.exec())