import glob
import numpy as np
import matplotlib.pyplot as plt

filenames = sorted(glob.glob("data/inflammation*.csv"))
filenames = filenames[0:3]
for f in filenames:
    print(f)

    data = np.loadtxt(fname=f, delimiter=",")

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel("average")
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel("max")
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel("min")
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    plt.show()
