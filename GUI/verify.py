import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QBrush
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtGui import QIcon
from deepface import DeepFace

from PyQt5.QtGui import QPalette


# Notes:  参考SCDN https://blog.csdn.net/m0_47682721/article/details/123928585
# pushButton2 第一张图片   pushBbutton2_1 第二张图片  pushButton3 start
# label 5 label 6 用于显示图片  label_result 用于显示结果
# lineEdit_3 lineEdit_3_1 分别显示输入图像的名字


class Verify(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 给MainWindow设置图标
        MainWindow.setWindowIcon(QIcon('D:\\download\\xj.ico'))  # 路径错误找不到问题所在

        # 给MainWindow设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("background.jpg")))
        MainWindow.setPalette(palette)

        MainWindow.resize(994, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 961, 721))
        self.label.setStyleSheet("font:28px;\n"
                                 "border-style:solid;\n"
                                 "border-width:1px;\n"
                                 "border-color:rgb(0, 0, 0);\n"
                                 "\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 135, 121, 41))
        self.pushButton_2.setStyleSheet("font:22px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_1.setGeometry(QtCore.QRect(50, 180, 121, 41))
        self.pushButton_2_1.setStyleSheet("font:22px;")
        self.pushButton_2_1.setObjectName("pushButton_2_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 350, 81))
        self.label_2.setStyleSheet("font: 75 26pt \"Segoe Print\";\n"
                                   "color:rgb(255, 85, 0);\n"
                                   "text-align:center;\n"
                                   "letter-spacing:4pt;")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 110, 961, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 220, 961, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 135, 321, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_3_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3_1.setGeometry(QtCore.QRect(170, 180, 321, 41))
        self.lineEdit_3_1.setObjectName("lineEdit_3_1")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 150, 151, 41))
        self.pushButton_3.setStyleSheet("font: 22px;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 280, 411, 421))
        self.label_3.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(725, 135, 200, 60))
        self.label_result.setStyleSheet("font:28px;\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgb(45, 45, 45);\n"
                                        "\n"
                                        "")
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 280, 401, 421))
        self.label_4.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 240, 91, 31))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 240, 72, 31))
        self.label_6.setStyleSheet("font: 14pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton_2_1.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_3_1.raise_()
        self.pushButton_3.raise_()
        # self.pushButton_4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_result.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 按钮关联函数
        self.pushButton_2.clicked.connect(self.openImage_1)
        self.pushButton_2_1.clicked.connect(self.openImage_2)
        self.pushButton_3.clicked.connect(self.startAction)
        # self.pushButton_4.clicked.connect(self.saveImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "verification"))
        self.pushButton_2.setText(_translate("MainWindow", "image1"))
        self.pushButton_2_1.setText(_translate("MainWindow", "image2"))

        self.label_2.setText(_translate("MainWindow", "img verification"))
        self.pushButton_3.setText(_translate("MainWindow", "start"))

        self.label_5.setText(_translate("MainWindow", "image1"))
        self.label_6.setText(_translate("MainWindow", "image2"))

    # 读取第一张图片 响应连接
    def openImage_1(self):
        global imgNamepath  # 这里为了方便别的地方引用图片路径，将其设置为全局变量
        # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是默认打开的路径，第四个参数是需要的格式
        imgNamepath, imgType = QFileDialog.getOpenFileName(self.centralwidget, "选择图片",
                                                           "D:\\python\\RRJ\\pycharmproject\\Practice\\chep2\\Image",
                                                           "*.jpg;;*.png;;All Files(*)")
        # 通过文件路径获取图片文件，并设置图片长宽为label控件的长、宽
        img = QtGui.QPixmap(imgNamepath).scaled(self.label_3.width(), self.label_3.height())
        # 在label控件上显示选择的图片
        self.label_3.setPixmap(img)
        # 显示所选图片的路径
        self.lineEdit_3.setText(imgNamepath)

    # 读取第二章图片 相应连接
    def openImage_2(self):
        global imgNamepath_1  # 这里为了方便别的地方引用图片路径，将其设置为全局变量
        # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是默认打开的路径，第四个参数是需要的格式
        imgNamepath_1, imgType = QFileDialog.getOpenFileName(self.centralwidget, "选择图片",
                                                             "D:\\python\\RRJ\\pycharmproject\\Practice\\chep2\\Image",
                                                             "*.jpg;;*.png;;All Files(*)")
        # 通过文件路径获取图片文件，并设置图片长宽为label控件的长、宽
        img = QtGui.QPixmap(imgNamepath_1).scaled(self.label_4.width(), self.label_4.height())
        # 在label控件上显示选择的图片
        self.label_4.setPixmap(img)
        # 显示所选图片的路径
        self.lineEdit_3_1.setText(imgNamepath_1)

    # 开始 相应连接
    def startAction(self):
        img = cv2.imread(imgNamepath)
        img_1 = cv2.imread(imgNamepath_1)
        result = DeepFace.verify(img, img_1)

        first_key = next(iter(result))  # 获取字典的第一个键
        first_value = result[first_key]  # 获取第一个键对应的值

        self.label_result.setText(str(first_value))


import sys

# ***Notice*** 这里后面要接到主页面上
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Verify()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
