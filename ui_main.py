# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):

        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(993, 692)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setMargin(10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.label_3 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.frame_4)
        self.label_4.setEnabled(True)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSite = QtGui.QPushButton(self.frame_4)
        self.btnSite.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.btnSite.setCheckable(False)
        self.btnSite.setFlat(True)
        self.btnSite.setObjectName(_fromUtf8("btnSite"))

        self.horizontalLayout.addWidget(self.btnSite)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))

        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        self.lblDevice = QtGui.QLabel(self.frame_5)
        self.lblDevice.setEnabled(False)
        self.lblDevice.setObjectName(_fromUtf8("lblDevice"))

        self.horizontalLayout_3.addWidget(self.lblDevice)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.chkInvert = QtGui.QCheckBox(self.frame_2)
        self.chkInvert.setObjectName(_fromUtf8("chkInvert"))

        self.horizontalLayout_2.addWidget(self.chkInvert)
        self.chkAutoscale = QtGui.QCheckBox(self.frame_2)
        self.chkAutoscale.setChecked(True)
        self.chkAutoscale.setObjectName(_fromUtf8("chkAutoscale"))

        self.horizontalLayout_2.addWidget(self.chkAutoscale)
        self.line = QtGui.QFrame(self.frame_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.horizontalLayout_2.addWidget(self.line)
        self.label_2 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())

        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinLowpass = QtGui.QSpinBox(self.frame_2)
        self.spinLowpass.setPrefix(_fromUtf8(""))
        self.spinLowpass.setMinimum(0)
        self.spinLowpass.setMaximum(999999)
        self.spinLowpass.setSingleStep(1)
        self.spinLowpass.setProperty("value", 35)
        self.spinLowpass.setObjectName(_fromUtf8("spinLowpass"))

        self.horizontalLayout_2.addWidget(self.spinLowpass)
        self.label_5 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())

        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineTitle = QtGui.QLineEdit(self.frame_2)
        self.lineTitle.setObjectName(_fromUtf8("lineTitle"))

        self.horizontalLayout_2.addWidget(self.lineTitle)
        self.line_2 = QtGui.QFrame(self.frame_2)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.horizontalLayout_2.addWidget(self.line_2)
        self.btnPause = QtGui.QPushButton(self.frame_2)
        self.btnPause.setCheckable(True)
        self.btnPause.setObjectName(_fromUtf8("btnPause"))

        self.horizontalLayout_2.addWidget(self.btnPause)
        self.btnSave = QtGui.QPushButton(self.frame_2)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))

        self.horizontalLayout_2.addWidget(self.btnSave)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))

        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))

        self.grECG = PlotWidget(self.frame_3)
        self.grECG.setFrameShape(QtGui.QFrame.NoFrame)
        self.grECG.setFrameShadow(QtGui.QFrame.Plain)
        self.grECG.setLineWidth(0)
        self.grECG.setObjectName(_fromUtf8("grECG"))

        self.verticalLayout_3.addWidget(self.grECG)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "diyECG", None))
        self.lblDevice.setText(_translate("MainWindow", "!!! ERROR !!! no valid input sound devices found. Plug in a microphone and restart this program!", None))
        self.chkInvert.setText(_translate("MainWindow", "invert", None))
        self.chkAutoscale.setText(_translate("MainWindow", "autoscale", None))
        self.label_2.setText(_translate("MainWindow", "lowpass:", None))
        self.spinLowpass.setToolTip(_translate("MainWindow", "set to 0 to disable", None))
        self.spinLowpass.setSuffix(_translate("MainWindow", " Hz", None))
        self.label_5.setText(_translate("MainWindow", "title:", None))
        self.btnPause.setText(_translate("MainWindow", "Pause", None))
        self.btnSave.setText(_translate("MainWindow", "Save Figure", None))

from pyqtgraph import PlotWidget
