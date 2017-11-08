



import wiringpi
import Adafruit_MCP3008

CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(CLK, CS, MISO, MOSI)



ecgValues = []
while True:

    ecgValues.append(round((mcp.read_adc(1)*3.3)/1024,2))
    print(ecgValues[len(ecgValues)-1])
    #Sampling Frecuency 250Hz
    wiringpi.delayMicroseconds(400)
    if (len(ecgValues)-1) == 5000:
        print(ecgValues)
        break
