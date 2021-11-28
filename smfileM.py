import sys
import cv2
import math
import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QTransform
from smfile import Ui_sp1win, Ui_sp2win, Ui_sp3win, Ui_sp4win, Ui_sp5win, Ui_sp6win, Ui_sp7win, Ui_sp8win, Ui_mg1win, Ui_mg2win, Ui_mg3win, Ui_mg4win, Ui_mg5win, Ui_mg6win, Ui_mg7win, Ui_mg8win

class spw1(QtWidgets.QMainWindow, Ui_sp1win):
    def __init__(self):
        super(spw1, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_sp1win.__init__(self)
        self.setupUi(self)

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(300, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpg);;Image Files (*.tiff);;Image Files (*.bmp)")
        for i in range(len(self.listImg)):
            if fname.endswith(".jpg"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".jpg"
            elif fname.endswith(".tiff"):
                name = fname[0:len(fname) - 5] + "_" + str(i + 1) + ".tiff"
            elif fname.endswith(".bmp"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".bmp"
            if name:
                cv2.imwrite(name, self.listImg[i])
            else:
                print('Error')

    def split1(self):
        self.imgWidth=self.image.shape[1]
        averageWidth = math.ceil(self.imgWidth / 2)
        img_1, img_2 = np.hsplit(self.image, [averageWidth])
        self.listImg = [img_1, img_2]

        img_1 = np.require(img_1, np.uint8, 'C')
        img_2 = np.require(img_2, np.uint8, 'C')

        image1 = QtGui.QImage(img_1, img_1.shape[1], img_1.shape[0], img_1.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image1)
        self.pixmap = self.pixmap.scaled(200, 500, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap)

        image2 = QtGui.QImage(img_2, img_2.shape[1], img_2.shape[0], img_2.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image2)
        self.pixmap = self.pixmap.scaled(200, 500, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class spw2(QtWidgets.QMainWindow, Ui_sp2win):
    def __init__(self):
        super(spw2, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_sp2win.__init__(self)
        self.setupUi(self)

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(300, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpg);;Image Files (*.tiff);;Image Files (*.bmp)")
        for i in range(len(self.listImg)):
            if fname.endswith(".jpg"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".jpg"
            elif fname.endswith(".tiff"):
                name = fname[0:len(fname) - 5] + "_" + str(i + 1) + ".tiff"
            elif fname.endswith(".bmp"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".bmp"
            if name:
                cv2.imwrite(name, self.listImg[i])
            else:
                print('Error')

    def split2(self):
        self.imgWidth=self.image.shape[1]
        averageWidth = math.ceil(self.imgWidth / 3)
        img_1, img_2, img_3 = np.hsplit(self.image, [averageWidth, averageWidth * 2])
        self.listImg = [img_1, img_2, img_3]

        img_1 = np.require(img_1, np.uint8, 'C')
        img_2 = np.require(img_2, np.uint8, 'C')
        img_3 = np.require(img_3, np.uint8, 'C')

        image1 = QtGui.QImage(img_1, img_1.shape[1], img_1.shape[0], img_1.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image1)
        self.pixmap = self.pixmap.scaled(200, 400, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap)

        image2 = QtGui.QImage(img_2, img_2.shape[1], img_2.shape[0], img_2.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image2)
        self.pixmap = self.pixmap.scaled(200, 400, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)

        image3 = QtGui.QImage(img_3, img_3.shape[1], img_3.shape[0], img_3.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image3)
        self.pixmap = self.pixmap.scaled(200, 400, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class spw3(QtWidgets.QMainWindow, Ui_sp3win):
    def __init__(self):
        super(spw3, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_sp3win.__init__(self)
        self.setupUi(self)

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(300, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpg);;Image Files (*.tiff);;Image Files (*.bmp)")
        for i in range(len(self.listImg)):
            if fname.endswith(".jpg"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".jpg"
            elif fname.endswith(".tiff"):
                name = fname[0:len(fname) - 5] + "_" + str(i + 1) + ".tiff"
            elif fname.endswith(".bmp"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".bmp"
            if name:
                cv2.imwrite(name, self.listImg[i])
            else:
                print('Error')

    def split3(self):
        self.imgHeight=self.image.shape[0]
        averageHeight = math.ceil(self.imgHeight / 2)
        img_1, img_2 = np.vsplit(self.image, [averageHeight])
        self.listImg = [img_1, img_2]

        image1 = QtGui.QImage(img_1, img_1.shape[1], img_1.shape[0], img_1.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image1)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap)

        image2 = QtGui.QImage(img_2, img_2.shape[1], img_2.shape[0], img_2.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image2)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class spw4(QtWidgets.QMainWindow, Ui_sp4win):
    def __init__(self):
        super(spw4, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_sp4win.__init__(self)
        self.setupUi(self)

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(300, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpg);;Image Files (*.tiff);;Image Files (*.bmp)")
        for i in range(len(self.listImg)):
            if fname.endswith(".jpg"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".jpg"
            elif fname.endswith(".tiff"):
                name = fname[0:len(fname) - 5] + "_" + str(i + 1) + ".tiff"
            elif fname.endswith(".bmp"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".bmp"
            if name:
                cv2.imwrite(name, self.listImg[i])
            else:
                print('Error')

    def split4(self):
        self.imgHeight=self.image.shape[0]
        self.imgWidth=self.image.shape[1]
        averageWidth = math.ceil(self.imgWidth / 2)
        img_1, img_2 = np.hsplit(self.image, [averageWidth])
        averageHeight = math.ceil(self.imgHeight / 2)
        img_3, img_4 = np.vsplit(img_1, [averageHeight])
        averageHeight = math.ceil(self.imgHeight / 2)
        img_5, img_6 = np.vsplit(img_2, [averageHeight])
        self.listImg = [img_3, img_4, img_5, img_6]

        img_3 = np.require(img_3, np.uint8, 'C')
        img_4 = np.require(img_4, np.uint8, 'C')
        img_5 = np.require(img_5, np.uint8, 'C')
        img_6 = np.require(img_6, np.uint8, 'C')

        image1 = QtGui.QImage(img_3, img_3.shape[1], img_3.shape[0], img_3.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image1)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap)

        image2 = QtGui.QImage(img_4, img_4.shape[1], img_4.shape[0], img_4.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image2)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

        image3 = QtGui.QImage(img_5, img_5.shape[1], img_5.shape[0], img_5.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image3)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)

        image4 = QtGui.QImage(img_6, img_6.shape[1], img_6.shape[0], img_6.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image4)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_5.setPixmap(self.pixmap)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class spw5(QtWidgets.QMainWindow, Ui_sp5win):
    def __init__(self):
        super(spw5, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_sp5win.__init__(self)
        self.setupUi(self)

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(300, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpg);;Image Files (*.tiff);;Image Files (*.bmp)")
        for i in range(len(self.listImg)):
            if fname.endswith(".jpg"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".jpg"
            elif fname.endswith(".tiff"):
                name = fname[0:len(fname) - 5] + "_" + str(i + 1) + ".tiff"
            elif fname.endswith(".bmp"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".bmp"
            if name:
                cv2.imwrite(name, self.listImg[i])
            else:
                print('Error')

    def split5(self):
        self.imgHeight=self.image.shape[0]
        self.imgWidth=self.image.shape[1]
        averageWidth = math.ceil(self.imgWidth / 3)
        img_1, img_2, img_3 = np.hsplit(self.image, [averageWidth, averageWidth * 2])
        averageHeight = math.ceil(self.imgHeight / 2)
        img_4, img_5 = np.vsplit(img_1, [averageHeight])
        averageHeight = math.ceil(self.imgHeight / 2)
        img_6, img_7 = np.vsplit(img_2, [averageHeight])
        averageHeight = math.ceil(self.imgHeight / 2)
        img_8, img_9 = np.vsplit(img_3, [averageHeight])
        self.listImg = [img_4, img_5, img_6, img_7, img_8, img_9]

        img_4 = np.require(img_4, np.uint8, 'C')
        img_5 = np.require(img_5, np.uint8, 'C')
        img_6 = np.require(img_6, np.uint8, 'C')
        img_7 = np.require(img_7, np.uint8, 'C')
        img_8 = np.require(img_8, np.uint8, 'C')
        img_9 = np.require(img_9, np.uint8, 'C')

        image1 = QtGui.QImage(img_4, img_4.shape[1], img_4.shape[0], img_4.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image1)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap)

        image2 = QtGui.QImage(img_5, img_5.shape[1], img_5.shape[0], img_5.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image2)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_5.setPixmap(self.pixmap)

        image3 = QtGui.QImage(img_6, img_6.shape[1], img_6.shape[0], img_6.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image3)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)

        image4 = QtGui.QImage(img_7, img_7.shape[1], img_7.shape[0], img_7.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image4)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_6.setPixmap(self.pixmap)

        image5 = QtGui.QImage(img_8, img_8.shape[1], img_8.shape[0], img_8.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image5)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

        image6 = QtGui.QImage(img_9, img_9.shape[1], img_9.shape[0], img_9.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image6)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_7.setPixmap(self.pixmap)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class spw6(QtWidgets.QMainWindow, Ui_sp6win):
    def __init__(self):
        super(spw6, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_sp6win.__init__(self)
        self.setupUi(self)

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(300, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpg);;Image Files (*.tiff);;Image Files (*.bmp)")
        for i in range(len(self.listImg)):
            if fname.endswith(".jpg"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".jpg"
            elif fname.endswith(".tiff"):
                name = fname[0:len(fname) - 5] + "_" + str(i + 1) + ".tiff"
            elif fname.endswith(".bmp"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".bmp"
            if name:
                cv2.imwrite(name, self.listImg[i])
            else:
                print('Error')

    def split6(self):
        self.imgHeight=self.image.shape[0]
        averageHeight = math.ceil(self.imgHeight / 3)
        img_1, img_2, img_3 = np.vsplit(self.image, [averageHeight, averageHeight * 2])
        self.listImg = [img_1, img_2, img_3]

        image1 = QtGui.QImage(img_1, img_1.shape[1], img_1.shape[0], img_1.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image1)
        self.pixmap = self.pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap)

        image2 = QtGui.QImage(img_2, img_2.shape[1], img_2.shape[0], img_2.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image2)
        self.pixmap = self.pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)

        image3 = QtGui.QImage(img_3, img_3.shape[1], img_3.shape[0], img_3.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image3)
        self.pixmap = self.pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class spw7(QtWidgets.QMainWindow, Ui_sp7win):
    def __init__(self):
        super(spw7, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_sp7win.__init__(self)
        self.setupUi(self)

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(300, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpg);;Image Files (*.tiff);;Image Files (*.bmp)")
        for i in range(len(self.listImg)):
            if fname.endswith(".jpg"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".jpg"
            elif fname.endswith(".tiff"):
                name = fname[0:len(fname) - 5] + "_" + str(i + 1) + ".tiff"
            elif fname.endswith(".bmp"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".bmp"
            if name:
                cv2.imwrite(name, self.listImg[i])
            else:
                print('Error')

    def split7(self):
        self.imgHeight=self.image.shape[0]
        self.imgWidth=self.image.shape[1]
        averageWidth = math.ceil(self.imgWidth / 2)
        img_1, img_2 = np.hsplit(self.image, [averageWidth])
        averageHeight = math.ceil(self.imgHeight / 3)
        img_3, img_4, img_5 = np.vsplit(img_1, [averageHeight, averageHeight * 2])
        averageHeight = math.ceil(self.imgHeight / 3)
        img_6, img_7, img_8 = np.vsplit(img_2, [averageHeight, averageHeight * 2])
        self.listImg = [img_3, img_4, img_5, img_6, img_7, img_8]

        img_3 = np.require(img_3, np.uint8, 'C')
        img_4 = np.require(img_4, np.uint8, 'C')
        img_5 = np.require(img_5, np.uint8, 'C')
        img_6 = np.require(img_6, np.uint8, 'C')
        img_7 = np.require(img_7, np.uint8, 'C')
        img_8 = np.require(img_8, np.uint8, 'C')

        image1 = QtGui.QImage(img_3, img_3.shape[1], img_3.shape[0], img_3.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image1)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap)

        image2 = QtGui.QImage(img_4, img_4.shape[1], img_4.shape[0], img_4.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image2)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

        image3 = QtGui.QImage(img_5, img_5.shape[1], img_5.shape[0], img_5.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image3)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_6.setPixmap(self.pixmap)

        image4 = QtGui.QImage(img_6, img_6.shape[1], img_6.shape[0], img_6.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image4)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)

        image5 = QtGui.QImage(img_7, img_7.shape[1], img_7.shape[0], img_7.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image5)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_5.setPixmap(self.pixmap)

        image6 = QtGui.QImage(img_8, img_8.shape[1], img_8.shape[0], img_8.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image6)
        self.pixmap = self.pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_7.setPixmap(self.pixmap)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class spw8(QtWidgets.QMainWindow, Ui_sp8win):
    def __init__(self):
        super(spw8, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_sp8win.__init__(self)
        self.setupUi(self)

    def OpenFile(self):
        self.name = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.image = cv2.imread(self.name)
        self.pixmap = QtGui.QPixmap(self.name)
        self.pixmap = self.pixmap.scaled(300, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpg);;Image Files (*.tiff);;Image Files (*.bmp)")
        for i in range(len(self.listImg)):
            if fname.endswith(".jpg"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".jpg"
            elif fname.endswith(".tiff"):
                name = fname[0:len(fname) - 5] + "_" + str(i + 1) + ".tiff"
            elif fname.endswith(".bmp"):
                name = fname[0:len(fname) - 4] + "_" + str(i + 1) + ".bmp"
            if name:
                cv2.imwrite(name, self.listImg[i])
            else:
                print('Error')

    def split8(self):
        self.imgHeight=self.image.shape[0]
        self.imgWidth=self.image.shape[1]
        averageWidth = math.ceil(self.imgWidth / 3)
        img_1, img_2, img_3 = np.hsplit(self.image, [averageWidth, averageWidth * 2])
        averageHeight = math.ceil(self.imgHeight / 3)
        img_4, img_5, img_6 = np.vsplit(img_1, [averageHeight, averageHeight * 2])
        averageHeight = math.ceil(self.imgHeight / 3)
        img_7, img_8, img_9 = np.vsplit(img_2, [averageHeight, averageHeight * 2])
        averageHeight = math.ceil(self.imgHeight / 3)
        img_10, img_11, img_12 = np.vsplit(img_3, [averageHeight, averageHeight * 2])
        self.listImg = [img_4, img_5, img_6, img_7, img_8, img_9, img_10, img_11, img_12]

        img_4 = np.require(img_4, np.uint8, 'C')
        img_5 = np.require(img_5, np.uint8, 'C')
        img_6 = np.require(img_6, np.uint8, 'C')
        img_7 = np.require(img_7, np.uint8, 'C')
        img_8 = np.require(img_8, np.uint8, 'C')
        img_9 = np.require(img_9, np.uint8, 'C')
        img_10 = np.require(img_10, np.uint8, 'C')
        img_11 = np.require(img_11, np.uint8, 'C')
        img_12 = np.require(img_12, np.uint8, 'C')

        image1 = QtGui.QImage(img_4, img_4.shape[1], img_4.shape[0], img_4.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image1)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(self.pixmap)

        image2 = QtGui.QImage(img_5, img_5.shape[1], img_5.shape[0], img_5.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image2)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_5.setPixmap(self.pixmap)

        image3 = QtGui.QImage(img_6, img_6.shape[1], img_6.shape[0], img_6.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image3)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_8.setPixmap(self.pixmap)

        image4 = QtGui.QImage(img_7, img_7.shape[1], img_7.shape[0], img_7.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image4)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(self.pixmap)

        image5 = QtGui.QImage(img_8, img_8.shape[1], img_8.shape[0], img_8.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image5)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_6.setPixmap(self.pixmap)

        image6 = QtGui.QImage(img_9, img_9.shape[1], img_9.shape[0], img_9.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image6)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_9.setPixmap(self.pixmap)

        image7 = QtGui.QImage(img_10, img_10.shape[1], img_10.shape[0], img_10.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image7)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(self.pixmap)

        image8 = QtGui.QImage(img_11, img_11.shape[1], img_11.shape[0], img_11.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image8)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_7.setPixmap(self.pixmap)

        image9 = QtGui.QImage(img_12, img_12.shape[1], img_12.shape[0], img_12.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image9)
        self.pixmap = self.pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.label_10.setPixmap(self.pixmap)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class mgw1(QtWidgets.QMainWindow,Ui_mg1win):
    def __init__(self):
        super(mgw1, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_mg1win.__init__(self)
        self.setupUi(self)

    def Reset(self):
        self.label.clear()
    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.view)
        else:
            print('Error')

    def merge1(self):
        self.image1=cv2.imread(self.name1)
        self.image2=cv2.imread(self.name2)
        self.view=cv2.hconcat([self.image1,self.image2])
        image = QtGui.QImage(self.view, self.view.shape[1], self.view.shape[0], self.view.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def m1(self):
        self.name1 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname=str(self.textEdit.setText(self.name1))
    def m2(self):
        self.name2 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname1=str(self.textEdit_2.setText(self.name2))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class mgw2(QtWidgets.QMainWindow, Ui_mg2win):
    def __init__(self):
        super(mgw2, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_mg2win.__init__(self)
        self.setupUi(self)

    def Reset(self):
        self.label.clear()

    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                              "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.view)
        else:
            print('Error')

    def merge2(self):
        self.image1=cv2.imread(self.name1)
        self.image2=cv2.imread(self.name2)
        self.image3 = cv2.imread(self.name3)
        self.view=cv2.hconcat([self.image1,self.image2,self.image3])
        image = QtGui.QImage(self.view, self.view.shape[1], self.view.shape[0], self.view.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def m1(self):
        self.name1 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname=str(self.textEdit.setText(self.name1))
    def m2(self):
        self.name2 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname1=str(self.textEdit_2.setText(self.name2))
    def m3(self):
        self.name3 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname2=str(self.textEdit_3.setText(self.name3))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class mgw3(QtWidgets.QMainWindow, Ui_mg3win):
    def __init__(self):
        super(mgw3, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_mg3win.__init__(self)
        self.setupUi(self)

    def Reset(self):
        self.label.clear()

    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                                  "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.view)
        else:
            print('Error')

    def merge3(self):
        self.image1 = cv2.imread(self.name1)
        self.image2 = cv2.imread(self.name2)
        self.view = cv2.vconcat([self.image1, self.image2])
        image = QtGui.QImage(self.view, self.view.shape[1], self.view.shape[0], self.view.shape[1] * 3,
                             QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def m1(self):
        self.name1 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname=str(self.textEdit.setText(self.name1))
    def m2(self):
        self.name2 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname1=str(self.textEdit_2.setText(self.name2))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class mgw4(QtWidgets.QMainWindow, Ui_mg4win):
    def __init__(self):
        super(mgw4, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_mg4win.__init__(self)
        self.setupUi(self)

    def Reset(self):
        self.label.clear()

    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                                  "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.view)
        else:
            print('Error')

    def merge4(self):
        self.image1=cv2.imread(self.name1)
        self.image2=cv2.imread(self.name2)
        self.image3 = cv2.imread(self.name3)
        self.image4 = cv2.imread(self.name4)
        self.h1=cv2.hconcat([self.image1, self.image2])
        self.h2=cv2.hconcat([self.image3, self.image4])
        self.view=cv2.vconcat([self.h1,self.h2])
        image = QtGui.QImage(self.view, self.view.shape[1], self.view.shape[0], self.view.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def m1(self):
        self.name1 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname=str(self.textEdit.setText(self.name1))
    def m2(self):
        self.name2 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname1=str(self.textEdit_2.setText(self.name2))
    def m3(self):
        self.name3 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname2=str(self.textEdit_3.setText(self.name3))
    def m4(self):
        self.name4 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname3=str(self.textEdit_4.setText(self.name4))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class mgw5(QtWidgets.QMainWindow, Ui_mg5win):
    def __init__(self):
        super(mgw5, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_mg5win.__init__(self)
        self.setupUi(self)

    def Reset(self):
        self.label.clear()

    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                                  "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.view)
        else:
            print('Error')

    def merge5(self):
        self.image1=cv2.imread(self.name1)
        self.image2=cv2.imread(self.name2)
        self.image3 = cv2.imread(self.name3)
        self.image4 = cv2.imread(self.name4)
        self.image5 = cv2.imread(self.name5)
        self.image6 = cv2.imread(self.name6)
        self.h1=cv2.hconcat([self.image1, self.image2, self.image3])
        self.h2=cv2.hconcat([self.image4, self.image5, self.image6])
        self.view=cv2.vconcat([self.h1,self.h2])
        image = QtGui.QImage(self.view, self.view.shape[1], self.view.shape[0], self.view.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def m1(self):
        self.name1 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname=str(self.textEdit.setText(self.name1))
    def m2(self):
        self.name2 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname1=str(self.textEdit_2.setText(self.name2))
    def m3(self):
        self.name3 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname2=str(self.textEdit_3.setText(self.name3))
    def m4(self):
        self.name4 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname3=str(self.textEdit_4.setText(self.name4))
    def m5(self):
        self.name5 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname4=str(self.textEdit_5.setText(self.name5))
    def m6(self):
        self.name6 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname5=str(self.textEdit_6.setText(self.name6))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class mgw6(QtWidgets.QMainWindow, Ui_mg6win):
    def __init__(self):
        super(mgw6, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_mg6win.__init__(self)
        self.setupUi(self)

    def Reset(self):
        self.label.clear()

    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                                  "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.view)
        else:
            print('Error')

    def merge6(self):
        self.image1=cv2.imread(self.name1)
        self.image2=cv2.imread(self.name2)
        self.image3 = cv2.imread(self.name3)
        self.view=cv2.vconcat([self.image1,self.image2,self.image3])
        image = QtGui.QImage(self.view, self.view.shape[1], self.view.shape[0], self.view.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def m1(self):
        self.name1 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname=str(self.textEdit.setText(self.name1))
    def m2(self):
        self.name2 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname1=str(self.textEdit_2.setText(self.name2))
    def m3(self):
        self.name3 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname2=str(self.textEdit_3.setText(self.name3))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class mgw7(QtWidgets.QMainWindow, Ui_mg7win):
    def __init__(self):
        super(mgw7, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_mg7win.__init__(self)
        self.setupUi(self)

    def Reset(self):
        self.label.clear()

    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                                  "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.view)
        else:
            print('Error')
    def merge7(self):
        self.image1=cv2.imread(self.name1)
        self.image2=cv2.imread(self.name2)
        self.image3 = cv2.imread(self.name3)
        self.image4 = cv2.imread(self.name4)
        self.image5 = cv2.imread(self.name5)
        self.image6 = cv2.imread(self.name6)
        self.h1=cv2.hconcat([self.image1, self.image2])
        self.h2=cv2.hconcat([self.image3, self.image4])
        self.h3 = cv2.hconcat([self.image5, self.image6])
        self.view=cv2.vconcat([self.h1,self.h2, self.h3])
        image = QtGui.QImage(self.view, self.view.shape[1], self.view.shape[0], self.view.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def m1(self):
        self.name1 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname=str(self.textEdit.setText(self.name1))
    def m2(self):
        self.name2 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname1=str(self.textEdit_2.setText(self.name2))
    def m3(self):
        self.name3 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname2=str(self.textEdit_3.setText(self.name3))
    def m4(self):
        self.name4 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname3=str(self.textEdit_4.setText(self.name4))
    def m5(self):
        self.name5 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname4=str(self.textEdit_5.setText(self.name5))
    def m6(self):
        self.name6 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname5=str(self.textEdit_6.setText(self.name6))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class mgw8(QtWidgets.QMainWindow, Ui_mg8win):
    def __init__(self):
        super(mgw8, self).__init__()
        QtGui.QWindow.__init__(self)
        Ui_mg8win.__init__(self)
        self.setupUi(self)

    def Reset(self):
        self.label.clear()

    def Save(self):
        fname, fliter = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', 'C:\\Users\\user\\Desktop\\',
                                                                  "Image Files (*.jpeg);;Image Files (*.bmp);;Image Files (*.tiff)")
        if fname:
            cv2.imwrite(fname, self.view)
        else:
            print('Error')

    def merge8(self):
        self.image1=cv2.imread(self.name1)
        self.image2=cv2.imread(self.name2)
        self.image3 = cv2.imread(self.name3)
        self.image4 = cv2.imread(self.name4)
        self.image5 = cv2.imread(self.name5)
        self.image6 = cv2.imread(self.name6)
        self.image7 = cv2.imread(self.name7)
        self.image8 = cv2.imread(self.name8)
        self.image9 = cv2.imread(self.name9)
        self.h1=cv2.hconcat([self.image1, self.image2, self.image3])
        self.h2=cv2.hconcat([self.image4, self.image5, self.image6])
        self.h3=cv2.hconcat([self.image7, self.image8, self.image9])
        self.view=cv2.vconcat([self.h1,self.h2,self.h3])
        image = QtGui.QImage(self.view, self.view.shape[1], self.view.shape[0], self.view.shape[1] * 3,
                              QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap(image)
        self.pixmap = self.pixmap.scaled(400, 500, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
    def m1(self):
        self.name1 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname=str(self.textEdit.setText(self.name1))
    def m2(self):
        self.name2 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname1=str(self.textEdit_2.setText(self.name2))
    def m3(self):
        self.name3 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname2=str(self.textEdit_3.setText(self.name3))
    def m4(self):
        self.name4 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname3=str(self.textEdit_4.setText(self.name4))
    def m5(self):
        self.name5 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname4=str(self.textEdit_5.setText(self.name5))
    def m6(self):
        self.name6 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname5=str(self.textEdit_6.setText(self.name6))
    def m7(self):
        self.name7 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname6=str(self.textEdit_7.setText(self.name7))
    def m8(self):
        self.name8 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname7=str(self.textEdit_8.setText(self.name8))
    def m9(self):
        self.name9 = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image")[0]
        self.imgname8=str(self.textEdit_9.setText(self.name9))

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)

    window=spw1()
    window.show()
    window1 = spw2()
    window1.show()
    window2 = spw3()
    window2.show()
    window3 = spw4()
    window3.show()
    window4 = spw5()
    window4.show()
    window5 = spw6()
    window5.show()
    window6 = spw7()
    window6.show()
    window7 = spw8()
    window7.show()

    window8=mgw1()
    window8.show()
    window9 = mgw2()
    window9.show()
    window10 = mgw3()
    window10.show()
    window11 = mgw4()
    window11.show()
    window12 = mgw5()
    window12.show()
    window13 = mgw6()
    window13.show()
    window14 = mgw7()
    window14.show()
    window15 = mgw8()
    window15.show()

    sys.exit(app.exec())
