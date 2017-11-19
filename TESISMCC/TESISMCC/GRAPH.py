import matplotlib.pyplot as plt
plt.use('Agg')
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


plt.plot([1,2,3],[5,7,4])
