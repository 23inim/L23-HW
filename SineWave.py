import numpy
from matplotlib import pyplot as plt

#function to create and show sine wave
def sineWave():
    #define the x axis for the plot
    x = numpy.arange(0, numpy.pi * 2, 0.01)
    #calulate corresponding y coordinates
    y = numpy.sin(x*2) #frequency doubled by multiplying x by 2

    #plot
    #choose plot type and input x and y coordinates
    plt.plot(x, y)
    #add the sine wave title to the graph
    plt.title("Sine Wave")
    #show the plot
    plt.show()

if __name__ == "__main__":
    sineWave()