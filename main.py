#!/usr/bin/env python2.7

import numpy as np

train_file = 'train_PA-D.dat'

d = np.loadtxt(train_file, comments='#')
for i in d:
    print i