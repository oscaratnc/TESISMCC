import sys
from PyQt4 import QtGui

class babyIMGUI (QtGui.QWidget):
    def __init__(self):
        super(babyIMGUI, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(500,500,500,500)
        self.setWindowTitle('New GUI')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    w = babyIMGUI()
    app.exec_()

if __name__ == '__main__' :
    main()


