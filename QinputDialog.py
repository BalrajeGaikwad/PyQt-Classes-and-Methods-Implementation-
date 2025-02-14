import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QInputDialog

class TextInputExample(QWidget):
   def __init__(self):
      super().__init__()

      self.initUI()

   def initUI(self):
      layout = QVBoxLayout()

      self.btn = QPushButton('Get Text', self)
      self.btn.clicked.connect(self.getText)
      layout.addWidget(self.btn)

      self.text_edit = QLineEdit(self)
      layout.addWidget(self.text_edit)

      self.setLayout(layout)

   def getText(self):
      text, okPressed = QInputDialog.getText(self, "Get Text", "Enter your name:", QLineEdit.Normal, "")
      if okPressed and text != '':
         self.text_edit.setText(text)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = TextInputExample()
   ex.show()
   sys.exit(app.exec())