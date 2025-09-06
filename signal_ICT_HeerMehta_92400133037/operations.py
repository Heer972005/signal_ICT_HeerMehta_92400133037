import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal,k):
    shifted_signal=np.roll(signal,k)
    if(k>0):
        shifted_signal[:k]=0
    elif k<0:
        shifted_signal[k:]=0
    return shifted_signal


def time_scale(signal,k):
    n=np.arange(0,len(signal),k)
    n=n.astype(int)
    n=n[n<len(signal)]
    return signal[n]


def signal_addition(signal1,signal2):
    if (len(signal1)!=len(signal2)):
        raise ValueError("Signals must have the same length for addition")
    return signal1 + signal2


def signal_multiplication(signal1,signal2):
    if(len(signal1)!=len(signal2)):
        raise ValueError("Signals must have the same length for multiplication")
    return signal1*signal2


def plot_signal(signal,t):
    plt.stem(t,signal,basefmt=" ")
    plt.title("Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()