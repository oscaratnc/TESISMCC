import MAX3010X as MAX30102
from smbus2 import SMBus
import GRAPH

import RPi.GPIO as GPIO
import ptvsd

ptvsd.enable_attach(secret = 'my-secret')
#10.206.251.180

GPIO.setmode(GPIO.BCM)
max102 = MAX30102.MAX30102.max102
GPIO.setup(4, GPIO.IN)
int_status = GPIO.input(4)
i = 0
Red = []
IR = []

print "interrupt status", int_status
i = 0
samplesTaken = 0
Spo2Sensor = MAX30102.MAX30102()
Spo2Sensor.begintest(Spo2Sensor.MAX30102_PARTID, Spo2Sensor.MAX30102_EXPECTED_PARTID)
Spo2Sensor.setup(31, 4, 2, 100, 411, 4096)
lastCorrectRed = 0
redTemp= 0
i=0
while i in range (300):
    
    reD = Spo2Sensor.getRed()
    iR  = Spo2Sensor.getIR()
    print "R: ",reD , "IR: ", iR
    Red.append(reD)
    IR.append(iR)

    i+=1

print "RED data: ", Red
print "IR data ", IR

GRAPH.plot(Red)






