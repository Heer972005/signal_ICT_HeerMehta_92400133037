from signal_ICT_HeerMehta_92400133037 import unitary_signals as us
from signal_ICT_HeerMehta_92400133037 import trigonometric_signals as ts
from signal_ICT_HeerMehta_92400133037 import operations as op
import numpy as np
import matplotlib.pyplot as plt

n = 20
step_signal = us.unit_step(n)
impulse_signal = us.unit_impulse(n)
ramp_signal = us.ramp_signal(n)


t = np.linspace(0, 1, 500)
sine_signal = ts.sine_wave(2, 5, 0, t)
cosine_signal = ts.cosine_wave(2, 5, 0, t)

sine_shifted = op.time_shift(sine_signal, 5)
plt.figure()
plt.plot(t, sine_signal, label="Original Sine")
plt.plot(t, sine_shifted, label="Shifted Sine (+5)")
plt.title("Sine Wave - Original vs Shifted")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

x = np.arange(-n, n)
added_signal = op.signal_addition(step_signal, ramp_signal)
plt.figure()
plt.stem(x, added_signal, basefmt=" ")
plt.title("Addition of Step and Ramp Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

multiplied_signal = op.signal_multiplication(sine_signal, cosine_signal)
plt.plot(t,multiplied_signal, label="Sine *Cosine")
plt.grid(True)
plt.legend()
plt.show()