#import MAX3010X as MAX30102
#import MAx30102 
import Spo2Sensor as Sp2
from smbus2 import SMBus
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import wiringpi
import numpy as np
from gpiozero import Button
GPIO.setmode(GPIO.BCM)

#Definitions for ECG acquisition
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(CLK, CS, MISO, MOSI)

#Definitions for SPO2 Acquisition
#max102 = MAX30102.MAX30102.max102
#Spo2Sensor = MAX30102.MAX30102()
#sampleRate= 200

#def setSamplerate(self, samplerate):
#    self.sampleRate = samplerate

#def getSampleRate(self):
#    return sampleRate
#def beginSpO2(self, sampleRate):
#    Spo2Sensor.begintest(Spo2Sensor.MAX30102_PARTID, Spo2Sensor.MAX30102_EXPECTED_PARTID)
#    Spo2Sensor.setup(31, 4, 2, sampleRate, 411, 4096)
#    Spo2Sensor.setup()
    

#Array variables to store samples
ecgValues = np.array([])
Red = np.array([])
IR = np.array([])


def getECG(self, numSeconds):
    startTime = wiringpi.millis()
    while wiringpi.millis()-startTime < (numSeconds*1000): 
       # print (wiringpi.millis()-startTime)/1000
        Ecg = round((mcp.read_adc(1)*3.3)/1024,3)
        self.ecgValues = np.append(self.ecgValues,Ecg)
        wiringpi.delayMicroseconds(200)
    #self.ecgValues = Spo2Sensor.removeDC(self.ecgValues)
   

def getSpo2(self,numSeconds, samplerate):
    print "begin measure"
    startTime = wiringpi.millis()
    Spo2 = Sp2.Spo2Sensor(sampleAvg= 4,sampleRate=samplerate)
    Spo2.enableAfull()
    Spo2.setFIFOAF(31)
    interrupt  = Button(7)
 
    while wiringpi.millis()-startTime < numSeconds*1000:
       interrupt.when_activated = Spo2.getNumberofSamples
    
      
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print "Buffer IR: ", len(Spo2.buffer_ir)
    self.IR = Spo2.buffer_ir
    print Spo2.buffer_ir
    print "Buffer Red: ", len(Spo2.buffer_red)
    self.Red = Spo2.buffer_red
    print Spo2.buffer_red
    print (wiringpi.millis()-startTime)

    #mx102 = MAx30102.MAX30102()
    #mx102.enable_interrupt(mx102.INTERRUPT_FIFO)
    #startTime = wiringpi.millis()
    #interrupt = Button(7)
    #interrupt.when_activated = mx102.read_sensor
    #startTime = wiringpi.millis()
    #while wiringpi.millis()-startTime < (numSeconds*1000): 
    #    RedValue = Spo2Sensor.getRed()
    #    IRValue = Spo2Sensor.getIR()
    #    Spo2Sensor.nextSample()
    #    self.Red = np.append(self.Red,RedValue)
    #    self.IR = np.append(self.IR, IRValue)

        
   
        
    
   
    

    
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

   











