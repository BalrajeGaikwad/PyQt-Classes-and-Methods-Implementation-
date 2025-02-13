import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QButtonGroup

class RadioButtonsGroupExample(QWidget):
   def __init__(self):
      super().__init__()
      self.initUI()

   def initUI(self):
      layout = QVBoxLayout()

      # Create button groups
      self.group1 = QButtonGroup(self)
      self.group2 = QButtonGroup(self)

      # Create radio buttons
      self.radio_button1 = QRadioButton("Option 1")
      self.radio_button2 = QRadioButton("Option 2")
      self.radio_button3 = QRadioButton("Option 3")
      self.radio_button4 = QRadioButton("Option 4")

      # Add buttons to layout
      layout.addWidget(self.radio_button1)
      layout.addWidget(self.radio_button2)
      layout.addWidget(self.radio_button3)
      layout.addWidget(self.radio_button4)

      # Group the radio buttons
      self.group1.addButton(self.radio_button1)
      self.group1.addButton(self.radio_button2)

      self.group2.addButton(self.radio_button3)
      self.group2.addButton(self.radio_button4)

      self.setLayout(layout)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = RadioButtonsGroupExample()
   ex.show()
   sys.exit(app.exec())
