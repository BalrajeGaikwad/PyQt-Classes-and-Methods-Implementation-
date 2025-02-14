import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

def window():
    app=QApplication(sys.argv)
    w=QWidget()

    b1=QPushButton(w)
    b1.setText("Information")
    b1.move(45,50)

    b2=QPushButton(w)
    b2.setText("Warning")
    b2.move(45,50)

    b3=QPushButton(w)
    b3.setText("Question")
    b3.move(45,50)

    b4=QPushButton(w)
    b4.setText("Critical")
    b4.move(45,50)

    b1.clicked.connect(show_info_messagebox)    
    b2.clicked.connect(show_warning_messagebox)    
    b3.clicked.connect(show_question_messagebox)    
    b4.clicked.connect(show_critical_messagebox)    

    #set windo title

    w.setWindowTitle("PyQt MessageBox")

    #show all widgets

    w.show()

    sys.exit(app.exec_())

def show_info_messagebox():
    msg=QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText("Information")
    msg.setWindowTitle("Information message")
    msg.setStandardButtons(QMessageBox.standardButton.Ok | QMessageBox.StandardButton.Cancel)
    retval=msg.exec()

def show_warning_messagebox():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Icon.Warning)
   msg.setText("Warning")
   msg.setWindowTitle("Warning MessageBox")
   msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
   retval = msg.exec()
def show_question_messagebox():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Icon.Question)
   msg.setText("Question")
   msg.setWindowTitle("Question MessageBox")
   msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
   retval = msg.exec()
def show_critical_messagebox():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Icon.Critical)
   msg.setText("Critical")
   msg.setWindowTitle("Critical MessageBox")
   msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
   retval = msg.exec()    


if __name__ == "__main__":
   window()
    



