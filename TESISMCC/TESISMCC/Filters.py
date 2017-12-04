from scipy import signal as sp

class filters:
    def lowPasFilter(self,signal,fc,sampleF):
        sampleRate  = sampleF
        print "Sample Rate: ", sampleRate
        nyq_rate = sampleRate/2.0
        print "Nyq: ", nyq_rate
        rbp= 3
      
        rtb= 40 

        Wp = fc/nyq_rate
        Ws= Wp*1.1
        print "Wp = ",Wp
        [N, Wn] = sp.buttord(Wp, Ws, rbp,rtb )
        print N, Wn
        [b, a] = sp.butter(N,Wp,'low')
        print b, a

        filtered = sp.lfilter(b,a,signal)
        
        return filtered
   

