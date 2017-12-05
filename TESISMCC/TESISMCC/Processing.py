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
    
    def quitaSobretiro(self,measure):
        measure[0:1001] = 0
        return measure

    
    def getACcomponent(self, measure):
        mean = np.mean(measure)
        measure = measure-mean
        return measure
    
    def getDCComponent(self,measure):
        DCcomponent = np.mean(measure)
        return DCcomponent
    
    def ratioOfRatios(self, measureRed,measureIR):
        dcRed= self.getDCComponent(measureRed)
        acRed = self.getACcomponent(measureRed)
        dcIR = self.getDCComponent(measureIR)
        acIR = self.getACcomponent(measureIR)

        RR = (acRed/dcRed) / (acIR/dcIR)

        return RR

    def calcSpO2(self, measureRed, measureIR):
        RR = self.ratioOfRatios(measureRed, measureIR)
        spO2Array = 110-25 * RR

        Spo2Value = np.around(np.mean(spO2Array),0)

        return Spo2Value
        
    def Normalize(self, measure):
        abs = np.max(np.abs(measure))
        measureN = measure/abs
        measureN = np.round(measureN,4)
        return measureN
