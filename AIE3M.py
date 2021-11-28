import sys
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QTransform
from PyQt5.QtWidgets import QMessageBox
from AIE3 import Ui_MainWindow
from smfileM import spw1,spw2,spw3,spw4,spw5,spw6,spw7,spw8,mgw1,mgw2,mgw3,mgw4,mgw5,mgw6,mgw7,mgw8

class Win(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Win, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    # OPEN AN IMAGE
    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(200, 500, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)
    # CLEAR
    def Reset(self):
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
    # SAVE AN IMAGE
    def SaveImage(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\', "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.image)
        else:
            print('Error')
    # RETURN ORIGINAL IMAGE
    def Original(self):
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

#     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # DETERMINE TAB
    # PIXEL RGB
    def ShowRGB(self):
        self.imageP1=str(self.textEdit.toPlainText())
        self.imageP2=str(self.textEdit_2.toPlainText())
        (b,g,r)=self.image[int(self.imageP1),int(self.imageP2)]
        self.px="Pixel at ("+str(self.imageP1)+","+str(self.imageP2)+") - Red:{}, Green:{}, Blue:{}".format(r,g,b)
        self.label_2.setText(str(self.px))
    # IMAGE'S DIMENSION
    def Dimension(self):
        self.dm="Image dimension: {}".format(self.image.shape)
        self.label_2.setText(str(self.dm))
    # IMAGE'S HEIGHT
    def Height(self):
        self.h="Image height: {}".format(self.image.shape[0])
        self.label_2.setText(str(self.h))
    # IMAGE'S WIDTH
    def Width(self):
        self.w="Image width: {}".format(self.image.shape[1])
        self.label_2.setText(str(self.w))
    # IMAGE'S NUMBER OF CHANNELS
    def ChannelsNo(self):
        self.cn="Number of channels of the image: {}".format(self.image.shape[2])
        self.label_2.setText(str(self.cn))
    # INFORMATION FOR OUTPUT TAB
    def InfoD(self):
        msg=QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Click show details for examples to input value")
        msg.setDetailedText("Pixel RGB: [100,100]")
        x=msg.exec_()

    # DRAW TAB
    # DRAW THE LINE
    def Line(self):
        imageL1 = str(self.textEdit_7.toPlainText())
        imageL2 = str(self.textEdit_8.toPlainText())
        imageL3 = str(self.textEdit_9.toPlainText())
        imageL4 = str(self.textEdit_10.toPlainText())
        imageL5 = str(self.textEdit_3.toPlainText())
        imageL6 = str(self.textEdit_4.toPlainText())
        imageL7 = str(self.textEdit_5.toPlainText())
        imageL8 = str(self.textEdit_6.toPlainText())
        cv2.line(self.image,(int(imageL1),int(imageL2)),(int(imageL3),int(imageL4)),(int(imageL6),int(imageL7),int(imageL8)),int(imageL5))
        lineImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(lineImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_4.setPixmap(self.pixmap)
    # DRAW THE RECTANGLE
    def Rectangle(self):
        imageRE1 = str(self.textEdit_7.toPlainText())
        imageRE2 = str(self.textEdit_8.toPlainText())
        imageRE3 = str(self.textEdit_9.toPlainText())
        imageRE4 = str(self.textEdit_10.toPlainText())
        imageRE5 = str(self.textEdit_3.toPlainText())
        imageRE6 = str(self.textEdit_4.toPlainText())
        imageRE7 = str(self.textEdit_5.toPlainText())
        imageRE8 = str(self.textEdit_6.toPlainText())
        cv2.rectangle(self.image,(int(imageRE1),int(imageRE2)),(int(imageRE3),int(imageRE4)),(int(imageRE6),int(imageRE7),int(imageRE8)),int(imageRE5))
        rectImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(rectImage)
        self.pixmap= self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_4.setPixmap(self.pixmap)
    # DRAW THE CIRCLE
    def Circle(self):
        imageCC1 = str(self.textEdit_11.toPlainText())
        imageCC2 = str(self.textEdit_12.toPlainText())
        imageCC3 = str(self.textEdit_13.toPlainText())
        imageCC4 = str(self.textEdit_3.toPlainText())
        imageCC5 = str(self.textEdit_4.toPlainText())
        imageCC6 = str(self.textEdit_5.toPlainText())
        imageCC7 = str(self.textEdit_6.toPlainText())
        cv2.circle(self.image,(int(imageCC1),int(imageCC2)),int(imageCC3),(int(imageCC5),int(imageCC6),int(imageCC7)),int(imageCC4))
        circleImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(circleImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_4.setPixmap(self.pixmap)
    # DRAW THE ELLIPSE
    def Ellipse(self):
        imageE1 = str(self.textEdit_11.toPlainText())
        imageE2 = str(self.textEdit_12.toPlainText())
        imageE3 = str(self.textEdit_14.toPlainText())
        imageE4 = str(self.textEdit_15.toPlainText())
        imageE5 = str(self.textEdit_16.toPlainText())
        imageE8 = str(self.textEdit_3.toPlainText())
        imageE9 = str(self.textEdit_4.toPlainText())
        imageE10 = str(self.textEdit_5.toPlainText())
        imageE11 = str(self.textEdit_6.toPlainText())
        cv2.ellipse(self.image,(int(imageE1),int(imageE2)),(int(imageE3),int(imageE4)),int(imageE5),0,360,(int(imageE9),int(imageE10),int(imageE11)),int(imageE8))
        ellipseImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(ellipseImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_4.setPixmap(self.pixmap)
    # PUT TEXT
    def comboText(self):
        text = str(self.comboBox.currentText())
        if text == 'Hershey Simplex':
            self.font=cv2.FONT_HERSHEY_COMPLEX
        elif text == 'Hershey Plain':
            self.font=cv2.FONT_HERSHEY_PLAIN
        elif text == 'Hershey Duplex':
            self.font=cv2.FONT_HERSHEY_DUPLEX
        elif text == 'Hershey Complex':
            self.font=cv2.FONT_HERSHEY_COMPLEX
        elif text == 'Hershey Triplex':
            self.font=cv2.FONT_HERSHEY_TRIPLEX
        elif text == 'Hershey Complex Small':
            self.font=cv2.FONT_HERSHEY_COMPLEX_SMALL
        elif text == 'Hershey Script Simplex':
            self.font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        elif text == 'Hershey Script Complex':
            self.font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    def Text(self):
        # font = cv2.FONT_HERSHEY_COMPLEX
        imageTX1 = str(self.textEdit_17.toPlainText())
        imageTX2 = str(self.textEdit_18.toPlainText())
        imageTX3 = str(self.textEdit_19.toPlainText())
        imageTX4 = str(self.textEdit_20.toPlainText())
        imageTX5 = str(self.textEdit_3.toPlainText())
        imageTX6 = str(self.textEdit_4.toPlainText())
        imageTX7 = str(self.textEdit_5.toPlainText())
        imageTX8 = str(self.textEdit_6.toPlainText())
        cv2.putText(self.image,imageTX4,(int(imageTX1),int(imageTX2)),self.font,float(imageTX3),(int(imageTX6),int(imageTX7),int(imageTX8)),int(imageTX5))
        textImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(textImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_4.setPixmap(self.pixmap)

    # INFORMATION FOR DRAW TAB
    def InfoDR(self):
        msg=QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Click shows details for examples to input value")
        # msg.setInformativeText("Theme font is fixed for the text")
        msg.setDetailedText("Thickness: [2]"+"                                             "+"Color: [0,0,255],see color codes chart(in BGR order)]"+
                            "                                                         "+"Line: [(0,0),(50,50)]"+"                                      "
                            +"Rectangle: [(0,0), (50,50)]"+"                                        "+"Circle: [(50,50),30]"
                            +"                                        "+"Ellipse: [(50,50),25,75,30]"+"                                        "+"Text: [(20,20),2,insert text]")

        x=msg.exec_()

# EDIT TAB
    # RESIZE IMAGE
    def Resize(self):
        self.imageR1 = str(self.textEdit_21.toPlainText())
        self.imageR2 = str(self.textEdit_22.toPlainText())
        dimension = (int(self.imageR1), int(self.imageR2))
        self.image = cv2.resize(self.image, dimension)
        self.pixmap = self.pixmap.scaled(int(self.imageR1), int(self.imageR2))
        self.label_4.setPixmap(self.pixmap)
    # CROP IMAGE
    def Crop(self):
        startX = int(self.textEdit_23.toPlainText())
        startY = int(self.textEdit_24.toPlainText())
        endX = int(self.textEdit_25.toPlainText())
        endY = int(self.textEdit_26.toPlainText())
        self.image = self.image[startY:endY, startX:endX]
        # self.pixmap=self.pixmap.copy(QtCore.QRect(startX,startY,int(self.image.shape[1]),int(self.image.shape[0])))
        # self.pixmap = self.pixmap.scaled(int(self.image.shape[1]),int(self.image.shape[0]))
        # self.label_25.setPixmap(self.pixmap)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2BGRA)
        self.qformat = QImage.Format_ARGB32
        self.img = QtGui.QImage(self.image, int(self.image.shape[1]), int(self.image.shape[0]), int(self.qformat))
        self.label_4.setPixmap((QtGui.QPixmap.scaled(QtGui.QPixmap.fromImage(self.img), int(self.image.shape[1]),
                                                     int(self.image.shape[0]), QtCore.Qt.KeepAspectRatio,
                                                     QtCore.Qt.SmoothTransformation)))
    # TRANSLATE IMAGE
    def Translate(self):
        imageT1 = int(self.textEdit_27.toPlainText())
        imageT2 = int(self.textEdit_28.toPlainText())
        translationMatrix=np.float32([[1.0,0.0,imageT1],[0.0,1.0,imageT2]])
        self.image = cv2.warpAffine(self.image, translationMatrix, (self.image.shape[0],self.image.shape[1]))
        imageTranslation = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(imageTranslation)
        self.pixmap = self.pixmap.scaled(900,500,QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
        self.pixmap = self.pixmap.scaled(int(self.image.shape[1]), int(self.image.shape[0]))
        self.label_4.setPixmap(self.pixmap)
    # ROTATE IMAGE
    def Rotate(self):
        imageRO = int(self.textEdit_29.toPlainText())
        scale=1.0
        self.center=(self.image.shape[1]/2, self.image.shape[0]/2)
        M=cv2.getRotationMatrix2D(self.center,-imageRO,scale)
        self.image=cv2.warpAffine(self.image,M,(self.image.shape[0],self.image.shape[1]))
        rotatedImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        transform=QTransform().rotate(imageRO)
        self.pixmap = QtGui.QPixmap(rotatedImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_4.setPixmap(self.pixmap)
    def comboFilter(self):
        text = str(self.comboBox_2.currentText())
        if text == 'Gray Scale':
            self.ConvertGS()
        elif text == 'CIE XYZ':
            self.ConvertBGRA()
        elif text == 'YCC':
            self.ConvertYCC()
        elif text == 'HSV':
            self.ConvertHSV()
        elif text == 'CIE LUV':
            self.ConvertLUV()
        elif text == 'HLS':
            self.ConvertHLS()

    # CONVERT TO GRAY SCALE
    def ConvertGS(self):
        self.image=cv2.cvtColor(self.image,cv2.COLOR_BGRA2GRAY)
        grayImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1], QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(grayImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    # CONVERT TO BGRA
    def ConvertBGRA(self):
        self.image= cv2.cvtColor(self.image, cv2.COLOR_BGR2BGRA)
        xyzImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(xyzImage)
        self.pixmap= self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    # CONVERT TO YCC
    def ConvertYCC(self):
        self.image= cv2.cvtColor(self.image, cv2.COLOR_BGR2YCrCb)
        yccImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(yccImage)
        self.pixmap2 = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    # CONVERT TO HSV
    def ConvertHSV(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        hsvImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(hsvImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    # CONVERT TO CIE LUV
    def ConvertLUV(self):
        self.image= cv2.cvtColor(self.image, cv2.COLOR_BGR2Luv)
        luvImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(luvImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    # CONVERT TO HLS
    def ConvertHLS(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HLS)
        hlsImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(hlsImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    # INFORMATION FOR EDIT TAB
    def InfoE(self):
        msg=QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Click show details for examples to input value")
        msg.setInformativeText("After clicked Gray Scale, must click BGRA")
        msg.setDetailedText("Resize: [50,50]"+"                                                           "
                            +"Crop: [0,0,300,300]"+"                                              "
                            +"Translate: [100,100]"+"                                              "+"Rotate: [30]")
        x=msg.exec_()

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    #EDIT 2 TAB
    #GAUSSIAN BLUR
    def comboG(self):
        text=str(self.comboBox_3.currentText())
        if text == '(3,3)':
            self.gaussian1()
        elif text == '(5,5)':
            self.gaussian2()
        elif text == '(7,7)':
            self.gaussian3()
        elif text == '(9,9)':
            self.gaussian4()
        elif text == '(11,11)':
            self.gaussian5()
    def gaussian1(self):
        self.image = cv2.GaussianBlur(self.image, (3, 3), 0)
        gblur1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                                QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(gblur1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def gaussian2(self):
        self.image = cv2.GaussianBlur(self.image, (5, 5), 0)
        gblur2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                                QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(gblur2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def gaussian3(self):
        self.image = cv2.GaussianBlur(self.image, (7, 7), 0)
        gblur3 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                                QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(gblur3)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def gaussian4(self):
        self.image = cv2.GaussianBlur(self.image, (9, 9), 0)
        gblur4 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                                QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(gblur4)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def gaussian5(self):
        self.image = cv2.GaussianBlur(self.image, (11, 11), 0)
        gblur5 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                                QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(gblur5)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # MEDIAN BLUR
    def comboM(self):
        text = str(self.comboBox_4.currentText())
        if text == '9':
            self.median1()
        elif text == '11':
            self.median2()
        elif text == '13':
            self.median3()
        elif text == '15':
            self.median4()
        elif text == '17':
            self.median5()
    def median1(self):
        self.image = cv2.medianBlur(self.image, 9)
        mblur1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(mblur1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def median2(self):
        self.image = cv2.medianBlur(self.image, 11)
        mblur2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(mblur2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def median3(self):
        self.image = cv2.medianBlur(self.image, 13)
        mblur3 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(mblur3)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def median4(self):
        self.image = cv2.medianBlur(self.image, 15)
        mblur4 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(mblur4)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def median5(self):
        self.image = cv2.medianBlur(self.image, 17)
        mblur5 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(mblur5)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # AVERAGE BLUR
    def comboA(self):
        text = str(self.comboBox_6.currentText())
        if text == '(3,3)':
            self.average1()
        elif text == '(5,5)':
            self.average2()
        elif text == '(7,7)':
            self.average3()
        elif text == '(9,9)':
            self.average4()
        elif text == '(11,11)':
            self.average5()
    def average1(self):
        self.image = cv2.blur(self.image, (11, 11))
        ablur1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(ablur1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def average2(self):
        self.image = cv2.blur(self.image, (5, 5))
        ablur2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(ablur2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def average3(self):
        self.image = cv2.blur(self.image, (7, 7))
        ablur3 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(ablur3)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def average4(self):
        self.image = cv2.blur(self.image, (9, 9))
        ablur4 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(ablur4)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def average5(self):
        self.image = cv2.blur(self.image, (11, 11))
        ablur5 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(ablur5)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # BILATERAL FILTER
    def comboB(self):
        text = str(self.comboBox_5.currentText())
        if text == '9':
            self.bilateral1()
        elif text == '11':
            self.bilateral2()
        elif text == '13':
            self.bilateral3()
        elif text == '15':
            self.bilateral4()
        elif text == '17':
            self.bilateral5()
    def bilateral1(self):
        self.image = cv2.bilateralFilter(self.image, 9, 75, 75)
        bblur1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(bblur1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def bilateral2(self):
        self.image = cv2.bilateralFilter(self.image, 11, 75, 75)
        bblur2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(bblur2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def bilateral3(self):
        self.image = cv2.bilateralFilter(self.image, 13, 75, 75)
        bblur3 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(bblur3)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def bilateral4(self):
        self.image = cv2.bilateralFilter(self.image, 15, 75, 75)
        bblur4 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(bblur4)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def bilateral5(self):
        self.image = cv2.bilateralFilter(self.image, 17, 75, 75)
        bblur5 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(bblur5)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # BOX BLUR
    def comboBO(self):
        text = str(self.comboBox_7.currentText())
        if text == '(3,3)':
            self.box1()
        elif text == '(5,5)':
            self.box2()
        elif text == '(7,7)':
            self.box3()
        elif text == '(9,9)':
            self.box4()
        elif text == '(11,11)':
            self.box5()
    def box1(self):
        self.image = cv2.boxFilter(self.image, 0, (3, 3))
        boblur1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(boblur1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def box2(self):
        self.image = cv2.boxFilter(self.image, 0, (5, 5))
        boblur2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(boblur2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def box3(self):
        self.image = cv2.boxFilter(self.image, 0, (7, 7))
        boblur3 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(boblur3)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def box4(self):
        self.image = cv2.boxFilter(self.image, 0, (9, 9))
        boblur4 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(boblur4)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def box5(self):
        self.image = cv2.boxFilter(self.image, 0, (11, 11))
        boblur5 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                              QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(boblur5)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # CONTRAST
    def comboC(self):
        text = str(self.comboBox_8.currentText())
        if text == '0.5':
            self.contrast1()
        elif text == '2.5':
            self.contrast2()
        elif text == '4.5':
            self.contrast3()
        elif text == '6.5':
            self.contrast4()
        elif text == '8.5':
            self.contrast5()
    def contrast1(self):
        self.image = cv2.addWeighted(self.image, 0.5, np.zeros(self.image.shape, self.image.dtype), 0, 0)
        con1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                               QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(con1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def contrast2(self):
        self.image = cv2.addWeighted(self.image, 2.5, np.zeros(self.image.shape, self.image.dtype), 0, 0)
        con2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                               QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(con2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def contrast3(self):
        self.image = cv2.addWeighted(self.image, 4.5, np.zeros(self.image.shape, self.image.dtype), 0, 0)
        con3 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                               QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(con3)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def contrast4(self):
        self.image = cv2.addWeighted(self.image, 6.5, np.zeros(self.image.shape, self.image.dtype), 0, 0)
        con4 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                               QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(con4)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def contrast5(self):
        self.image = cv2.addWeighted(self.image, 8.5, np.zeros(self.image.shape, self.image.dtype), 0, 0)
        con5 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                               QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(con5)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # SHARPENING
    def comboS(self):
        text = str(self.comboBox_9.currentText())
        if text == 'Sharpen 1':
            self.sharpen1()
        elif text == 'Sharpen 2':
            self.sharpen2()
    def sharpen1(self):
        kernel_sharpening = np.array([[-1, -1, -1],
                                      [-1, 9, -1],
                                      [-1, -1, -1]])
        self.image = cv2.filter2D(self.image, -1, kernel_sharpening)
        sha1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                            QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(sha1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def sharpen2(self):
        kernel_sharpening = np.array([[-1, -1, -1, -1, -1],
                                      [-1, -1, -1, -1, -1],
                                      [-1, -1, 25, -1, -1],
                                      [-1, -1, -1, -1, -1],
                                      [-1, -1, -1, -1, -1]])
        self.image = cv2.filter2D(self.image, -1, kernel_sharpening)
        sha2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                            QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(sha2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # GRAY SCALE HISTOGRAM EQUALIZATION
    def grayHE(self):
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.equalizeGrayImage = cv2.equalizeHist(self.gray_image)
        hist = cv2.calcHist(self.equalizeGrayImage, [0], None, [256], [0, 256])
        plt.plot(hist, color='k')
        plt.hist(self.equalizeGrayImage.flatten(), 256, [0, 256])
        plt.show()

        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.equalizeHist(self.gray_image)
        self.qformat = QImage.Format_Grayscale8
        self.img = QtGui.QImage(self.image, int(self.image.shape[1]), int(self.image.shape[0]), int(self.qformat))
        # self.label_4.setPixmap((QtGui.QPixmap.scaled(QtGui.QPixmap.fromImage(self.img), int(self.image.shape[1]),
        #                                            int(self.image.shape[0]), QtCore.Qt.KeepAspectRatio,
        #                                            QtCore.Qt.SmoothTransformation)))
        self.label_4.setPixmap((QtGui.QPixmap.scaled(QtGui.QPixmap.fromImage(self.img), 900,500, QtCore.Qt.KeepAspectRatio,
                                                     QtCore.Qt.SmoothTransformation)))
    # COLOR HISTOGRAM EQUALIZATION
    def colorHE(self):
        self.channels = cv2.split(self.image)
        self.eqChannels = []
        for ch, color in zip(self.channels, ['B', 'G', 'R']):
            self.eqChannels.append(cv2.equalizeHist(ch))
        self.eqImage = cv2.merge(self.eqChannels)
        self.eqImage = cv2.cvtColor(self.eqImage, cv2.COLOR_BGR2RGB)
        for i, col in enumerate(['b', 'g', 'r']):
            hist = cv2.calcHist([self.eqImage], [i], None, [256], [0, 256])
            plt.plot(hist, color=col)
            plt.xlim([0, 256])
            plt.hist(self.eqImage.flatten(), 256, [0, 256])
        plt.show()

        self.channels = cv2.split(self.image)
        self.eqChannels = []
        for ch, color in zip(self.channels, ['B', 'G', 'R']):
            self.eqChannels.append(cv2.equalizeHist(ch))
        self.image = cv2.merge(self.eqChannels)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2BGRA)
        self.qformat = QImage.Format_ARGB32
        self.img = QtGui.QImage(self.image, int(self.image.shape[1]), int(self.image.shape[0]), int(self.qformat))
        # self.label_4.setPixmap((QtGui.QPixmap.scaled(QtGui.QPixmap.fromImage(self.img), int(self.image.shape[1]),
        #                                            int(self.image.shape[0]), QtCore.Qt.KeepAspectRatio,
        #                                            QtCore.Qt.SmoothTransformation)))
        self.label_4.setPixmap((QtGui.QPixmap.scaled(QtGui.QPixmap.fromImage(self.img), 900,500, QtCore.Qt.KeepAspectRatio,
                                                     QtCore.Qt.SmoothTransformation)))
    # INFORMATION FOR FILTERING AND SPILT MERGE
    def InfoE2(self):
        msg=QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Click shows details for examples to input value")
        # msg.setInformativeText("Click O.I. for getting back original image")
        msg.setDetailedText("All the choice given is the kernel size. [Filtering] "
                            "1x2 means 1 row and 2 columns, and so on. The image can only split and merge until 3x3 only with same image size. [Split Merge]")
        x=msg.exec_()

    # SPLIT
    def splitCombo(self):
        text = str(self.comboBox_10.currentText())
        if text == '1x2':
            self.split1()
        elif text == '1x3':
            self.split2()
        elif text == '2x1':
            self.split3()
        elif text == '2x2':
            self.split4()
        elif text == '2x3':
            self.split5()
        elif text == '3x1':
            self.split6()
        elif text == '3x2':
            self.split7()
        elif text == '3x3':
            self.split8()
    def split1(self):
        self.ws=spw1()
        self.ws.show()
    def split2(self):
        self.ws1=spw2()
        self.ws1.show()
    def split3(self):
        self.ws2=spw3()
        self.ws2.show()
    def split4(self):
        self.ws3=spw4()
        self.ws3.show()
    def split5(self):
        self.ws4=spw5()
        self.ws4.show()
    def split6(self):
        self.ws5=spw6()
        self.ws5.show()
    def split7(self):
        self.ws6=spw7()
        self.ws6.show()
    def split8(self):
        self.ws7=spw8()
        self.ws7.show()

    # MERGE
    def mergeCombo(self):
        text = str(self.comboBox_11.currentText())
        if text == '1x2':
            self.merge1()
        elif text == '1x3':
            self.merge2()
        elif text == '2x1':
            self.merge3()
        elif text == '2x2':
            self.merge4()
        elif text == '2x3':
            self.merge5()
        elif text == '3x1':
            self.merge6()
        elif text == '3x2':
            self.merge7()
        elif text == '3x3':
            self.merge8()
    def merge1(self):
        self.wm=mgw1()
        self.wm.show()
    def merge2(self):
        self.wm1=mgw2()
        self.wm1.show()
    def merge3(self):
        self.wm2=mgw3()
        self.wm2.show()
    def merge4(self):
        self.wm3=mgw4()
        self.wm3.show()
    def merge5(self):
        self.wm4=mgw5()
        self.wm4.show()
    def merge6(self):
        self.wm5=mgw6()
        self.wm5.show()
    def merge7(self):
        self.wm6=mgw7()
        self.wm6.show()
    def merge8(self):
        self.wm7=mgw8()
        self.wm7.show()

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    #EDIT 3 TAB
    #PREWITT EDGE DETECTION
    def prewittCombo(self):
        text = str(self.comboBox_12.currentText())
        if text == 'x':
            self.prewittX()
        elif text == 'y':
            self.prewittY()
        elif text == 'x and y':
            self.prewitt()
    def prewittX(self):
        kernel_Prewitt_x = np.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]])
        # pX = cv2.filter2D(self.image, -1, kernel_Prewitt_x)
        # pX = np.uint8(np.absolute(pX))
        self.image = cv2.filter2D(self.image, -1, kernel_Prewitt_x)
        preX = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                           QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(preX)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def prewittY(self):
        kernel_Prewitt_y = np.array([
            [1, 1, 1],
            [0, 0, 0],
            [-1, -1, -1]])
        # pY = cv2.filter2D(self.image, -1, kernel_Prewitt_y)
        # pY = np.uint8(np.absolute(pY))
        self.image = cv2.filter2D(self.image, -1, kernel_Prewitt_y)
        preY = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                            QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(preY)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def prewitt(self):
        kernel_Prewitt_x = np.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]])
        kernel_Prewitt_y = np.array([
            [1, 1, 1],
            [0, 0, 0],
            [-1, -1, -1]])
        pX = cv2.filter2D(self.image, -1, kernel_Prewitt_x)
        pY = cv2.filter2D(self.image, -1, kernel_Prewitt_y)
        pX = np.uint8(np.absolute(pX))
        pY = np.uint8(np.absolute(pY))
        self.image = cv2.bitwise_or(pX, pY)
        pre = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                           QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(pre)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # ROBERT EDGE DETECTION
    def robertCombo(self):
        text = str(self.comboBox_13.currentText())
        if text == 'x':
            self.robertX()
        elif text == 'y':
            self.robertY()
        elif text == 'x and y':
            self.robert()
    def robertX(self):
        kernel_Roberts_x = np.array([
            [1, 0],
            [0, -1]
        ])
        self.image = cv2.filter2D(self.image, -1, kernel_Roberts_x)
        robX = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                           QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(robX)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def robertY(self):
        kernel_Roberts_y = np.array([
            [0, -1],
            [1, 0]
        ])
        self.image = cv2.filter2D(self.image, -1, kernel_Roberts_y)
        robY = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                            QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(robY)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def robert(self):
        kernel_Roberts_x = np.array([
            [1, 0],
            [0, -1]
        ])
        kernel_Roberts_y = np.array([
            [0, -1],
            [1, 0]
        ])
        robertX = cv2.filter2D(self.image, -1, kernel_Roberts_x)
        robertY = cv2.filter2D(self.image, -1, kernel_Roberts_y)
        robertX = np.uint8(np.absolute(robertX))
        robertY = np.uint8(np.absolute(robertY))
        self.image = cv2.bitwise_or(robertX, robertY)
        rob = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                           QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(rob)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # SOBEL EDGE DETECTION
    def sobelCombo(self):
        text = str(self.comboBox_14.currentText())
        if text == 'x':
            self.sobelX()
        elif text == 'y':
            self.sobelY()
        elif text == 'x and y':
            self.sobel()
    def sobelX(self):
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.Sobel(self.gray_image, cv2.CV_64F, 1, 0)
        self.image = np.uint8(np.absolute(self.image))
        sobX = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(sobX)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def sobelY(self):
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image= cv2.Sobel(self.gray_image, cv2.CV_64F, 0, 1)
        self.image = np.uint8(np.absolute(self.image))
        sobY = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(sobY)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def sobel(self):
        sobelX = cv2.Sobel(self.gray_image, cv2.CV_64F, 1, 0)
        sobelY = cv2.Sobel(self.gray_image, cv2.CV_64F, 0, 1)
        sobelX = np.uint8(np.absolute(sobelX))
        sobelY = np.uint8(np.absolute(sobelY))
        self.image = cv2.bitwise_or(sobelX, sobelY)
        sob = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(sob)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # CANNY EDGE DETECTION
    def canny(self):
        t1 = int(self.textEdit_30.toPlainText())
        t2 = int(self.textEdit_31.toPlainText())
        self.grayimage = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.Canny(self.grayimage, t1, t2)
        can = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(can)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # LAPLACIAN EDGE DETECTION
    def laplacian(self):
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGRA2GRAY)
        lap = cv2.Laplacian(self.gray_image, cv2.CV_64F)
        self.image = np.uint8(np.absolute(lap))
        grayImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(grayImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # THRESHOLDING IMAGE SEGMENTATION
    def thresholdCombo(self):
        text = str(self.comboBox_15.currentText())
        if text == 'Thresholding BINARY':
            self.thresholding1()
        elif text == 'Thresholding BINARYINV':
            self.thresholding2()
        elif text == 'Thresholding TRUNC':
            self.thresholding3()
        elif text == 'Thresholding TOZERO':
            self.thresholding4()
        elif text == 'Thresholding TOZEROINV':
            self.thresholding5()
    def thresholding1(self):
        thr = int(self.textEdit_32.toPlainText())
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        retval, self.image = cv2.threshold(self.gray_image, thr, 255, cv2.THRESH_BINARY)
        grayImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(grayImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def thresholding2(self):
        thr = int(self.textEdit_32.toPlainText())
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        retval, self.image = cv2.threshold(self.gray_image, thr, 255, cv2.THRESH_BINARY_INV)
        grayImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(grayImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def thresholding3(self):
        thr = int(self.textEdit_32.toPlainText())
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        retval, self.image = cv2.threshold(self.gray_image, thr, 255, cv2.THRESH_TRUNC)
        grayImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(grayImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def thresholding4(self):
        thr = int(self.textEdit_32.toPlainText())
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        retval, self.image = cv2.threshold(self.gray_image, thr, 255, cv2.THRESH_TOZERO)
        grayImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(grayImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def thresholding5(self):
        thr = int(self.textEdit_32.toPlainText())
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        retval, self.image = cv2.threshold(self.gray_image, thr, 255, cv2.THRESH_TOZERO_INV)
        grayImage = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1],
                                 QImage.Format_Grayscale8)
        self.pixmap = QtGui.QPixmap(grayImage)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    # CLUSTER IMAGE SEGMENTATION
    def clusterCombo(self):
        text = str(self.comboBox_16.currentText())
        if text == 'KMeansRandomCenters':
            self.cluster1()
        elif text == 'KMeansPPCenters':
            self.cluster2()
    def cluster1(self):
        maxI = int(self.textEdit_33.toPlainText())
        eps = float(self.textEdit_34.toPlainText())
        k = int(self.textEdit_35.toPlainText())
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        pixel_values = image.reshape((-1, 3))
        pixel_values = np.float32(pixel_values)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, maxI, eps)
        retval, labels, centers= cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        labels = labels.flatten()
        segmented_image = centers[labels.flatten()]
        self.image = segmented_image.reshape(image.shape)
        clus1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                           QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(clus1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def cluster2(self):
        maxI = int(self.textEdit_33.toPlainText())
        eps = float(self.textEdit_34.toPlainText())
        k = int(self.textEdit_35.toPlainText())
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        pixel_values = image.reshape((-1, 3))
        pixel_values = np.float32(pixel_values)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, maxI, eps)
        retval, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
        centers = np.uint8(centers)
        labels = labels.flatten()
        segmented_image = centers[labels.flatten()]
        self.image = segmented_image.reshape(image.shape)
        clus2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(clus2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    # CLUSTER DISABLE IMAGE SEGMENTATION
    def clusterDCombo(self):
        text = str(self.comboBox_17.currentText())
        if text == 'Cluster Disable RANDOM':
            self.clusterDisableR()
        elif text == 'Cluster Disable PP':
            self.clusterDisableP()
    def clusterDisableR(self):
        maxI = int(self.textEdit_33.toPlainText())
        eps = float(self.textEdit_34.toPlainText())
        k = int(self.textEdit_35.toPlainText())
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        pixel_values = image.reshape((-1, 3))
        pixel_values = np.float32(pixel_values)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, maxI, eps)
        retval, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        labels = labels.flatten()
        segmented_image = centers[labels.flatten()]
        self.image = segmented_image.reshape(image.shape)
        cls = int(self.textEdit_36.toPlainText())
        masked_image = np.copy(image)
        masked_image = masked_image.reshape((-1, 3))
        masked_image[labels == cls] = [0, 0, 0]
        self.image = masked_image.reshape(image.shape)
        clus1 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(clus1)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)
    def clusterDisableP(self):
        maxI = int(self.textEdit_33.toPlainText())
        eps = float(self.textEdit_34.toPlainText())
        k = int(self.textEdit_35.toPlainText())
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        pixel_values = image.reshape((-1, 3))
        pixel_values = np.float32(pixel_values)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, maxI, eps)
        retval, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
        centers = np.uint8(centers)
        labels = labels.flatten()
        segmented_image = centers[labels.flatten()]
        self.image = segmented_image.reshape(image.shape)
        cls = int(self.textEdit_36.toPlainText())
        masked_image = np.copy(image)
        masked_image = masked_image.reshape((-1, 3))
        masked_image[labels == cls] = [0, 0, 0]
        self.image = masked_image.reshape(image.shape)
        clus2 = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(clus2)
        self.pixmap = self.pixmap.scaled(900, 500, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

    def InfoE3(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Click shows details for examples to input value")
        # msg.setInformativeText("Click O.I. for getting back original image")
        msg.setDetailedText("Canny: [30,200]"+"                                                 "+"Threshold: [128]"+"                                             "
                            +"Cluster: [100,0.2,3,2(For cluster disable value must smaller than number of cluster)]")
        x = msg.exec_()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Win()
    window.show()
    sys.exit(app.exec())