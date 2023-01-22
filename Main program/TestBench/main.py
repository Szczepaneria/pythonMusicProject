# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import faulthandler
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, QTimer
import pyPlayer as playerTools

# init player with playlist
playerTools.searchFiles()
p1 = playerTools.Player(playerTools.InitPlaylist(playerTools.fileList, mode=1))


class Ui_Widget(object):
    def sldDisconnect(self, slider):
        slider.valueChanged.disconnect()

    def sliderChanged(self, slider):
        p1.changePos(slider.value())

    def sldReconnect(self, slider):
        slider.valueChanged.connect(self.sliderChanged)
        slider.valueChanged.emit(slider.value())

    def changeVolume(self, slider):
        p1.pressChangeVolume(slider)

    # def setSound(self):

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setEnabled(True)
        Widget.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QtCore.QSize(800, 500))
        Widget.setMaximumSize(QtCore.QSize(800, 500))
        self.verticalLayoutWidget = QtWidgets.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 473))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionsLayout = QtWidgets.QHBoxLayout()
        self.optionsLayout.setObjectName("optionsLayout")
        self.buttonMode = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonMode.setMinimumSize(QtCore.QSize(70, 70))
        self.buttonMode.setMaximumSize(QtCore.QSize(100, 16777215))
        self.buttonMode.setObjectName("buttonMode")
        self.optionsLayout.addWidget(self.buttonMode)
        spacerItem = QtWidgets.QSpacerItem(600, 90, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.optionsLayout.addItem(spacerItem)
        self.soundSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soundSlider.sizePolicy().hasHeightForWidth())
        self.soundSlider.setSizePolicy(sizePolicy)
        self.soundSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.soundSlider.setMaximumSize(QtCore.QSize(58, 90))
        self.soundSlider.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.soundSlider.setOrientation(QtCore.Qt.Vertical)
        self.soundSlider.setObjectName("soundSlider")
        self.soundSlider.setMinimum(0)
        self.soundSlider.setMaximum(100)
        self.optionsLayout.addWidget(self.soundSlider)
        self.verticalLayout.addLayout(self.optionsLayout)
        self.textDisplayLayout = QtWidgets.QVBoxLayout()
        self.textDisplayLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.textDisplayLayout.setContentsMargins(-1, -1, -1, 0)
        self.textDisplayLayout.setObjectName("textDisplayLayout")
        self.textSongDisplay = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textSongDisplay.setMinimumSize(QtCore.QSize(760, 50))
        self.textSongDisplay.setMaximumSize(QtCore.QSize(760, 150))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.textSongDisplay.setFont(font)
        self.textSongDisplay.setReadOnly(True)
        self.textSongDisplay.setObjectName("textSongDisplay")
        self.textDisplayLayout.addWidget(self.textSongDisplay)
        self.verticalLayout.addLayout(self.textDisplayLayout)
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.buttonsLayout.setContentsMargins(5, 40, 5, 50)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.buttonPrevious = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPrevious.sizePolicy().hasHeightForWidth())
        self.buttonPrevious.setSizePolicy(sizePolicy)
        self.buttonPrevious.setObjectName("buttonPrevious")
        self.buttonPrevious.setIcon(QIcon("left_next.png"))
        self.buttonsLayout.addWidget(self.buttonPrevious)
        self.buttonPlay = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonPlay.setToolTipDuration(0)
        self.buttonPlay.setObjectName("buttonPlay")
        self.buttonsLayout.addWidget(self.buttonPlay)
        self.buttonNext = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonNext.setText("Next")
        self.buttonNext.setCheckable(False)
        self.buttonNext.setIcon(QIcon("right_next.png"))
        self.buttonNext.setObjectName("buttonNext")
        self.buttonsLayout.addWidget(self.buttonNext)
        self.verticalLayout.addLayout(self.buttonsLayout)
        self.sliderSong = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.sliderSong.setMinimum(0)
        self.sliderSong.setMaximum(1000)
        self.sliderSong.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSong.setObjectName("sliderSong")
        self.verticalLayout.addWidget(self.sliderSong)
        self.buttonMode.setDisabled(False)


        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

        self.buttonPlay.clicked.connect(lambda: p1.playPushedPlay(button=self.buttonPlay, display=self.textSongDisplay))
        self.buttonNext.clicked.connect(lambda: p1.playNext(self.textSongDisplay))
        self.buttonPrevious.clicked.connect(lambda: p1.playPrevious(self.textSongDisplay))
        self.soundSlider.valueChanged.connect(lambda: p1.pressChangeVolume(self.soundSlider))

        # self.sliderSong.valueChanged.connect(lambda: self.sliderChanged(self.sliderSong))
        # self.sliderSong.sliderPressed.connect(lambda: self.sldDisconnect(self.sliderSong))
        # self.sliderSong.sliderReleased.connect(lambda: self.sldReconnect(self.sliderSong))

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "PythonPlayer"))
        self.buttonMode.setText(_translate("Widget", "Mode"))
        self.textSongDisplay.setPlaceholderText(_translate("Widget", "<Press 'Play' to play music>"))
        self.buttonPrevious.setText(_translate("Widget", "Previous"))
        self.buttonPlay.setText(_translate("Widget", "Play/Pause"))

    def getDisplay(self):
        return self.textSongDisplay

    def getSlider(self):
        return self.sliderSong


if __name__ == "__main__":
    faulthandler.enable()
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()

    timer = QTimer()
    timer.timeout.connect(lambda: p1.checkUserEvent(Ui_Widget.getDisplay(ui)))
    timer.setInterval(1000)  # 1000ms = 1s
    timer.start()

    timer_slider = QTimer()
    timer_slider.timeout.connect(lambda: p1.sliderUpdate(Ui_Widget.getSlider(ui)))
    timer_slider.setInterval(500)
    timer_slider.start()

    sys.exit(app.exec_())
