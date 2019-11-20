import numpy as np
from scipy.optimize import minimize


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


# оценка максимального правдоподобия
def сredibilityAssessment(data, f, l, eps=1E-10, maxiter=1E+4):
    last_t = median(data)
    F = lambda t: np.sum([-np.log(f((y-t)/l)) for y in data])
    res = minimize(F, last_t, method='nelder-mead',
    options={'xtol': 1e-8})
    return res.x[0]
    # dF = lambda t: np.sum([np.tanh((y-t)/l)/l for y in data])
    # i = 0
    # while i < maxiter:
    #         new_t = last_t - F(last_t)/dF(last_t)
    #         if not (i % 1):
    #             print(f'#{i}\tt={new_t}')
    #         if abs(new_t - last_t) < eps:
    #             return new_t
    #         last_t = new_t
    #         i += 1
    # return new_t

# обобщенная радикальная оценка
def generalRadical(data, f, l, b, eps=1E-10, maxiter=1E+4):
    last_t = median(data)
    F = lambda t: (-1/(b*np.power(l,b))) * np.sum([np.power(f((y-t)/l),b) for y in data])
    res = minimize(F, last_t, method='nelder-mead',
    options={'xtol': 1e-8})
    return res.x[0]
    # dF = lambda t: (-1/np.power(np.pi*l,b)/l) * np.sum([
    #     np.sinh((y-t)/l) / np.power(np.cosh((y-t)/l),b+1)
    #     for y in data])
    # i = 0
    # while i < maxiter:
    #         new_t = last_t - F(last_t)/dF(last_t)
    #         if abs(new_t - last_t) < eps:
    #             return new_t
    #         last_t = new_t
    #         i += 1
    # return new_t