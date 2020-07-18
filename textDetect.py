# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textDetect.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import os
import cv2
import pytesseract
import qdarkstyle
import nlp_summary

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 430, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 60, 471, 351))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 461, 131))
        self.listWidget.setObjectName("listWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 200, 461, 371))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 430, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 580, 461, 261))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 500, 451, 341))
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 430, 141, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(900, 430, 91, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.openFolder)
        self.listWidget.doubleClicked.connect(self.listItem_Clicked)
        self.pushButton_2.clicked.connect(self.textExtraction)
        self.pushButton_3.clicked.connect(self.textDetection)
        self.pushButton_4.clicked.connect(self.textDetection_char)
        self.pushButton_5.clicked.connect(self.summarizing)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Detector"))
        self.pushButton.setText(_translate("MainWindow", "Open Folder"))
        self.pushButton_2.setText(_translate("MainWindow", "Detect Text"))
        self.label.setText(_translate("MainWindow", "Selected image"))
        self.pushButton_3.setText(_translate("MainWindow", "Detect BBox (words)"))
        self.label_2.setText(_translate("MainWindow", "Detection"))
        self.pushButton_4.setText(_translate("MainWindow", "Detect BBox (Chr)"))
        self.pushButton_5.setText(_translate("MainWindow", "Summary"))
        
    def openFolder(self):
        print('folder opened')
        self.select_folder()

    def select_folder(self):
        self.listWidget.clear()
        folder = QFileDialog.getExistingDirectory()
        for filename in sorted(os.listdir(folder)):
            ext = ['.png', '.jpg', '.jpeg']
            if not filename.endswith(tuple(ext)): continue
            fullname = os.path.join(folder, filename)
            self.listWidget.addItem(fullname)

    def openFileDialog(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
    
    def listItem_Clicked(self):
        item = self.listWidget.currentItem()
        #self.label.setText(str(item.text()))
        self.label.setPixmap(QPixmap(item.text()).scaled(420, 420, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def textDetection(self):
        item = self.listWidget.currentItem()
        img = cv2.imread(item.text())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.textBrowser_2.clear()
        h_img,w_img,_ = img.shape
        cong = r'--oem 3 --psm 6 outputbase digits'
        boxes = pytesseract.image_to_data(img,config=cong)
        self.textBrowser_2.setText(str(boxes))
        for x,i in enumerate(boxes.splitlines()):
            if x != 0:
                i = i.split()
                if len(i) == 12:
                    x, y, w, h = int(i[6]), int(i[7]), int(i[8]), int(i[9])
                    cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 1)
                    cv2.putText(img, i[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50,50,255),2)
        myQImage = self.imageOpenCv2ToQImage(img)
        self.label_2.setPixmap(QPixmap.fromImage(myQImage).scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    
    def textDetection_char(self):
        item = self.listWidget.currentItem()
        img = cv2.imread(item.text())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.textBrowser_2.clear()
        h_img,w_img,_ = img.shape
        conf = r'--oem 3 --psm 6 outputbase digits'
        boxes = pytesseract.image_to_boxes(img, config=conf)
        self.textBrowser_2.setText(str(boxes))
        for i in boxes.splitlines():
            i = i.split(' ')
            x, y, w, h = int(i[1]), int(i[2]), int(i[3]), int(i[4])
            cv2.rectangle(img, (x,h_img-y), (w, h_img-h), (0,0,255), 1)
            cv2.putText(img, i[0], (x,h_img-y+25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (50,50,255),2)
        myQImage = self.imageOpenCv2ToQImage(img)
        self.label_2.setPixmap(QPixmap.fromImage(myQImage).scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    
    def textExtraction(self):
        item = self.listWidget.currentItem()
        img = cv2.imread(item.text())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.textBrowser.setText(str(pytesseract.image_to_string(img)))

    def imageOpenCv2ToQImage (self, cv_img):
        height, width, bytesPerComponent = cv_img.shape
        bytesPerLine = bytesPerComponent * width;
        cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB, cv_img)
        return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)

    def summarizing(self):
        self.label_2.clear()
        item = self.listWidget.currentItem()
        img = cv2.imread(item.text())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        text = str(pytesseract.image_to_string(img))
        self.textBrowser_2.setText(nlp_summary.summary_text(text))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

