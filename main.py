from chacalc import *
from generator import generate

def f(x):
    return 1 / np.pi / np.cosh(x)

def main():
    for i in range(2,5):
        n = 10**i
        data = generate(n)
        print(f'N {n}')
        # data = np.loadtxt('data_100')
        print(f'Медиана {median(data)}')
        print(f'Среднее {avr(data)}')
        print(f'Дисперсия {variance(data)}')
        print(f'Коэф аcсим {assimСoef(data)}')
        print(f'Эксцесса {exces(data)}')

        t = сredibilityAssessment(data, f, 1, maxiter=100)
        print(f'Оценка максимального правдоподобия\nt={t}')

        b = [0.1, 0.5, 1]
        print('Обобщенная радикальная оценка')
        for bi in b:
            t = generalRadical(data, f, 1, bi)
            print(f'b={bi}\tt={t}')
        print('\n' + ('='*50))


if __name__ == '__main__':
    main()