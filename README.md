signal_ICT_HeerMehta_92400133037-->
A Python package for basic Signal Generation and Operations

Modules-->
1. unitary_signals
-unit_step(n) → Unit step signal
-unit_impulse(n) → Unit impulse signal
-ramp_signal(n) → Ramp signal

2. trigonometric_signals
-sine_wave(A, f, phi, t) → Sine wave
-cosine_wave(A, f, phi, t) → Cosine wave
-exponential_signal(A, a, t) → Exponential signal

3. operations
-time_shift(signal, k) → Shift signal by k
-time_scale(signal, k) → Scale time axis
-signal_addition(signal1, signal2) → Add two signals
-signal_multiplication(signal1, signal2) → Multiply two signals

INSTALLATION-->
pip install dist/signal_ICT_HeerMehta_92400133037-0.1.0-py3-none-any.whl


USAGE EXAMPLE-->
from signal_ICT_HeerMehta_92400133037 import unitary_signals
unitary_signals.unit_step(20)

