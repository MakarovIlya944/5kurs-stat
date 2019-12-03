from chacalc import *
from math import pi
from generator import generate
import json

def f(x):
    return 1 / pi / np.cosh(x)

lineLenght = 70

def makeExperiment(b, left=2, right=5, t=[0,0], l=[1,1], e=0):

    ans = {}

    for i in range(left, right):
        print('\n' + ('='*lineLenght))
        n = 10**i
        print(f'Параметры \tN {n}\tE {e}')
        print(f'Параметры \tt чистое: {t[0]}\tзасоренное: {t[1]}')
        print(f'Параметры \tl чистое: {l[0]}\tзасоренное: {l[1]}')
        filename = f'data_t{t[0]}_{t[1]}_l{l[0]}_{l[1]}_e{e}_n{n}'
        try:
            data = np.loadtxt(filename)
        except Exception:
            data = generate(n, filename)

        res_data = {}

        res_data['median']=median(data)
        print(f'Медиана \tвычисленное: {res_data["median"]}')

        res_data['avr']=avr(data)
        print(f'Среднее \tвычисленное: {res_data["avr"]}')

        res_data['variance']=variance(data)
        print(f'Дисперсия \tвычисленное: {res_data["variance"]} \tтеоретическое: {round(pi*pi/4,5)}')

        res_data['assimСoef']=assimСoef(data)
        print(f'Коэф аcсим \tвычисленное: {res_data["assimСoef"]}')

        res_data['exces']=exces(data)
        print(f'Эксцесса \tвычисленное: {res_data["exces"]} \tтеоретическое: {5}\n')
        
        print('Оценим t')
        _t = сredibilityAssessment(data, f, 1)
        res_data['credibility']=_t
        print(f'Оценка максимального правдоподобия\nt={_t}')

        print('Обобщенная радикальная оценка')
        res_data['radical'] = {}
        for bi in b:
            _t = generalRadical(data, f, 1, bi)
            print(f'b={bi}\tt={_t}')
            res_data['radical'][bi] = _t

        ans[n] = res_data

    return ans

def main():

    data = []

    # проверяемые значение параметра смещения
    t = [0, 1, -1]
    # ошбика для параметра смещения
    er_t = [1, 0, 2]
    # проверяемые значение параметра масштаба
    l = [1, 2, -1]
    # ошибка для параметра масштаба
    er_l = [1, 3, 2]
    # степень робастности
    b = [0.1, 0.25, 0.5, 0.75, 1]
    # степень засорения
    e = [0.25, 0.5, 0.75]

    t_data = [(t[i],er_t[i]) for i in range(len(t))]
    l_data = [(l[i],er_l[i]) for i in range(len(l))]

    for _t, _er_t in t_data:
        print(('/\\'*lineLenght))
        print(f'Значение t {_t} er t {_er_t}')
        for _l, _er_l in l_data:
            print(f'Значение l {_l} er l {_er_l}')
            for _e in e:
                d = {'l':_l, 't':_t, 'er_l':_er_l+_l, 'er_t':_er_t+_t, 'e':_e}

                print(f'\nСтепень засорения: {_e}\nЧистое распределение')
                d['clear'] = makeExperiment(b)
                print(('+'*lineLenght))

                print('\nЗасоренное распределение с симметричным засорением')
                d['symm'] = makeExperiment(b,t=[_t,_t],l=[_l,_er_l+_l],e=_e)
                print(('+'*lineLenght))

                print('\nЗасоренное распределение с асимметричным засорением')
                d['asymm'] = makeExperiment(b,t=[_t,_er_t+_t],l=[_l,_er_l+_l],e=_e)
                print(('+'*lineLenght))

                data.append(d)
    
    with open('result.json', 'w') as f:
        f.write(json.dumps(data))

if __name__ == '__main__':
    main()