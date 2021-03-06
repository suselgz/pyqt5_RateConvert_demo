import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow

import HLCAO
from Rate import Rate
import cv2 as cv

class CommonHelper:
    def __init__(self):
        pass
    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()
        
def initconnect():
    ui.pushButton.clicked.connect(partial(convert, ui))
    
def convert(ui):   
    usd=ui.lineEdit_USD.text()
    ra=Rate(usd)
    result=float(ra.convert())
    ui.lineEdit_CNY.setText(str(result))

   # img=cv.imread("D:\\1.jpg")
   # cv.imshow("img",img)
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    
    styleFile = './style.qss'
    qssStyle = CommonHelper.readQss(styleFile)
    MainWindow.setStyleSheet(qssStyle)
    ui = HLCAO.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    initconnect()
    sys.exit(app.exec_())
    

