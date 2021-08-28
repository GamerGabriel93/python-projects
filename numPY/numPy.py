import numpy as np


def tutorial():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))
    b = np.array([6, 7, 8])
    print(b)
    print(type(b))


def different():
    a = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    b = np.arange(11)
    c = a - b
    print('A tömb elemei:', a)
    print('B tömb elemei:', b)
    print('C tömb elemei:', c)
