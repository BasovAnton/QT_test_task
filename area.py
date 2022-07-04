# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'area.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(700, 1000)
        Form.setMinimumSize(QSize(700, 1000))
        Form.setMaximumSize(QSize(700, 1000))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        Form.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QSize(400, 100))
        self.pushButton_start.setMaximumSize(QSize(500, 200))

        self.horizontalLayout.addWidget(self.pushButton_start)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(300, 25))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QSize(0, 0))
        self.lcdNumber.setMaximumSize(QSize(300, 75))

        self.verticalLayout_3.addWidget(self.lcdNumber)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hl0 = QHBoxLayout()
        self.hl0.setObjectName(u"hl0")
        self.le00 = QLineEdit(Form)
        self.le00.setObjectName(u"le00")
        self.le00.setMinimumSize(QSize(150, 150))
        self.le00.setMaximumSize(QSize(150, 150))
        font2 = QFont()
        font2.setPointSize(30)
        font2.setStyleStrategy(QFont.NoAntialias)
        self.le00.setFont(font2)
        self.le00.setCursor(QCursor(Qt.SizeVerCursor))
        self.le00.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le00.setAlignment(Qt.AlignCenter)
        self.le00.setReadOnly(True)

        self.hl0.addWidget(self.le00)

        self.le01 = QLineEdit(Form)
        self.le01.setObjectName(u"le01")
        self.le01.setMinimumSize(QSize(150, 150))
        self.le01.setMaximumSize(QSize(150, 150))
        self.le01.setFont(font2)
        self.le01.setCursor(QCursor(Qt.SizeVerCursor))
        self.le01.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le01.setAlignment(Qt.AlignCenter)
        self.le01.setReadOnly(True)

        self.hl0.addWidget(self.le01)

        self.le02 = QLineEdit(Form)
        self.le02.setObjectName(u"le02")
        self.le02.setMinimumSize(QSize(150, 150))
        self.le02.setMaximumSize(QSize(150, 150))
        self.le02.setFont(font2)
        self.le02.setCursor(QCursor(Qt.SizeVerCursor))
        self.le02.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le02.setAlignment(Qt.AlignCenter)
        self.le02.setReadOnly(True)

        self.hl0.addWidget(self.le02)

        self.le03 = QLineEdit(Form)
        self.le03.setObjectName(u"le03")
        self.le03.setMinimumSize(QSize(150, 150))
        self.le03.setMaximumSize(QSize(150, 150))
        self.le03.setFont(font2)
        self.le03.setCursor(QCursor(Qt.SizeVerCursor))
        self.le03.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le03.setAlignment(Qt.AlignCenter)
        self.le03.setReadOnly(True)

        self.hl0.addWidget(self.le03)


        self.verticalLayout.addLayout(self.hl0)

        self.hl1 = QHBoxLayout()
        self.hl1.setObjectName(u"hl1")
        self.le10 = QLineEdit(Form)
        self.le10.setObjectName(u"le10")
        self.le10.setMinimumSize(QSize(150, 150))
        self.le10.setMaximumSize(QSize(150, 150))
        self.le10.setFont(font2)
        self.le10.setCursor(QCursor(Qt.SizeVerCursor))
        self.le10.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le10.setAlignment(Qt.AlignCenter)
        self.le10.setReadOnly(True)

        self.hl1.addWidget(self.le10)

        self.le11 = QLineEdit(Form)
        self.le11.setObjectName(u"le11")
        self.le11.setMinimumSize(QSize(150, 150))
        self.le11.setMaximumSize(QSize(150, 150))
        self.le11.setFont(font2)
        self.le11.setCursor(QCursor(Qt.SizeVerCursor))
        self.le11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le11.setAlignment(Qt.AlignCenter)
        self.le11.setReadOnly(True)

        self.hl1.addWidget(self.le11)

        self.le12 = QLineEdit(Form)
        self.le12.setObjectName(u"le12")
        self.le12.setMinimumSize(QSize(150, 150))
        self.le12.setMaximumSize(QSize(150, 150))
        self.le12.setFont(font2)
        self.le12.setCursor(QCursor(Qt.SizeVerCursor))
        self.le12.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le12.setAlignment(Qt.AlignCenter)
        self.le12.setReadOnly(True)

        self.hl1.addWidget(self.le12)

        self.le13 = QLineEdit(Form)
        self.le13.setObjectName(u"le13")
        self.le13.setMinimumSize(QSize(150, 150))
        self.le13.setMaximumSize(QSize(150, 150))
        self.le13.setFont(font2)
        self.le13.setCursor(QCursor(Qt.SizeVerCursor))
        self.le13.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le13.setAlignment(Qt.AlignCenter)
        self.le13.setReadOnly(True)

        self.hl1.addWidget(self.le13)


        self.verticalLayout.addLayout(self.hl1)

        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.le20 = QLineEdit(Form)
        self.le20.setObjectName(u"le20")
        self.le20.setMinimumSize(QSize(150, 150))
        self.le20.setMaximumSize(QSize(150, 150))
        self.le20.setFont(font2)
        self.le20.setCursor(QCursor(Qt.SizeVerCursor))
        self.le20.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le20.setAlignment(Qt.AlignCenter)
        self.le20.setReadOnly(True)

        self.hl2.addWidget(self.le20)

        self.le21 = QLineEdit(Form)
        self.le21.setObjectName(u"le21")
        self.le21.setMinimumSize(QSize(150, 150))
        self.le21.setMaximumSize(QSize(150, 150))
        self.le21.setFont(font2)
        self.le21.setCursor(QCursor(Qt.SizeVerCursor))
        self.le21.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le21.setAlignment(Qt.AlignCenter)
        self.le21.setReadOnly(True)

        self.hl2.addWidget(self.le21)

        self.le22 = QLineEdit(Form)
        self.le22.setObjectName(u"le22")
        self.le22.setMinimumSize(QSize(150, 150))
        self.le22.setMaximumSize(QSize(150, 150))
        self.le22.setFont(font2)
        self.le22.setCursor(QCursor(Qt.SizeVerCursor))
        self.le22.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le22.setAlignment(Qt.AlignCenter)
        self.le22.setReadOnly(True)

        self.hl2.addWidget(self.le22)

        self.le23 = QLineEdit(Form)
        self.le23.setObjectName(u"le23")
        self.le23.setMinimumSize(QSize(150, 150))
        self.le23.setMaximumSize(QSize(150, 150))
        self.le23.setFont(font2)
        self.le23.setCursor(QCursor(Qt.SizeVerCursor))
        self.le23.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le23.setAlignment(Qt.AlignCenter)
        self.le23.setReadOnly(True)

        self.hl2.addWidget(self.le23)


        self.verticalLayout.addLayout(self.hl2)

        self.hl3 = QHBoxLayout()
        self.hl3.setObjectName(u"hl3")
        self.le30 = QLineEdit(Form)
        self.le30.setObjectName(u"le30")
        self.le30.setMinimumSize(QSize(150, 150))
        self.le30.setMaximumSize(QSize(150, 150))
        self.le30.setFont(font2)
        self.le30.setCursor(QCursor(Qt.SizeVerCursor))
        self.le30.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le30.setAlignment(Qt.AlignCenter)
        self.le30.setReadOnly(True)

        self.hl3.addWidget(self.le30)

        self.le31 = QLineEdit(Form)
        self.le31.setObjectName(u"le31")
        self.le31.setMinimumSize(QSize(150, 150))
        self.le31.setMaximumSize(QSize(150, 150))
        self.le31.setFont(font2)
        self.le31.setCursor(QCursor(Qt.SizeVerCursor))
        self.le31.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le31.setAlignment(Qt.AlignCenter)
        self.le31.setReadOnly(True)

        self.hl3.addWidget(self.le31)

        self.le32 = QLineEdit(Form)
        self.le32.setObjectName(u"le32")
        self.le32.setMinimumSize(QSize(150, 150))
        self.le32.setMaximumSize(QSize(150, 150))
        self.le32.setFont(font2)
        self.le32.setCursor(QCursor(Qt.SizeVerCursor))
        self.le32.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le32.setAlignment(Qt.AlignCenter)
        self.le32.setReadOnly(True)

        self.hl3.addWidget(self.le32)

        self.le33 = QLineEdit(Form)
        self.le33.setObjectName(u"le33")
        self.le33.setMinimumSize(QSize(150, 150))
        self.le33.setMaximumSize(QSize(150, 150))
        self.le33.setFont(font2)
        self.le33.setCursor(QCursor(Qt.SizeVerCursor))
        self.le33.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.le33.setAlignment(Qt.AlignCenter)
        self.le33.setReadOnly(True)

        self.hl3.addWidget(self.le33)


        self.verticalLayout.addLayout(self.hl3)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_left = QPushButton(Form)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setMinimumSize(QSize(150, 200))

        self.horizontalLayout_2.addWidget(self.pushButton_left)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_up = QPushButton(Form)
        self.pushButton_up.setObjectName(u"pushButton_up")
        self.pushButton_up.setMinimumSize(QSize(150, 100))

        self.verticalLayout_2.addWidget(self.pushButton_up)

        self.pushButton_down = QPushButton(Form)
        self.pushButton_down.setObjectName(u"pushButton_down")
        self.pushButton_down.setMinimumSize(QSize(150, 100))

        self.verticalLayout_2.addWidget(self.pushButton_down)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.pushButton_right = QPushButton(Form)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setMinimumSize(QSize(150, 200))

        self.horizontalLayout_2.addWidget(self.pushButton_right)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"2048", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e:", None))
        self.le00.setText(QCoreApplication.translate("Form", u"0", None))
        self.le01.setText(QCoreApplication.translate("Form", u"0", None))
        self.le02.setText(QCoreApplication.translate("Form", u"0", None))
        self.le03.setText(QCoreApplication.translate("Form", u"0", None))
        self.le10.setText(QCoreApplication.translate("Form", u"0", None))
        self.le11.setText(QCoreApplication.translate("Form", u"0", None))
        self.le12.setText(QCoreApplication.translate("Form", u"0", None))
        self.le13.setText(QCoreApplication.translate("Form", u"0", None))
        self.le20.setText(QCoreApplication.translate("Form", u"0", None))
        self.le21.setText(QCoreApplication.translate("Form", u"0", None))
        self.le22.setText(QCoreApplication.translate("Form", u"0", None))
        self.le23.setText(QCoreApplication.translate("Form", u"0", None))
        self.le30.setText(QCoreApplication.translate("Form", u"0", None))
        self.le31.setText(QCoreApplication.translate("Form", u"0", None))
        self.le32.setText(QCoreApplication.translate("Form", u"0", None))
        self.le33.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_left.setText(QCoreApplication.translate("Form", u"\u0412\u043b\u0435\u0432\u043e", None))
        self.pushButton_up.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.pushButton_down.setText(QCoreApplication.translate("Form", u"\u0412\u043d\u0438\u0437", None))
        self.pushButton_right.setText(QCoreApplication.translate("Form", u"\u0412\u043f\u0440\u0430\u0432\u043e", None))
    # retranslateUi

