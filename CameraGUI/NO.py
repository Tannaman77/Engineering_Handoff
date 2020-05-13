import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QLabel

from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSlot
f = False
FEG = 10
def window():
	try:
	   app = QApplication(sys.argv)
	   widget = QWidget()
	   textLabel = QLabel(widget)
	   textLabel.setText("Hello World")
	   widget.setGeometry(50,50,320,200)
	   widget.setWindowTitle("PyQt5 Example")
	   widget.show()
	   sys.exit(app.exec_())
	   if FEG == 10:
	   	f = True
	except:
	   pass	
if __name__ == '__main__' and f == True:
	window()
