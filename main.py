import sys
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DataVisualizer(QMainWindow):
    def __init__(self):
        super(DataVisualizer, self).__init__()
        loadUi("main.ui", self)
        

def load_data(self):
    file_name,_=QFileDialog.getOpenFileName(self ,"open CSV", "","CSV Files (*.csv)")
    if file_name:
        data=pd.read_csv(file_name)
        
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataVisualizer()
    window.setWindowTitle("Analysis Application")
    window.show()
    sys.exit(app.exec_())
