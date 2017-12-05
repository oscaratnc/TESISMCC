
import Spo2Sensor as Sp2
import time
from smbus2 import SMBus
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import wiringpi
import Processing as pr
import numpy as np
from scipy import signal as sp
from gpiozero import Button
GPIO.setmode(GPIO.BCM)

#Definitions for ECG acquisition
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(CLK, CS, MISO, MOSI)


#Array variables to store samples
ecgValues = np.array([])
Red = np.array([])
IR = np.array([])
Spo2Value = 0


def getECG(self, numSeconds):
    sampleRate = 250
    starTime = wiringpi.millis()

    while wiringpi.millis()-starTime < numSeconds*1000: 
        Ecg = round((mcp.read_adc(1)*3.3)/1024,3)
        self.ecgValues = np.append(self.ecgValues,Ecg)
        wiringpi.delayMicroseconds(200)
   
   

def getSpo2(self,numSeconds, samplerate):
    print "begin measure"
    startTime = wiringpi.millis()
    Spo2 = Sp2.Spo2Sensor(sampleAvg= 8,sampleRate=samplerate)
    newSample = False
    AFthreshold= 17
    Spo2.enableAfull()
    Spo2.setFIFOAF(AFthreshold)
    interrupt  = Button(7)

    while wiringpi.millis()-startTime < numSeconds*1000:
      interrupt.when_activated = Spo2.sampleAvailable()
      if Spo2.newSample == True:
          Spo2.readSample()
          Spo2.newSample = False
          
    
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    print "Buffer IR: ", len(Spo2.buffer_ir)

    self.IR = Spo2.buffer_ir
    self.IR = pr.removeDC(self.IR)
    self.IR = sp.medfilt(self.IR)
    self.IR = pr.lowPasFIRFilter(pr(), self.IR, 6,samplerate)
    #self.IR = pr.lowPasFIRFilter(pr(), self.IR, 60,samplerate)
    for x in np.ndarray(self.IR):
        print x
    
    print "Buffer Red: ", len(Spo2.buffer_red)
    self.Red = Spo2.buffer_red
    self.Red = sp.medfilt(self.Red)
    self.Red = pr.lowPasFIRFilter(pr(), self.Red, 6,samplerate)
    #self.Red = pr.lowPasFIRFilter(pr(), self.Red, 60,samplerate)
    for x in np.ndarray(self.Red):
        print x

    self.Spo2Value = pr.Processing.
    


  

   

   

       
   
   
        
    
   
    

    
    #      # print (wiringpi.millis()-startTime)/1000
    #       reD = Spo2Sensor.getRed()
    #       iR  = Spo2Sensor.getIR()
    #       #print "R: ", reD , "IR: ", iR
    #       self.Red = np.append(self.Red,reD)  
    #       self.IR = np.append(self.IR,iR)
   
    #   #self.Red = Spo2Sensor.lowPasFilter(self.Red,6,samplerate)
    #   #self.Red = Spo2Sensor.removeDC(self.Red)
   
   
    #   #self.IR = Spo2Sensor.lowPasFilter(self.IR,6,samplerate)
    #   #self.IR = Spo2Sensor.removeDC(self.IR)
   
   

    #   print "min IR:", min(self.IR)
    #   print "max IR:", max(self.IR)
    #   print "min RED:", min(self.Red)
    #   print "max RED: ", max(self.Red)

   











