# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys

import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from dashboard import Ui_Object
from PyQt6.QtGui import QPainter, QColor, QPen
import pyqtgraph as pg
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Object()
        self.ui.setupUi(self)
        self.label = QLabel(self)
        pixmap = QPixmap("image.png")
        self.label.move(1490, 0)
        new_width = 141
        new_height = 131
        resized_pixmap = pixmap.scaled(new_width, new_height)
        self.label.setPixmap(resized_pixmap)
        self.label1 = QLabel("20", parent=window)
        self.label1.move(1330,755)
        self.label2 = QLabel("60", parent=window)
        self.label2.move(1330, 265)

        self.plot_item1 = None
        self.plot_item2 = None

        layout = QVBoxLayout()
        pg.setConfigOption('background', 'w')
        self.graph = pg.PlotWidget()
        x_axis = pg.AxisItem(orientation='bottom')
        y_axis = pg.AxisItem(orientation='left')
        z_axis = pg.AxisItem(orientation='right')
        x_axis.setLabel(text='Time')
        y_axis.setLabel(text='Thick, MM')
        self.graph.setAxisItems({'bottom':x_axis, 'left':y_axis})
        self.graph.showGrid(x=True, y=True)
        layout.addWidget(self.graph)
        self.ui.plot_widget.setLayout(layout)
        self.ui.checkBox_2.stateChanged.connect(self.update_graph2)
        self.ui.checkBox_3.stateChanged.connect(self.update_graph3)
        self.ui.checkBox_4.stateChanged.connect(self.update_graph4)

    def update_graph2(self):
        state = self.ui.checkBox_2.isChecked()
        df = pd.read_csv('A.csv')
        if(state):
            layout = QVBoxLayout()
            if self.plot_item2 is not None:
                self.graph.removeItem(self.plot_item2)
            thick = df.iloc[0:210, 5]
            temp = df.iloc[0:210, 7]/101+7.5
            if self.plot_item1 is not None:
                self.graph.removeItem(self.plot_item1)
            self.plot_item1=self.graph.plot(thick, pen='r')
            layout.addWidget(self.graph)
            self.plot_item2=self.graph.plot(temp, pen='g')
            layout.addWidget(self.graph)
            self.ui.checkBox_3.setChecked(False)
            self.ui.checkBox_3.setEnabled(False)
            self.ui.checkBox_4.setChecked(False)
            self.ui.checkBox_4.setEnabled(False)
            self.ui.plot_widget.setLayout(layout)
        else:
            if self.plot_item1 is not None:
                self.graph.removeItem(self.plot_item1)
            if self.plot_item2 is not None:
                self.graph.removeItem(self.plot_item2)
            self.ui.checkBox_3.setChecked(False)
            self.ui.checkBox_3.setEnabled(True)
            self.ui.checkBox_4.setChecked(False)
            self.ui.checkBox_4.setEnabled(True)

    def update_graph3(self):
        state = self.ui.checkBox_3.isChecked()
        df = pd.read_csv('A.csv')
        if(state):
            layout = QVBoxLayout()
            if self.plot_item2 is not None:
                self.graph.removeItem(self.plot_item2)
            thick = pd.concat([df.iloc[0:120, 9], df.iloc[211:340,9]])
            temp = pd.concat([df.iloc[0:120, 11], df.iloc[211:340, 11]])/101+7.8
            if self.plot_item1 is not None:
                self.graph.removeItem(self.plot_item1)
            self.plot_item1=self.graph.plot(thick, pen='r')
            layout.addWidget(self.graph)
            self.plot_item2=self.graph.plot(temp, pen='g')
            layout.addWidget(self.graph)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_2.setEnabled(False)
            self.ui.checkBox_4.setChecked(False)
            self.ui.checkBox_4.setEnabled(False)
            self.ui.plot_widget.setLayout(layout)
        else:
            if self.plot_item1 is not None:
                self.graph.removeItem(self.plot_item1)
            if self.plot_item2 is not None:
                self.graph.removeItem(self.plot_item2)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_2.setEnabled(True)
            self.ui.checkBox_4.setChecked(False)
            self.ui.checkBox_4.setEnabled(True)

    def update_graph4(self):
        state = self.ui.checkBox_4.isChecked()
        df = pd.read_csv('A.csv')
        if(state):
            layout = QVBoxLayout()
            layout1 = QVBoxLayout()
            if self.plot_item2 is not None:
                self.graph.removeItem(self.plot_item2)
            thick = pd.concat([df.iloc[0:120, 13], df.iloc[341:430,13]])
            temp = pd.concat([df.iloc[0:120, 15], df.iloc[341:430, 15]])/101+7.5
            if self.plot_item1 is not None:
                self.graph.removeItem(self.plot_item1)
            self.plot_item1=self.graph.plot(thick, pen='r')
            layout.addWidget(self.graph)
            self.plot_item2=self.graph.plot(temp, pen='g')
            layout1.addWidget(self.graph)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_2.setEnabled(False)
            self.ui.checkBox_3.setChecked(False)
            self.ui.checkBox_3.setEnabled(False)
            self.ui.plot_widget.setLayout(layout)
        else:
            if self.plot_item1 is not None:
                self.graph.removeItem(self.plot_item1)
            if self.plot_item2 is not None:
                self.graph.removeItem(self.plot_item2)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_2.setEnabled(True)
            self.ui.checkBox_3.setChecked(False)
            self.ui.checkBox_3.setEnabled(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(0, 0, 0), 1))  # Set pen color and width
        painter.drawLine(1310, 270, 1310, 760)
        painter.drawLine(1310, 270, 1320, 270)
        painter.drawLine(1310, 319, 1320, 319)
        painter.drawLine(1310, 368, 1320, 368)
        painter.drawLine(1310, 417, 1320, 417)
        painter.drawLine(1310, 466, 1320, 466)
        painter.drawLine(1310, 515, 1320, 515)
        painter.drawLine(1310, 564, 1320, 564)
        painter.drawLine(1310, 613, 1320, 613)
        painter.drawLine(1310, 662, 1320, 662)
        painter.drawLine(1310, 711, 1320, 711)
        painter.drawLine(1310, 760, 1320, 760)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setFixedSize(1667, 888)
    dashboard = Dashboard()
    layout = QVBoxLayout()
    layout.addWidget(dashboard)
    widget = QWidget()
    widget.setLayout(layout)
    window.setCentralWidget(widget)
    window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
