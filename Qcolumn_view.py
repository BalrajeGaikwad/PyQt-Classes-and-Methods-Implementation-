import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabBar
class EventHandling(QMainWindow):
   def __init__(self):
      super().__init__()
      self.initUI()
   def initUI(self):
      self.setWindowTitle("QTabBar")
      self.setGeometry(100, 100, 600, 400)

      tab_bar = QTabBar(self)
      tab_bar.addTab("Tab 1")
      tab_bar.addTab("Tab 2")
      tab_bar.addTab("Tab 3")

      tab_bar.currentChanged.connect(self.tab_changed)
      self.setCentralWidget(tab_bar)

   def tab_changed(self, index):
      print(f"Tab changed to index {index}")

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = EventHandling()
   window.show()
   sys.exit(app.exec())