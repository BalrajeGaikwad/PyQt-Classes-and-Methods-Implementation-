import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCheckBox, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget=QWidget()
        layout=QVBoxLayout()

        for i in range(5):
            checkbox=QCheckBox(f'option {i}',self)
            layout.addWidget(checkbox)

            checkbox.stateChanged.connect(self.checkbox_state_changed)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)



    def checkbox_state_changed(self, state):
        checkbox=self.sender()
        print(f"{checkbox.text()} is {'checked' if state ==2 else 'unchecked'}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())