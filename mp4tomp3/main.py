from PyQt5 import QtWidgets
import os, sys
from converter import convert, output_name



class PrettyWidget(QtWidgets.QWidget):
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('MP4 to MP3 Convertor')     
        
        btn = QtWidgets.QPushButton('Browse', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.SingleBrowse)
        btn.move(150, 100)  

        btn1 = QtWidgets.QPushButton('Convert', self)
        btn1.resize(btn.sizeHint())
        btn1.clicked.connect(self.conv)
        btn1.move(150, 150)   

        self.show()

    def SingleBrowse(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, 
                                                       'Single File',
                                                       "~/Desktop/PyRevolution/PyQt4",
                                                      '*.mp4')
        
        self.c = filePath[0]
        print('filePath',filePath[0], '\n')
        
    def conv(self):
        # convert()
        try:
            output_filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save Mp3 File", output_name(self.c), "*.mp3")
            print(output_filename)
            convert(self.c, output_filename[0])
        except:
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()