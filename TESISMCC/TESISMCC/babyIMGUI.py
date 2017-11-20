import sys
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(400,200)
    w.move(600,300)
    w.setWindowTitle('BabyIM')
    w.show()

    app.exec_()

if __name__ == '__main__' :
    main()


