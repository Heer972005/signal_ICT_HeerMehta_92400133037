import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    signal=[]
    for i in range(-n,n):
        if i>=0:
            signal.append(1)
        else:
            signal.append(0)
    signal=np.array(signal)
    plt.stem(range(-n,n),signal)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal



def unit_impulse(n):
    signal=np.zeros(n)
    signal[0]=1
    plt.stem(range(n),signal)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal


def ramp_signal(n):
    signal=np.array([i if i>=0 else 0 for i in range(-n,n)])
    plt.stem(range(-n,n), signal)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal
