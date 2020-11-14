from PyQt5 import QtWidgets
import os, sys
from converter import convert



class PrettyWidget(QtWidgets.QWidget):
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('Single Browse')     
        
        btn = QtWidgets.QPushButton('Browse', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.SingleBrowse)
        btn.move(150, 100)     

        self.show()

    def SingleBrowse(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, 
                                                       'Single File',
                                                       "~/Desktop/PyRevolution/PyQt4",
                                                      '*.mp4')
        print('filePath',filePath[0], '\n')
        
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()