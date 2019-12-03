import numpy as np
from scipy.optimize import minimize


my_round = 5

def median(data):
    return round(np.median(data),my_round)


def avr(data):
    return round(np.mean(data),my_round)


def variance(data):
    return round(np.var(data),my_round)


def assimСoef(data):
    e = avr(data)
    v = variance(data)
    return round(np.sum([(el - e)**3 for el in data]) / len(data) / np.power(v, 1.5),my_round)


def exces(data):
    e = avr(data)
    v = variance(data)
    return round(np.sum([(el - e)**4 for el in data]) / len(data) / (v ** 2),my_round)


# оценка максимального правдоподобия
def сredibilityAssessment(data, f, l):
    last_t = median(data)
    F = lambda t: np.sum([-np.log(f((y-t)/l)) for y in data])
    res = minimize(F, last_t, method='nelder-mead',
    options={'xtol': 1e-8})
    return round(res.x[0],my_round)
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
def generalRadical(data, f, l, b):
    last_t = median(data)
    F = lambda t: (-1/(b*np.power(l,b))) * np.sum([np.power(f((y-t)/l),b) for y in data])
    res = minimize(F, last_t, method='nelder-mead',
    options={'xtol': 1e-8})
    return round(res.x[0],my_round)
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