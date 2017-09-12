# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:36:10 2017

@author: caicai
"""

import sys  
from PySide.QtCore import *  
from PySide.QtGui import *  
  
  
# Create a Qt application  
app = QApplication(sys.argv)  
# Create a Label and show it  
label = QLabel("Hello World")  
label.show()  
# Enter Qt application main loop  
app.exec_()  
sys.exit() 