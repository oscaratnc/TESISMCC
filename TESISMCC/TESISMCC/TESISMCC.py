import MAX3010X as MAX30102
from smbus2 import SMBus

import RPi.GPIO as GPIO
import ptvsd

ptvsd.enable_attach(secret = 'Rpi')
#10.206.251.180

GPIO.setmode(GPIO.BCM)
max102 = MAX30102.MAX30102.max102
GPIO.setup(4, GPIO.IN)
int_status = GPIO.input(4)
i = 0
Red = []
IR = []

print "interrupt status", int_status

Spo2Sensor = MAX30102.MAX30102()
Spo2Sensor.begintest(Spo2Sensor.MAX30102_PARTID, Spo2Sensor.MAX30102_EXPECTED_PARTID)
Spo2Sensor.setup(31, 4, 2, 100, 411, 4096)
print"###################################################."
i = 0
while i in range (200):
    redValue = Spo2Sensor.getRed()
    Red.append(redValue)
    irValue = Spo2Sensor.getIR()
    IR.append(irValue)
    i+=1
 
Red = Spo2Sensor.lastCorrect(Red)
print Red
IR = Spo2Sensor.lastCorrect(IR)
print IR




  #   print "read pointer 1: ", Spo2Sensor.getReadPointer()
  #  sample = max102.read_i2c_block_data(Spo2Sensor.MAX30102_ADDRESS, Spo2Sensor.MAX30102_FIFODATAREG,6)
  # print "read pointer 2: ", Spo2Sensor.getReadPointer()
  #  print "sample read:", sample
  #  Redsample = sample[0:3]
  #  IRsample = sample[3:6]
  #  Redvalue = Red.append(Spo2Sensor.concatbyte(Redsample))
  #  IRvalue  = IR.append(Spo2Sensor.concatbyte(IRsample))
  #  print Red
  #  print IR
  #  i = i+1





