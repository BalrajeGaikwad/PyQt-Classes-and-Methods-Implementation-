from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox

class MyWindow(QMainWindow):
   def __init__(self):
      super().__init__()

      self.setWindowTitle("Basic QSpinBox Example")
      self.setGeometry(200, 200, 300, 200)

      spinbox = QSpinBox(self)
      spinbox.move(100, 50)
      spinbox.setMinimum(0)
      spinbox.setMaximum(100)
      spinbox.setValue(50)

if __name__ == "__main__":
   app = QApplication([])
   window = MyWindow()
   window.show()
   app.exec()