import sys

from deepface import DeepFace
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton

class testing(QMainWindow):
    def setup_GUI(self):
        def click():
            print("iiiii")
        win=QMainWindow()
        win.setGeometry(400,400,400,400)
        win.setWindowTitle("verify two images")
        button=QPushButton(win)
        button.resize(200,100)
        button.setText("Choose image")
        button.move(100,100)
        button.clicked.connect(click)


if __name__=="__main__":
    app=QApplication(sys.argv)
    MainWindow=testing()
    MainWindow.show()
    sys.exit(app.exec_())