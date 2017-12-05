from scipy import signal as sp

class filters:
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
      
    
    def removeDC(self, measure):
        mean = np.mean(measure)
        measure = measure-mean
        return measure
        
    def Normalize(self, measure):
        abs = np.max(np.abs(measure))
        measureN = measure/abs
        measureN = np.round(measureN,4)
        return measureN
