import MAX3010X as MAX30102
from smbus2 import SMBus
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import wiringpi
import numpy as np
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
sampleRate= 200

def setSamplerate(self, samplerate):
    self.sampleRate = samplerate

def getSampleRate(self):
    return sampleRate


def beginSpO2(self, sampleRate):
    Spo2Sensor.begintest(Spo2Sensor.MAX30102_PARTID, Spo2Sensor.MAX30102_EXPECTED_PARTID)
    Spo2Sensor.setup(31, 4, 2, sampleRate, 411, 4096)

#Array variables to store samples
ecgValues = np.array([])
Red = np.array([])
IR = np.array([])
RedAC =np.array([])
IRAC= np.array([])
       

def getECG(self, numSeconds):
    startTime = wiringpi.millis()
    while wiringpi.millis()-startTime < (numSeconds*1000): 
       # print (wiringpi.millis()-startTime)/1000
        Ecg = round((mcp.read_adc(1)*3.3)/1024,3)
        self.ecgValues = np.append(self.ecgValues,Ecg)
        wiringpi.delayMicroseconds(400)
    self.ecgValues = Spo2Sensor.removeDC(self.ecgValues)
   
        

def getSpo2(self,numSeconds):
    
   startTime = wiringpi.millis()
   samplerate = self.getSampleRate(self)

   while wiringpi.millis()-startTime < (numSeconds*1000): 
      # print (wiringpi.millis()-startTime)/1000
       reD = Spo2Sensor.getRed()
       iR  = Spo2Sensor.getIR()
       #print "R: ", reD , "IR: ", iR
       self.Red = np.append(self.Red,reD)  
       self.IR = np.append(self.IR,iR)
   
   self.Red = Spo2Sensor.lowPasFilter(self.Red,6,samplerate)
   self.Red = Spo2Sensor.removeDC(self.Red)
   
   
   self.IR = Spo2Sensor.lowPasFilter(self.IR,6,samplerate)
   self.IR = Spo2Sensor.removeDC(self.IR)
   
   

   print "min IR:", min(self.IR)
   print "max IR:", max(self.IR)
   print "min RED:", min(self.Red)
   print "max RED: ", max(self.Red)

   











