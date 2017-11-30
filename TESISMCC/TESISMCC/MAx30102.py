from smbus2 import SMBus
import numpy as np



def _get_valid(d,value):
    try:
        return d[value]
    except KeyError:
        raise KeyError("Value %s not valid, use one of: %s" % (value,','.join([str(s) for s in d.keys()])))

def _twos_complement(val,bits):
    #Compute the 2's complement of int value val
    if (val &(1<<(bits-1)))!= 0:
        val = val-(1<<bits)
    return val
class MAX30102(object):
    BUS  = 1
    i2c  = SMBus(BUS) 
    #REGISTERS:

        # INTERRUPT STATE REGISTERS
    MAX30102_INSTAT1 = 0x00
    MAX30102_INSTAT2 = 0x01
    MAX30102_INTENABLE1 = 0x02
    MAX30102_INTENABLE2 = 0x03

    # FIFO BUS REGISTERS
    MAX30102_FIFOWRITEPTR = 0x04
    MAX30102_FIFOOVERFLOW = 0x05
    MAX30102_FIFOREADPTR = 0x06
    MAX30102_FIFODATAREG = 0x07

    # CONFIGURATION REGISTERS
    MAX30102_FIFOCONFIG = 0x08
    MAX30102_MODECONFIG = 0x09
    MAX30102_SPO2CONFIG = 0x0A
    MAX30102_LED1_PULSEAMP = 0x0C
    MAX30102_LED2_PULSEAMP = 0x0D
    MAX30102_PROX_LED_PA = 0x10
    MAX30102_MULTILEDCONFIG1 = 0x11
    MAX30102_MULTILEDCONFIG2 = 0x12

    # DIE TEMPERATURE REGISTERS
    MAX30102_DIETEMPINT = 0x1F
    MAX30102_DIETEMPFRAC = 0X20
    MAX30102_DIETEMPCONFIG = 0X21

    # PROXIMITY FUNCTION REGISTERS
    MAX30102_PROXINTTHRES = 0X30

    # PARTID REGISTER
    MAX30102_REVISIONID = 0XFE
    MAX30102_PARTID = 0xFF

    # MAX30102 Commands
    MAX30102_INT_A_FULL_MASK = 0b10000000
    MAX30102_INT_A_FULL_ENABLE = 0x80
    MAX30102_INT_A_FULL_DISABLE = 0X00

    MAX30102_INT_A_DATA_RDY_MASK = 0b01000000
    MAX30102_INT_DATA_RDY_ENABLE = 0x40
    MAX30102_INT_DATA_RDY_DISABLE = 0x00

    MAX30102_INT_ALC_OVF_MASK = 0b00100000
    MAX30102_INT_ALC_OVF_ENABLE = 0x20
    MAX30102_INT_ALC_OVF_DISABLE = 0x00

    MAX30102_INT_PROX_INT_MASK = 0b00010000
    MAX30102_INT_PROX_INT_ENABLE = 0x10
    MAX30102_INT_PROX_INT_DISABLE = 0x00

    MAX30102_INT_DIE_TEMP_RDY_MASK = 0b00000010
    MAX30102_INT_DIE_TEMP_RDY_ENABLE = 0x02
    MAX30102_INT_DIE_TEMP_RDY_DISABLE = 0x00

    MAX30102_SAMPLEAVG_MASK = 0b11100000
    MAX30102_SAMPLEAVG_1 = 0x00
    MAX30102_SAMPLEAVG_2 = 0x20
    MAX30102_SAMPLEAVG_4 = 0x40
    MAX30102_SAMPLEAVG_8 = 0x60
    MAX30102_SAMPLEAVG_16 = 0x80
    MAX30102_SAMPLEAVG_32 = 0xA0

    MAX30102_ROLLOVER_MASK = 0xEF
    MAX30102_ROLLOVER_ENABLE = 0x10
    MAX30102_ROLLOVER_DISABLE = 0x00

    MAX30102_A_FULL_MASK = 0xF0

    # Mode configuration commands (page 19)
    MAX30102_SHUTDOWN_MASK = 0x7F
    MAX30102_SHUTDOWN = 0x80
    MAX30102_WAKEUP = 0x00

    MAX30102_RESET_MASK = 0xBF
    MAX30102_RESET = 0x40

    MAX30102_MODE_MASK = 0xF8
    MAX30102_MODE_REDONLY = 0x02  # HEARTRATE MODE (RED LED)
    MAX30102_MODE_IRONLY = 0x03  # SPO2 MODE (IR LED)
    MAX30102_MODE_MULTILED = 0x07  # MULTILED (RED & IR)

    # SPO2 configuration commands (pgs 19-20)
    MAX30102_ADCRANGE_MASK = 0x9F
    MAX30102_ADCRANGE_2048 = 0x00
    MAX30102_ADCRANGE_4096 = 0x20
    MAX30102_ADCRANGE_8192 = 0x40
    MAX30102_ADCRANGE_16384 = 0x60

    MAX30102_SAMPLERATE_MASK = 0xE3
    MAX30102_SAMPLERATE_50 = 0x00
    MAX30102_SAMPLERATE_100 = 0x04
    MAX30102_SAMPLERATE_200 = 0x08
    MAX30102_SAMPLERATE_400 = 0x0C
    MAX30102_SAMPLERATE_800 = 0x10
    MAX30102_SAMPLERATE_1000 = 0x14
    MAX30102_SAMPLERATE_1600 = 0x18
    MAX30102_SAMPLERATE_3200 = 0x1C

    MAX30102_PULSEWIDTH_MASK = 0xFC
    MAX30102_PULSEWIDTH_69 = 0x00
    MAX30102_PULSEWIDTH_118 = 0x01
    MAX30102_PULSEWIDTH_215 = 0x02
    MAX30102_PULSEWIDTH_411 = 0x03

    # Multi-LED Mode configuration (pg 22)
    MAX30102_SLOT1_MASK = 0xF8
    MAX30102_SLOT2_MASK = 0x8F
    MAX30102_SLOT3_MASK = 0xF8
    MAX30102_SLOT4_MASK = 0x8F

    SLOT_NONE = 0x00
    SLOT_RED_LED = 0x01
    SLOT_IR_LED = 0x02
    SLOT_NONE_PILOT = 0x04
    SLOT_RED_PILOT = 0x05
    SLOT_IR_PILOT = 0x06
    SLOT_GREEN_PILOT = 0x07

    MAX30102_EXPECTED_PARTID = 0x15

    INTERRUPT_SPO2  = 0
    INTERRUPT_HR = 1
    INTERRUPT_TEMP = 2
    INTERRUPT_FIFO = 3
    MODE_HR = 0x02
    MODE_SPO2 = 0x03
    MAX30102_ADDRESS = 0X57
    # REGISTER DEFINITION END


    #ADC RESOLUTION 69:15bits, 118:16bits, 215: 17bits, 411: 18 bits
    PULSE_WIDTH = { 69:  0, 118: 1, 215: 2, 411: 3}
    SAMPLE_RATE = { 50:0, 100:1, 200:2, 400:3, 800:4, 1000:5, 1600:6, 3200:7}
    LED_CURRENT = { 0: 0, .2: 1, .4: 2, 3.1:15, 6.4: 17, 12.5: 63, 25.4:127, 50:255}


    def __init__(self, mode = MODE_SPO2, sample_rate= 200, led_current_red =6.4, led_current_ir = 6.4, pulse_width= 411, max_buffer_len= 10000):
      
        self.set_mode(self.MODE_SPO2)
        self.set_led_current (led_current_red, led_current_ir)
        self.set_spo_config(pulse_width)

        self.buffer_red = np.array([])
        self.buffer_ir = np.array([])

        self.max_buffer_len = max_buffer_len
        self._interrupt = None

        print "Config done :)"

    @property
    def red(self):
        return self.buffer_red[-1] if self.buffer_red else None

    @property
    def ir(self):
        return self.bufer_ir[-1] if self.buffer_ir else None

    def set_led_current(self, led_current_red = 6.4, led_current_ir = 6.4):
        i2c = self.i2c
        #validate the settings, convert bit values
        led_current_red = _get_valid(self.LED_CURRENT, led_current_red )
        led_current_ir = _get_valid(self.LED_CURRENT,led_current_ir)
        i2c.write_byte_data(self.MAX30102_ADDRESS,self.MAX30102_LED1_PULSEAMP,(led_current_red<<4) | led_current_ir) 
        i2c.write_byte_data(self.MAX30102_ADDRESS,self.MAX30102_LED2_PULSEAMP,(led_current_red<<4) | led_current_ir)

    def set_mode(self, mode):
        i2c = self.i2c
        reg = i2c.read_byte_data(self.MAX30102_ADDRESS,self.MAX30102_MODECONFIG)
        i2c.write_byte_data(self.MAX30102_ADDRESS,self.MAX30102_MODECONFIG,reg & self.MAX30102_MODE_MASK)
        i2c.write_byte_data(self.MAX30102_ADDRESS, self.MAX30102_MODECONFIG, reg | mode)
        print "mode done"
        
    def set_spo_config(self, pulseWidth):
        i2c = self.i2c
        reg = i2c.read_byte_data(self.MAX30102_ADDRESS,self.MAX30102_SPO2CONFIG)
        reg = reg & 0xFC
        i2c.write_byte_data(self.MAX30102_ADDRESS, self.MAX30102_SPO2CONFIG, reg|pulseWidth)

    def enable_spo2(self):
        self.set_mode(self.MODE_SPO2)

    def disable_spo2(self):
        self.set_mode(self.MODE_HR)

    def enable_interrupt(self, interrupt_type):
        i2c = self.i2c
        i2c.write_byte_data(self.MAX30102_ADDRESS, self.MAX30102_INTENABLE1, (interrupt_type+1)<<4 )
        print i2c.read_byte_data(self.MAX30102_ADDRESS,self.MAX30102_INSTAT1)

    def getNumberOfSamples(self):
        i2c = self.i2c
        writePointer = i2c.read_byte_data(self.MAX30102_ADDRESS,self.MAX30102_FIFOWRITEPTR)
        readPointer = i2c.read_byte_data(self.MAX30102_ADDRESS,self.MAX30102_FIFOREADPTR)
        return abs(32+(writePointer - readPointer))%32

    def read_sensor(self):
        i2c = self.i2c
       
        
        
        Samples = i2c.read_i2c_block_data(self.MAX30102_ADDRESS,self.MAX30102_FIFODATAREG,6)
        tempLongRed = 0
        tempLongIR = 0

        tempsample=Samples[0]
        tempsample<<= 16
        tempLongRed = tempLongRed + tempsample

        tempsample=Samples[1]
        tempsample<<= 8 
        tempLongRed= tempLongRed+tempsample
                    
        tempsample= Samples[2]
        tempLongRed= tempLongRed + tempsample
        tempLongRed = tempLongRed & 0x3FFFF

        tempsample=Samples[3]
        tempsample<<= 16
        tempLongIR = tempLongIR + tempsample

        tempsample=Samples[4]
        tempsample<<= 8 
        tempLongIR = tempLongIR+tempsample
                    
        tempsample= Samples[2]
        tempLongIR =tempLongIR + tempsample
        tempLongIR = tempLongIR & 0x3FFFF
                    
        self.buffer_red = np.append(self.buffer_red,tempLongRed)
        self.buffer_ir  = np.append(self.buffer_ir, tempLongIR)

        self.buffer_red = self.buffer_red[-self.max_buffer_len:]
        self.buffer_ir = self.buffer_ir[-self.max_buffer_len:]
        
        

    def shutdown(self):
        i2c = self.i2c
        reg = i2c.read_byte_data(self.MAX30102_ADDRESS,self.MAX30102_MODECONFIG)
        i2c.write_byte_data(self.MAX30102_ADDRESS,self.MAX30102_MODECONFIG, reg | self.MAX30102_SHUTDOWN)

    def reset(self):
        i2c = self.i2c
        reg = i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_MODECONFIG)
        i2c.write_byte_data(self.MAX30102_ADDRESS, self.MAX30102_MODECONFIG, reg | self.MAX30102_RESET)

    def refresh_temperature (self):
        i2c = self.i2c
        reg  = i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_MODECONFIG)
        i2c.write_byte_data(self.MAX30102_ADDRESS, self.MAX30102_MODECONFIG,reg | (1 << 3))
            
    def get_temperature (self):
        i2c = self.i2c
        intg = _twos_complement(i2c.read_byte_data(self.MAX30102_ADDRESS,self.MAX30102_DIETEMPINT))
        frac = i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_DIETEMPFRAC)
        return intg + (frac * 0.0625)

    def get_rev_id(self):
        i2c = self.i2c
        return i2c.read_byte_data(self.MAX30102_ADDRESS,self.MAX30102_REVISIONID)

    def get_part_id (self):
        i2c = self.i2c
        return i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_PARTID)

    def getRegisters(self):
        i2c = self.i2c
        print   "INT STATUS: ", i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_INSTAT1),
        print   "INT_ENABLE:", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_INTENABLE1),
        print   "FIFO_WR_PTR: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_FIFOWRITEPTR),
        print   "OVRFLOW_CTR: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_FIFOOVERFLOW),
        print   "FIFO_RD_PTR: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_FIFOREADPTR),
        print   "FIFO_DATA: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_FIFODATAREG),
        print   "MODE_CONFIG: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_MODECONFIG),
        print   "SPO2_CONFIG: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_SPO2CONFIG),
        print   "LED1_CONFIG: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_LED1_PULSEAMP),
        print   "LED2_CONFIG: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_LED2_PULSEAMP),
        print   "TEMP_INTG:", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_DIETEMPINT),
        print   "TEMP_FRAC: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_DIETEMPFRAC),
        print   "REV_ID: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_REVISIONID),
        print   "PART_ID: ", self.i2c.read_byte_data(self.MAX30102_ADDRESS, self.MAX30102_PARTID),
                    