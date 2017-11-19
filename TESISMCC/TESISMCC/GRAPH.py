import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('agg')
def plot(x):
    i=0
    x=x
    time = [None]*len(x)

    for i in range (len(x)):
        time[i]=i
    
    axes = plt.gca()
    axes.set_ylim([max(x)-1500, max(x)+1500])
    plt.plot(time,x)

    plt.show()



