from glob import glob
import os
import numpy as np

d = 'elastix'

with open(os.path.join(d, 'TransformParameters.0.txt')) as f:
    lines = f.readlines()
    params = lines[2]
    params = params.replace('(', '').replace(')', '')
    params = params.split()[1:]

    params = [float(p) for p in params]

    P = params
    H = np.array([[P[0], P[1], P[4]],
                  [P[2], P[3], P[5]],
                  [0, 0, 1]])

    H_file = '%03d.%03d.H' % (0, 1)

    print("Writing %s" % os.path.abspath(H_file))
    with open(H_file, 'w'):
        np.savetxt(H_file, H)
