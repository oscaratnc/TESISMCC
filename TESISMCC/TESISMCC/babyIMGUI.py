import Sensor as Sensors
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

numSecondsECG=.5
numSecondsSpO2=10
sampleRate = 400

Sensors.getECG(Sensors,numSecondsECG)
print "ECG done"
Sensors.getSpo2(Sensors,numSecondsSpO2)
print "SPO2 done"
ECG = Sensors.ecgValues
RED = Sensors.Red
IR = Sensors.IR
#PPG = RED/IR
#print ECG
#print RED
#print IR

IRFile = open("IRfile.txt", 'w')
IRFile.write("Red:\n ")
for i in range(RED.shape[0]):
    
    valueRed = str(RED[i])
    IRFile.write(valueRed)

IRFile.write("IR: ")
for i in range(IR.shape[0]):
   
    valueIR = str(IR[i])
    IRFile.write(valueIR)
    
IRFile.close


app = QtGui.QApplication([])

win = pg.GraphicsWindow()
win.resize(1000,1000)
win.setWindowTitle("Signals Ploting")

pg.setConfigOptions(antialias= True)

p1 = win.addPlot(title="ECG")
p1.plot(ECG, pen=(255,0,0))

win.nextRow()
p2 = win.addPlot(title = "RED LED")
p2.plot(RED, pen=(0,255,0))

#win.nextRow()
#p3= win.addPlot(title = "IR LED")
p2.plot(IR, pen=(0,0,255))

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()