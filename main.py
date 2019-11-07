from chacalc import *
from generator import generate

def f(x):
    return 1 / np.pi / np.cosh(x)

def main():
    data = generate(10)
    #data = np.loadtxt('data_10000')
    #print(variance(data))
    #print(exces(data))
    #print(abs(variance(data)-(np.power(np.pi,2))/4))
    #print(abs(exces(data)-5))


if __name__ == '__main__':
    main()