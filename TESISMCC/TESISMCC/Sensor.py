import MAX3010X as MAX30102
from smbus2 import SMBus
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import wiringpi
GPIO.setmode(GPIO.BCM)

#Definitions for ECG acquisition
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(CLK, CS, MISO, MOSI)

#Definitions for SPO2 Acquisition
max102 = MAX30102.MAX30102.max102
Spo2Sensor = MAX30102.MAX30102()
Spo2Sensor.begintest(Spo2Sensor.MAX30102_PARTID, Spo2Sensor.MAX30102_EXPECTED_PARTID)
Spo2Sensor.setup(31, 4, 2, 100, 411, 4096)

#Array variables to store samples
ecgValues = []
Red = []
IR = []

def getECG(self, num):
    while True: 
        Ecg = round((mcp.read_adc(1)*3.3)/1024,2)
        ecgValues.append(Ecg)
        wiringpi.delayMicroseconds(400)
        if (len(ecgValues)-1 == num):
                break

def getSpo2(self,num):
    
    while True:
       
        reD = Spo2Sensor.getRed()
        iR  = Spo2Sensor.getIR()
        #print "R: ", reD , "IR: ", iR
        Red.append(reD)
        IR.append(iR)
        if (len(IR)-1 == num):
            break













