
IR_AC_Max = 20
IR_AC_Min = -20

IR_AC_Signal_Current = 0
IR_AC_Signal_Previous
IR_AC_Signal_min = 0
IR_AC_Signal_max = 0
IR_Average_Estimated

positiveEdge = 0
negativeEdge = 0
ir_avg_reg = 0

cbuf=[0]*32
offset = 0;
FIRCoeffs = [172, 321, 579, 927, 1360, 1858, 2390, 2916, 3391, 3768, 4012, 4096]

def checkForBeat (self, sample):
    beatDetected = False

    IR_AC_Signal_Previous = IR_AC_Signal_Current
    #print IR_AC_Signal_Current
    IR_Average_Estimated = averageDCEstimator (ir_avg_reg, sample)
    IR_AC_Signal_Current = lowpassFIRFilter( sample- IR_Average_Estimated)

    if (IR_AC_Signal_Previous < 0 ) & (IR_AC_Signal_Current >= 0):
        IR_AC_Max = IR_AC_Signal_max
        IR_AC_Min = IR_AC_Signal_min
         
        positiveEdge = 1
        negativeEdge = 0
        IR_AC_Signal_max = 0 


