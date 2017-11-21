
from Sensor import acquireData
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

sensor = Sensor()
sensor.acquireData(sensor, 50)
ECG = sensors.ecgValues
RED = sensors.Red
IR = sensors.IR
print ECG
print RED
print IR

app = QtGui.QApplication([])

win = pg.GraphicsWindow()
win.resize(1000,600)
win.setWindowTitle("Signals Ploting")

pg.setConfigOptions(antialias= True)

p2 = win.addPlot(title="Vital Curves")
p2.plot(ECG, pen=(255,0,0), name="ECG")
p2.plot(RED, pen=(0,255,0), name="HR led")
p2.plot(IR, pen=(0,0,255), name="IR led")
