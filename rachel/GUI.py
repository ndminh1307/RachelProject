import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt

from subprocess import Popen, PIPE


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Rachel Application"
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(800,600)

        converseButton = QPushButton("Converse to Rachel", self)
        converseButton.setToolTip("Converse to Rachel now")
        converseButton.resize(200,50)
        converseButton.move(200, 10)
        converseButton.clicked.connect(self.converse)
        
        #Label output
        self.lbl = QLabel(self)
        self.lbl.move(50,200)
        self.lbl.resize(600,400)
        self.lbl.setWordWrap(True)
        self.lbl.setAlignment(Qt.AlignTop)

        self.show()

    @pyqtSlot()
    def converse(self):
        def run(command):
            process = Popen(command, stdout=PIPE, shell=True)
            while True:
                line = process.stdout.readline().rstrip()
                if not line:
                    break
                yield line
        
        for output in run("python3 -m main"):
            self.lbl.setText(self.lbl.text() + "\n" + output.decode("utf-8"))
        
if __name__ =='__main__':
    app =QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
