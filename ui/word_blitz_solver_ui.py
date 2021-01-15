# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'word_blitz_solver_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(272, 198)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lie_00 = QLineEdit(self.centralwidget)
        self.lie_00.setObjectName(u"lie_00")
        self.lie_00.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lie_00)

        self.lie_01 = QLineEdit(self.centralwidget)
        self.lie_01.setObjectName(u"lie_01")
        self.lie_01.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lie_01)

        self.lie_02 = QLineEdit(self.centralwidget)
        self.lie_02.setObjectName(u"lie_02")
        self.lie_02.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lie_02)

        self.lie_03 = QLineEdit(self.centralwidget)
        self.lie_03.setObjectName(u"lie_03")
        self.lie_03.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lie_03)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lie_04 = QLineEdit(self.centralwidget)
        self.lie_04.setObjectName(u"lie_04")
        self.lie_04.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lie_04)

        self.lie_05 = QLineEdit(self.centralwidget)
        self.lie_05.setObjectName(u"lie_05")
        self.lie_05.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lie_05)

        self.lie_06 = QLineEdit(self.centralwidget)
        self.lie_06.setObjectName(u"lie_06")
        self.lie_06.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lie_06)

        self.lie_07 = QLineEdit(self.centralwidget)
        self.lie_07.setObjectName(u"lie_07")
        self.lie_07.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lie_07)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lie_08 = QLineEdit(self.centralwidget)
        self.lie_08.setObjectName(u"lie_08")
        self.lie_08.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lie_08)

        self.lie_09 = QLineEdit(self.centralwidget)
        self.lie_09.setObjectName(u"lie_09")
        self.lie_09.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lie_09)

        self.lie_10 = QLineEdit(self.centralwidget)
        self.lie_10.setObjectName(u"lie_10")
        self.lie_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lie_10)

        self.lie_11 = QLineEdit(self.centralwidget)
        self.lie_11.setObjectName(u"lie_11")
        self.lie_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lie_11)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lie_12 = QLineEdit(self.centralwidget)
        self.lie_12.setObjectName(u"lie_12")
        self.lie_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lie_12)

        self.lie_13 = QLineEdit(self.centralwidget)
        self.lie_13.setObjectName(u"lie_13")
        self.lie_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lie_13)

        self.lie_14 = QLineEdit(self.centralwidget)
        self.lie_14.setObjectName(u"lie_14")
        self.lie_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lie_14)

        self.lie_15 = QLineEdit(self.centralwidget)
        self.lie_15.setObjectName(u"lie_15")
        self.lie_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lie_15)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.pub_analyse = QPushButton(self.centralwidget)
        self.pub_analyse.setObjectName(u"pub_analyse")

        self.horizontalLayout_5.addWidget(self.pub_analyse)

        self.pub_solve = QPushButton(self.centralwidget)
        self.pub_solve.setObjectName(u"pub_solve")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pub_solve.sizePolicy().hasHeightForWidth()
        )
        self.pub_solve.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.pub_solve)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 272, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Solver", None)
        )
        self.lie_00.setText("")
        self.pub_analyse.setText(
            QCoreApplication.translate("MainWindow", u"Analyse", None)
        )
        self.pub_solve.setText(
            QCoreApplication.translate("MainWindow", u"Solve", None)
        )

    # retranslateUi
