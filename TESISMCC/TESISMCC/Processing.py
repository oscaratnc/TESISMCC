from scipy import signal as sp
import numpy as np

class Processing:
    def lowPasFIRFilter(self,signal,fc,sampleF):
        sampleRate = sampleF
        nyq_rate = sampleRate/2.0
        width = (fc*1.1)/nyq_rate
        rst  = 60.0
        N, beta = sp.kaiserord(rst, width)
        cutoff_hz = fc
        taps  = sp.firwin(N, cutoff_hz/nyq_rate,width, window = 'kaiser')
        filtered = sp.lfilter(taps,1.0,signal)
        return filtered
      
    
    def getACcomponent(self, measure):
        mean = np.mean(measure)
        measure = measure[1000:np.alen(measure)]-mean
        return measure
    
    def getDCComponent(self,measure):
        DCcomponent = np.mean(measure)
        return DCcomponent
    
    def ratioOfRatios(self, measureRed,measureIR):
        dcRed= getDCComponent(measureRed)
        acRed = getACcomponent(measureRed)
        dcIR = getDCComponent(measureIR)
        acIR = getACcomponent(measureIR)

        RR = (acRed/dcRed) / (acIR/dcIR)

        return RR

    def calcSpO2(self, measureRed, measureIR):
        RR = self.ratioOfRatios(measureRed, measureIR)
        spO2 = 110-25 * RR
        return spO2
        
    def Normalize(self, measure):
        abs = np.max(np.abs(measure))
        measureN = measure/abs
        measureN = np.round(measureN,4)
        return measureN
