# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Object(object):
    def setupUi(self, Object):
        Object.setObjectName("Object")
        Object.resize(1667, 888)
        font = QtGui.QFont()
        font.setPointSize(12)
        Object.setFont(font)
        self.tableWidget = QtWidgets.QTableWidget(parent=Object)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1491, 101))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(1, 8, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.label = QtWidgets.QLabel(parent=Object)
        self.label.setGeometry(QtCore.QRect(1490, 0, 141, 131))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=Object)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 100, 1491, 31))
        self.tableWidget_2.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.label_2 = QtWidgets.QLabel(parent=Object)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_2.setObjectName("label_2")
        self.horizontalScrollBar = QtWidgets.QScrollBar(parent=Object)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 130, 1641, 16))
        self.horizontalScrollBar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_3 = QtWidgets.QLabel(parent=Object)
        self.label_3.setGeometry(QtCore.QRect(770, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Object)
        self.label_4.setGeometry(QtCore.QRect(950, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(parent=Object)
        self.label_11.setGeometry(QtCore.QRect(1380, 170, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_11.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.label_11.setObjectName("label_11")
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=Object)
        self.tableWidget_3.setGeometry(QtCore.QRect(1380, 230, 251, 141))
        self.tableWidget_3.setRowCount(2)
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_3.setItem(1, 1, item)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget_3.verticalHeader().setStretchLastSection(True)
        self.tableWidget_4 = QtWidgets.QTableWidget(parent=Object)
        self.tableWidget_4.setGeometry(QtCore.QRect(1380, 380, 251, 211))
        self.tableWidget_4.setRowCount(5)
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setObjectName("tableWidget_4")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.tableWidget_4.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.tableWidget_4.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_4.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_4.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_4.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_4.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_4.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget_4.setItem(4, 1, item)
        self.tableWidget_4.horizontalHeader().setVisible(False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget_4.verticalHeader().setStretchLastSection(True)
        self.tableWidget_5 = QtWidgets.QTableWidget(parent=Object)
        self.tableWidget_5.setGeometry(QtCore.QRect(1380, 600, 251, 141))
        self.tableWidget_5.setRowCount(2)
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setObjectName("tableWidget_5")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_5.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.tableWidget_5.setItem(1, 0, item)
        self.tableWidget_5.horizontalHeader().setVisible(False)
        self.tableWidget_5.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_5.verticalHeader().setMinimumSectionSize(55)
        self.tableWidget_5.verticalHeader().setStretchLastSection(True)
        self.checkBox = QtWidgets.QCheckBox(parent=Object)
        self.checkBox.setGeometry(QtCore.QRect(1380, 750, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.checkBox.setObjectName("checkBox")
        self.label_12 = QtWidgets.QLabel(parent=Object)
        self.label_12.setGeometry(QtCore.QRect(1380, 780, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_12.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=Object)
        self.label_13.setGeometry(QtCore.QRect(1380, 810, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_13.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.label_13.setObjectName("label_13")
        self.plot_widget = QtWidgets.QWidget(parent=Object)
        self.plot_widget.setGeometry(QtCore.QRect(210, 260, 1101, 551))
        self.plot_widget.setObjectName("plot_widget")
        self.textEdit = QtWidgets.QTextEdit(parent=Object)
        self.textEdit.setGeometry(QtCore.QRect(840, 170, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=Object)
        self.textEdit_2.setGeometry(QtCore.QRect(980, 170, 104, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=Object)
        self.label_5.setGeometry(QtCore.QRect(210, 180, 41, 21))
        self.label_5.setObjectName("label_5")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=Object)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 180, 111, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=Object)
        self.checkBox_3.setGeometry(QtCore.QRect(400, 180, 111, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=Object)
        self.checkBox_4.setGeometry(QtCore.QRect(530, 180, 111, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_6 = QtWidgets.QLabel(parent=Object)
        self.label_6.setGeometry(QtCore.QRect(960, 235, 61, 6))
        self.label_6.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Object)
        self.label_7.setGeometry(QtCore.QRect(910, 230, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Object)
        self.label_8.setGeometry(QtCore.QRect(1050, 225, 101, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Object)
        self.label_9.setGeometry(QtCore.QRect(1160, 235, 61, 6))
        self.label_9.setStyleSheet("background-color:rgb(0, 170, 127)")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_18 = QtWidgets.QLabel(parent=Object)
        self.label_18.setGeometry(QtCore.QRect(1330, 530, 16, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=Object)
        self.label_19.setGeometry(QtCore.QRect(1330, 550, 16, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=Object)
        self.label_20.setGeometry(QtCore.QRect(1330, 570, 16, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=Object)
        self.label_21.setGeometry(QtCore.QRect(1330, 590, 16, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=Object)
        self.label_22.setGeometry(QtCore.QRect(1330, 610, 16, 16))
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(parent=Object)
        self.label_24.setGeometry(QtCore.QRect(1330, 450, 16, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=Object)
        self.label_25.setGeometry(QtCore.QRect(1330, 490, 16, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=Object)
        self.label_26.setGeometry(QtCore.QRect(1330, 430, 16, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=Object)
        self.label_27.setGeometry(QtCore.QRect(1330, 410, 16, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=Object)
        self.label_28.setGeometry(QtCore.QRect(1330, 466, 20, 20))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=Object)
        self.label_29.setGeometry(QtCore.QRect(1330, 510, 16, 16))
        self.label_29.setObjectName("label_29")

        self.retranslateUi(Object)
        QtCore.QMetaObject.connectSlotsByName(Object)

    def retranslateUi(self, Object):
        _translate = QtCore.QCoreApplication.translate
        Object.setWindowTitle(_translate("Object", "Object"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Object", "Tag Node"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Object", "Location"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Object", "Tag Point"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Object", "3 Head No"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Object", "Provision"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Object", "Probe type"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("Object", "3 Records from"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("Object", "By"))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("Object", "Whole range"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Object", "10553-ЕР"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Object", "Wellhead system #10, outfall line of well R-5A"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Object", "10553-EP-12"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Object", "010553"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Object", "12"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("Object", "Gortsevoy small"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("Object", "15-08-2022"))
        item = self.tableWidget.item(1, 7)
        item.setText(_translate("Object", "14-10-2023"))
        item = self.tableWidget.item(1, 8)
        item.setText(_translate("Object", "All"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Object", "TextLabel"))
        self.label_2.setText(_translate("Object", "Commentary"))
        self.label_3.setText(_translate("Object", "  Period"))
        self.label_4.setText(_translate("Object", " To"))
        self.label_11.setText(_translate("Object", "Risk assessment of corrosion rate \n"
"corrosion"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("Object", "Admission to"))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("Object", "+3MM"))
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("Object", "Maximum \n"
"permissible \n"
"rate\n"
"corrosion"))
        item = self.tableWidget_3.item(1, 1)
        item.setText(_translate("Object", "0.120MM/Year"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.item(0, 0)
        item.setText(_translate("Object", "Risk"))
        item = self.tableWidget_4.item(0, 1)
        item.setText(_translate("Object", "Speed  17.295MM/Year"))
        item = self.tableWidget_4.item(1, 0)
        item.setText(_translate("Object", "High"))
        item = self.tableWidget_4.item(1, 1)
        item.setText(_translate("Object", ">0.108"))
        item = self.tableWidget_4.item(2, 0)
        item.setText(_translate("Object", "Moderate"))
        item = self.tableWidget_4.item(2, 1)
        item.setText(_translate("Object", "0.06-0.108"))
        item = self.tableWidget_4.item(3, 0)
        item.setText(_translate("Object", "Low"))
        item = self.tableWidget_4.item(3, 1)
        item.setText(_translate("Object", "0.012-0.06"))
        item = self.tableWidget_4.item(4, 0)
        item.setText(_translate("Object", "Very \n"
"low"))
        item = self.tableWidget_4.item(4, 1)
        item.setText(_translate("Object", "<0.012"))
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        item = self.tableWidget_5.item(0, 0)
        item.setText(_translate("Object", "Replacing the sensing element \n"
"element"))
        item = self.tableWidget_5.item(1, 0)
        item.setText(_translate("Object", "Required"))
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        self.checkBox.setText(_translate("Object", "Cleaning of contaminants!"))
        self.label_12.setText(_translate("Object", "   degreasing"))
        self.label_13.setText(_translate("Object", "   recommended?"))
        self.textEdit.setHtml(_translate("Object", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">03-30-2023</p></body></html>"))
        self.textEdit_2.setHtml(_translate("Object", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">09-15-2023</p></body></html>"))
        self.label_5.setText(_translate("Object", "Serial"))
        self.checkBox_2.setText(_translate("Object", "2019-02298"))
        self.checkBox_3.setText(_translate("Object", "2019-02289"))
        self.checkBox_4.setText(_translate("Object", "2019-02297"))
        self.label_7.setText(_translate("Object", "Thick:"))
        self.label_8.setText(_translate("Object", "Temperature:"))
        self.label_18.setText(_translate("Object", "a"))
        self.label_19.setText(_translate("Object", "t"))
        self.label_20.setText(_translate("Object", "u"))
        self.label_21.setText(_translate("Object", "r"))
        self.label_22.setText(_translate("Object", "e"))
        self.label_24.setText(_translate("Object", "m"))
        self.label_25.setText(_translate("Object", "e"))
        self.label_26.setText(_translate("Object", "e"))
        self.label_27.setText(_translate("Object", "T"))
        self.label_28.setText(_translate("Object", "p"))
        self.label_29.setText(_translate("Object", "r"))
