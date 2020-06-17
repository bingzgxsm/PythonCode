# Listing_20-3.py
# Copyright Warren & Csrter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Temperature-conversion program

import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("tempconv.ui")[0]     # Load the temperature conversion UI  

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_CtoF.clicked.connect(self.btn_CtoF_clicked)       # Bind the event handlers 
        self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)       #   to the buttons
        
    def btn_CtoF_clicked(self):                             # CtoF button event handler
        cel = float(self.editCel.text())                    #
        fahr = cel * 9 / 5.0 + 32                           #
        self.spinFahr.setValue(int(fahr + 0.5))             #
          
    def btn_FtoC_clicked(self):                             # FtoC button event handler
        fahr = self.spinFahr.value()                        #
        cel = (fahr - 32) * 5 / 9.0                         #
        self.editCel.setText(str(cel))                      #
        
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
