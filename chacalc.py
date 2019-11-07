import numpy as np


def median(data):
    return np.median(data)


def avr(data):
    return np.mean(data)


def variance(data):
    return np.var(data)


def assimСoef(data):
    e = avr(data)
    v = variance(data)
    return np.sum([(el - e)**3 for el in data]) / len(data) / np.power(v, 1.5)


def exces(data):
    e = avr(data)
    v = variance(data)
    return np.sum([(el - e)**4 for el in data]) / len(data) / (v ** 2)


def сredibilityAssessment(data, f, l, eps=1E-10, maxiter=1E+4):
    last_x = median(data)
    F = lambda t: np.sum([-np.log(f((y-t)/l)) for y in data])
    dF = lambda t: np.sum([np.tanh((y-t)/l) for y in data])
    i = 0
    while i < maxiter:
            new_x = last_x - F(last_x)/dF(last_x)
            if abs(new_x - last_x) < eps:
                return new_x
            new_x = last_x
            i += 1
    return
