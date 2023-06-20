import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QBrush, QImage
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtGui import QIcon
from deepface import DeepFace
from PyQt5.QtGui import QPalette
import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

# from enterTest1 import FirstWindowActions


class Stream(object):
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
        self.pushButton_2.setGeometry(QtCore.QRect(50, 150, 121, 41))
        self.pushButton_2.setStyleSheet("font:22px;")
        self.pushButton_2.setObjectName("pushButton_2")

        # self.pushButton_2_1 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2_1.setGeometry(QtCore.QRect(50, 180, 121, 41))
        # self.pushButton_2_1.setStyleSheet("font:22px;")
        # self.pushButton_2_1.setObjectName("pushButton_2_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 25, 350, 82))
        self.label_2.setStyleSheet("font: 75 26pt \"Segoe Print\";\n"
                                   "color:rgb(255, 85, 0);\n"
                                   "text-align:center;\n"
                                   "letter-spacing:3.5pt;")
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
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 150, 321, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 150, 151, 41))
        self.pushButton_3.setStyleSheet("font: 22px;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(730, 150, 151, 41))
        self.pushButton_4.setStyleSheet("font:22px;")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(295, 270, 411, 421))
        self.label_3.setStyleSheet("font:28px;\n"
                                   "border-style:solid;\n"
                                   "border-width:1px;\n"
                                   "border-color:rgb(45, 45, 45);\n"
                                   "\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        # self.label_3

        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(540, 270, 401, 421))
        # self.label_4.setStyleSheet("font:28px;\n"
        #                            "border-style:solid;\n"
        #                            "border-width:1px;\n"
        #                            "border-color:rgb(45, 45, 45);\n"
        #                            "\n"
        #                            "")
        # self.label_4.setText("")
        # self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(465, 230, 91, 31))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        # self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(710, 230, 72, 31))
        # self.label_6.setStyleSheet("font: 14pt \"Arial\";")
        # self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.pushButton_2.raise_()
        # self.pushButton_2_1.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_3.raise_()
        # self.label_4.raise_()
        self.label_5.raise_()
        # self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 26))
        self.menubar.setObjectName("menubar")
        self.menutest2 = QtWidgets.QMenu(self.menubar)
        self.menutest2.setObjectName("menutest2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondemo1 = QtWidgets.QAction(MainWindow)
        self.actiondemo1.setObjectName("actiondemo1")
        self.actiondemo2 = QtWidgets.QAction(MainWindow)
        self.actiondemo2.setObjectName("actiondemo2")
        self.menutest2.addAction(self.actiondemo1)
        self.menutest2.addAction(self.actiondemo2)
        self.menubar.addAction(self.menutest2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 按钮关联函数
        self.pushButton_2.clicked.connect(self.openVideo)
        # self.pushButton_2_1.clicked.connect(self.saveVideo)
        self.pushButton_3.clicked.connect(self.startAction)
        self.pushButton_4.clicked.connect(self.realTime)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "detection"))
        self.pushButton_2.setText(_translate("MainWindow", "video"))
        # self.pushButton_2_1.setText(_translate("MainWindow", "save"))
        self.label_2.setText(_translate("MainWindow", "video detection"))
        self.pushButton_3.setText(_translate("MainWindow", "start"))
        self.pushButton_4.setText(_translate("MainWindow", "realtime"))
        self.label_5.setText(_translate("MainWindow", "input"))
        # self.label_6.setText(_translate("MainWindow", "result"))
        # self.menutest2.setTitle(_translate("MainWindow", "test2"))
        self.actiondemo1.setText(_translate("MainWindow", "demo1"))
        self.actiondemo2.setText(_translate("MainWindow", "demo2"))

    # 选择本地图片上传
    def openVideo(self):
        global videoNamepath  # 这里为了方便别的地方引用图片路径，将其设置为全局变量
        # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是默认打开的路径，第四个参数是需要的格式
        videoNamepath, imgType = QFileDialog.getOpenFileName(self.centralwidget, "选择图片",
                                                           "D:\\python\\RRJ\\pycharmproject\\Practice\\chep2\\Image",
                                                           "*.mp4;;*.jpg;;*.png;;All Files(*)")
        # 通过文件路径获取图片文件，并设置图片长宽为label控件的长、宽
        # img = QtGui.QPixmap(imgNamepath).scaled(self.label_3.width(), self.label_3.height())
        self.cap=cv2.VideoCapture(videoNamepath)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        # 在label控件上显示选择的图片
        # self.label_3.setPixmap(img)
        # 显示所选图片的路径
        self.lineEdit_3.setText(videoNamepath)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            q_image = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.label_3.setPixmap(pixmap.scaled(self.label_3.width(), self.label_3.height()))
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            # self.timer.stop()
            # self.cap.release()

    # 保存图片到本地(第二种方式:首先提取相对应Qlabel中的图片，然后打开一个保存文件的弹出框，最后保存图片到选中的路径)
    def saveVideo(self):
        # 提取Qlabel中的图片
        img = self.label_4.pixmap().toImage()
        fpath, ftype = QFileDialog.getSaveFileName(self.centralwidget, "保存图片", "d:\\", "*.jpg;;*.png;;All Files(*)")
        img.save(fpath)

    def realTime(self):
        face_objs = DeepFace.stream(db_path='test',
                                    time_threshold=1,
                                    frame_threshold=1,
                                    )


    # 生成素描图
    def startAction(self):
        # img = cv2.imread(imgNamepath)
        # img = cv2.resize(img, dsize=(768, 1080))//target_size=    detector_backend=


        face_objs = DeepFace.stream(db_path='test',
                                    source=videoNamepath,
                                    time_threshold = 1,
                                    frame_threshold = 1,
                                           )
        # print(face_objs)
        print('-------')
        # print(face_objs)
        # # 图像转灰度图像
        # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # # 灰度图像到反转灰度图像
        # inverted_gray_image = 255 - gray_image
        # # 模糊倒置灰度图像
        # blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19, 19), 0)
        # # 反转模糊图像
        # inverted_blurred_image = 255 - blurred_inverted_gray_image
        # # 准备照片素描
        # sketck = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

        # path = "D:\\python\\RRJ\\pycharmProject2\\zhanCunDiZhi\\"
        # # 因为不知道怎么将<class 'numpy.ndarray'>转换为<class 'PyQt5.QtGui.QPixmap'>类型，因此采用暂存再读出的方式
        # cv2.imwrite(path + 'ZC.jpg', sketck)
        # pyqt5从路径读取图片
        # imgShow = QPixmap(path + 'ZC.jpg')
        # self.label_4.setScaledContents(True)
        # self.label_4.setPixmap(pixmap)


if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ui=Stream()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())