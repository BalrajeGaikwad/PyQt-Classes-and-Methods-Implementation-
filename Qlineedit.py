import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout

def textchanged(text):
    print("Contents of text box: " + text)
    

def enterPress():
    print("Edited")


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    e1 = QLineEdit()
    e1.setValidator(QIntValidator())  
    e1.setMaxLength(4) 
    e1.setAlignment(Qt.AlignRight) 
    e1.setFont(QFont("Arial", 20))  

    e2 = QLineEdit()
    e2.setValidator(QDoubleValidator(0.99, 99.99, 2)) 

    flo = QFormLayout()
    flo.addRow("Integer Validator", e1)
    flo.addRow("Double Validator", e2)

    e3 = QLineEdit()
    e3.setInputMask('+99_9999_999999')  
    flo.addRow("Input Mask", e3)

    e4 = QLineEdit()
    e4.textChanged.connect(textchanged)  
    flo.addRow("Text Changed", e4)

    e5 = QLineEdit()
    e5.setEchoMode(QLineEdit.Password)  
    flo.addRow("Password", e5)

    e6 = QLineEdit("Hello Python")
    e6.setReadOnly(True)
    flo.addRow("Read Only", e6)

    e5.editingFinished.connect(enterPress) 

    win.setLayout(flo)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
