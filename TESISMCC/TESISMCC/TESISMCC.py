import MAX3010X as MAX30102
from smbus2 import SMBus
import wiringpi as wiry

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
i = 0
samplesTaken = 0
Spo2Sensor = MAX30102.MAX30102()
Spo2Sensor.begintest(Spo2Sensor.MAX30102_PARTID, Spo2Sensor.MAX30102_EXPECTED_PARTID)
Spo2Sensor.setup(31, 4, 2, 100, 411, 4096)
print"###################################################."
Starttime = wiry.millis()
while i in range (50):
    Spo2Sensor.check()

    while Spo2Sensor.available():
        samplesTaken+=1
        print "R: ", Spo2Sensor.getFIFORed, ", IR: ", Spo2Sensor.getFIFOIR, "Hz: ", (samplesTaken/(wiry.millis()-Starttime)/1000)
        Spo2Sensor.nextSample()
    i+=1








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





