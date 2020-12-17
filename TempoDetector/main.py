import sys, os 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap 
import librosa 


class ImageLabel(QLabel):

    def __init__(self):
        super().__init__() 
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet(''' 
            QLabel{
                border: 4px dashed #aaa
            }
        ''')


    def setPixmap(self, image):
        super().setPixmap(image)

    def change_text(self, text):
        self.setText(f"\n\n {text} \n\n")




class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout() 

        self.photoViewer = ImageLabel() 

        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)


    def dragEnterEvent(self, event):
        try:
            event.accept() 
        except:
            event.ignore()
    def dragMoveEvent(self, event): 
        try:
            event.accept() 
        except:
            event.ignore()

    def dropEvent(self, event):
        try:
            
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile() 
            self.set_image(file_path)

            event.accept()
        except:
            event.ignore() 

    def set_image(self, file_path):
        # self.photoViewer.setPixmap(QPixmap(file_path))
        print(file_path)
        name = str(file_path).split("/")[-1]
        signal, sr = librosa.load(file_path, sr = 22050)
        onset_envelope= librosa.onset.onset_strength(signal, sr)
        tempo, beats = librosa.beat.beat_track(onset_envelope= onset_envelope)
        
        self.photoViewer.change_text(f"Tempo of the Song: {tempo} \n File Name: {name}")



app = QApplication(sys.argv)

demo = AppDemo() 
demo.show()

sys.exit(app.exec_())