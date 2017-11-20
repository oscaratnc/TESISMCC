import sys
from PyQt4 import QtGui, QtCore

class  Window (QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PyQt tuts!")
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        self.show()

    def close_application():
        print("WHOOOOAAAA HARDCORE!!")
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()

