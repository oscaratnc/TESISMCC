import Adafruit_GPIO as SPI
import wiringpi
import Adafruit_MCP3008

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE))

sampleNumber = 10

ecgValues = [0] * sampleNumber

for i in range(sampleNumber):
    ecgValues[i] = mcp.read_adc(0)
    print (ecgValues)
    wiringpi.delayMicroseconds(400)

