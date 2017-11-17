import matplotlib.pyplot as plt

def plot(self, x):
    i=0
    x= self.x
    time = [None]*len(x)

    for i in range (len(x)):
        time[i]=i
    
    axes = plt.gca()
    axes.set_ylim([max(x)-(.4*max(x)), max(x)+(.4+max(x))])
    plt.plot(time,x)

    plt.show()
