import Sensor as Sensors
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

numSecondsECG=3 
numSecondsSpO2=5

Sensors.getECG(Sensors,numSecondsECG)
print "ECG done"
Sensors.getSpo2(Sensors,numSecondsSpO2)
print "SPO2 done"
ECG = Sensors.ecgValues
RED = Sensors.Red
IR = Sensors.IR
print ECG
print RED
print IR

app = QtGui.QApplication([])

win = pg.GraphicsWindow()
win.resize(1000,600)
win.setWindowTitle("Signals Ploting")

pg.setConfigOptions(antialias= True)

p1 = win.addPlot(title="ECG")
p1.plot(ECG, pen=(255,0,0))

win.nextRow()
p2 = win.addPlot(title = "RED LED")
p2.plot(RED, pen=(0,255,0))

win.nextRow()
p3= win.addPlot(title = "IR LED")
p3.plot(IR, pen=(0,0,255))

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()