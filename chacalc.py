import numpy as np
import scipy.integrate
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

# b=0 ОМП
def integralOfInfluenceRadical(y,t,l,f,dF,b):
    F=lambda x: __commonFunctionRadical(x,t,l,f,dF,b)*dF(x,l)
    i = scipy.integrate.quad(F, -10, -0.000000001)+scipy.integrate.quad(F, 0.000000001,10)
    return __commonFunctionRadical(y,t,l,f,dF,b)/i[0]

def __commonFunctionRadical(y,t,l,f,dF,b):
    return dF((y-t)/l,l)/f((y-t)/l)*np.power(f((y-t)/l),b)

# оценка максимального правдоподобия
def сredibilityAssessment(data, f, l):
    last_t = median(data)
    F = lambda t: np.sum([-np.log(f((y-t)/l)) for y in data])
    res = minimize(F, last_t, method='nelder-mead',
    options={'xtol': 1e-3})
    return round(res.x[0],my_round)

# обобщенная радикальная оценка
def generalRadical(data, f, l, b):
    last_t = median(data)
    F = lambda t: (-1/(b*np.power(l,b))) * np.sum([np.power(f((y-t)/l),b) for y in data])
    res = minimize(F, last_t, method='nelder-mead',
    options={'xtol': 1e-3})
    return round(res.x[0],my_round)