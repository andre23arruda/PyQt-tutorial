from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('QT5Agg')
from matplotlib.figure import Figure
import time

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(995, 767)
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(False)
        self.comecar_button = QtWidgets.QPushButton(Dialog)
        self.comecar_button.setGeometry(QtCore.QRect(240, 670, 151, 61))
        self.comecar_button.setObjectName("comecar_button")
        self.fire_slider = QtWidgets.QSlider(Dialog)
        self.fire_slider.setGeometry(QtCore.QRect(80, 620, 831, 20))
        self.fire_slider.setMinimum(15)
        self.fire_slider.setMaximum(100)
        self.fire_slider.setPageStep(20)
        self.fire_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fire_slider.setObjectName("fire_slider")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 911, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")
        self.parar_button = QtWidgets.QPushButton(Dialog)
        self.parar_button.setGeometry(QtCore.QRect(610, 670, 151, 61))
        self.parar_button.setObjectName("parar_button")

        self.decay_factor = 1.5
        self.stop = 0
        self.fire = np.zeros([70, 100],dtype = 'uint8')

        self.img_canvas = FigureCanvas(Figure())
        self.layout.addWidget(self.img_canvas)
        self.img_ax = self.img_canvas.figure.subplots()
        self.img_ax.imshow(self.fire, cmap = 'hot', vmin = 0, vmax = 36, aspect = 'auto')
        self.img_ax.axis('off')

        self.timer = self.img_canvas.new_timer(100, [(self.createFire, (), {})])

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Fire_Doom"))
        self.comecar_button.setText(_translate("Dialog", "Começar"))
        self.parar_button.setText(_translate("Dialog", "Parar"))
        self.fire_slider.valueChanged.connect(self.getSlider)
        self.comecar_button.clicked.connect(self.startFire)
        self.parar_button.clicked.connect(self.stopFire)

    def startFire(self):
        self.timer.start()

    def createFire(self):
        heigth = 70
        width = 100
        self.fire[heigth-1, :] = 36    

        for row in range(heigth - 1):
            for col in range(width):
                decay_factor = self.decay_factor
                decay = np.int_(np.floor(np.random.rand() * decay_factor))
                self.fire[heigth - 2 - row, col - decay] = np.clip(self.fire[heigth - 1 - row, col] - decay , 0, 36)
        self.img_ax.clear()        
        self.img_ax.imshow(self.fire, cmap = 'hot', vmin = 0, vmax = 36, aspect = 'auto')
        self.img_ax.axis('off')
        self.img_ax.figure.canvas.draw()
        print('Deu bom')
        
    def getSlider(self):
        self.decay_factor = 11.5 - self.fire_slider.value()/10
        print(self.decay_factor)

    def stopFire(self):
        self.stop = 1
        self.timer.stop()

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

