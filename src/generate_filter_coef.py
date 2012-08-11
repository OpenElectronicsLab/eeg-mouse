#!/usr/bin/python
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

nyquest_freq = 250./2;

# 10-12 Hz 10th order elliptic bandpass filter, from
x_filter = signal.iirdesign(
    wp = [10.5/nyquest_freq, 14.5/nyquest_freq],
    ws = [4./nyquest_freq, 20./nyquest_freq],
    gstop=30, gpass=1, ftype='butterworth'
)

# 21.5-24.5 Hz 12th order elliptic bandpass filter, from
y_filter = signal.iirdesign(
    wp = [21.0/nyquest_freq, 25.0/nyquest_freq],
    ws = [15./nyquest_freq, 35./nyquest_freq],
    gstop=60, gpass=1, ftype='butterworth'
)

# 5 Hz 10th order elliptic lowpass filter, from
smooth_filter = signal.iirdesign(
    wp = 5./nyquest_freq,
    ws= 14./nyquest_freq, gstop=40,
    gpass=1, ftype='butterworth'
)


fig = plt.figure()
for filter in [x_filter, y_filter, smooth_filter]:
    w,h = signal.freqz(*filter)
    plt.plot(w*(nyquest_freq/max(w)), np.abs(h))
    plt.xlim(0,40)
    plt.xlabel('frequency (Hz)');
    plt.ylabel('response');
fig.savefig("test.png")

with open('filter_coefs.yaml','wt') as f:
    f.write('x_filter:\n');
    f.write('    in_coef: ' + str(x_filter[0].tolist()) + '\n');
    f.write('    out_coef: ' + str(x_filter[1][1:].tolist()) + '\n');
    f.write('y_filter:\n');
    f.write('    in_coef: ' + str(y_filter[0].tolist()) + '\n');
    f.write('    out_coef: ' + str(y_filter[1][1:].tolist()) + '\n');
    f.write('smooth_filter:\n');
    f.write('    in_coef: ' + str(smooth_filter[0].tolist()) + '\n');
    f.write('    out_coef: ' + str(smooth_filter[1][1:].tolist()) + '\n');

