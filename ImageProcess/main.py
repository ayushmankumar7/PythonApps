from PyQt5 import QtGui, QtCore, QtWidgets
import cv2
import sys

class DisplayImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DisplayImageWidget, self).__init__(parent)

        self.button = QtWidgets.QPushButton('Browse Image')
        self.button.clicked.connect(self.SingleBrowse)
        self.image_frame = QtWidgets.QLabel()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.image_frame)
        self.setLayout(self.layout)


    def SingleBrowse(self):
        self.image = None
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, 
                                                       'Single File',
                                                       "~/Desktop/PyRevolution/PyQt4",
                                                      '*.jpg')
        
        self.c = filePath[0]
        print('filePath',filePath[0], '\n')
        self.show_image(self.c)


    
    @QtCore.pyqtSlot()
    def show_image(self, path):
        self.image = cv2.imread(path)
        self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    display_image_widget = DisplayImageWidget()
    display_image_widget.show()
    sys.exit(app.exec_())