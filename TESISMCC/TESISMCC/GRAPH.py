from PyQt4 import QtGui
import matplotlib.pyplot as plt
import TESISMCC
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg  as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


class plotWidget:
    Spo2= TESISMCC.spo2Sensor()
    Spo2.dataAcquisition(20)
           
    def __init__(self):
        Red= TESISMCC.Red
        IR = TESISMCC.IR
        super(plotWidget, self).__init__()
        self.initUI(Red,IR)

    def initUI(self,Red,IR):
        self.setGeometry(600,300,1000,600)
        self.center()
        self.setWindowTitle('Plotting window')

        grid = QtGui.QGridLayout()
        self.setLayout(grid)
       
        btn1 = QtGui.QPushButton('Plot Red', self)
        btn1.resize(btn1.sizeHint()) 
        btn1.clicked.connect(self.plotRed(Red))
        grid.addWidget(btn1, 2,0)

        btn2 = QtGui.QPushButton('Plot IR', self)
        btn2.resize(btn2.sizeHint())    
        btn2.clicked.connect(self.plotIR(IR))
        grid.addWidget(btn2, 2,1)
               
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)     
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 1,0,1,2)
        grid.addWidget(self.toolbar, 0,0,1,2)
               
        self.show()

        def plotRed(self,Red):
            red = Red
            plt.cla()
            ax= self.figure.add_subplot(111)
            x= [i for i in range(len(red))]
            y= red
            ax.plot(x,y,'r.-')
            ax.setTitle('HR MODE')
            self.canvas.draw()

        def plotIR(self,iR):
            IR = iR
            plt.cla()
            ax= self.figure.add_subplot(111)
            x= [i for i in range(len(IR))]
            y= IR
            ax.plot(x,y,'r.-')
            ax.setTitle('SPO2 MODE')
            self.canvas.draw()

        def center(self):
            qr = self.frameGeometry()
            cp = QtGui.QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
def main():
    spo2= TESISMCC.Sp
    
    app = QtGui.QApplication(sys.argv)
    w= plotWidget()
    app.exec_()

if __name__ == '__main__':
        main()

