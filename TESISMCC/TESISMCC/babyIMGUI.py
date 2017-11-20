import sys
from PyQt4 import QtGui

class babyIMGUI (QtGui.QWidget):
    def __init__(self):
        super(babyIMGUI, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(500,500,500,500)
        self.setWindowTitle('New GUI')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)

        btn1 = QtGui.QPushButton('Button 1', self)
        btn1.resize(btn1.sizeHint())
        hbox.addWidget(btn1)

        btn2 = QtGui.QPushButton('Button 2', self)
        btn2.resize(btn2.sizeHint())
        hbox.addWidget(btn2)
             
        self.setLayout(hbox)
        self.show()
   
def main():
    app = QtGui.QApplication(sys.argv)
    w = babyIMGUI()
    app.exec_()

if __name__ == '__main__' :
    main()


