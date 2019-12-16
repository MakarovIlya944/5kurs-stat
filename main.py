from chacalc import *
from math import pi
from generator import generate
import json
from matplotlib.pyplot import *
import sys

def f(x):
	return 1 / pi / np.cosh(x)
def df(x,l):
	return np.tanh(x)/np.cosh(x)/np.pi/l

lineLenght = 70
monteCarloNumber = 100
monteCarloStep = monteCarloNumber//10

def makeExperiment(b, left=5, right=6, t=[0,0], l=[1,1], e=0):
	ans = {}

	for i in range(left, right):

		#print('\n' + ('='*lineLenght))
		n = 10 ** i
		#print(f'Параметры \tN {n}\tE {e}')
		#print(f'Параметры \tt чистое: {t[0]}\tзасоренное: {t[1]}')
		#print(f'Параметры \tl чистое: {l[0]}\tзасоренное: {l[1]}')

		res_data = {}
		res_data['median'] = []
		res_data['avr'] = []
		res_data['variance'] = []
		res_data['assimСoef'] = []
		res_data['exces'] = []
		res_data['credibility'] = {'calculated':[],'criteria':[]}
		res_data['radical'] = {bi:{'calculated':[],'criteria':[]} for bi in b}

		for m in range(monteCarloNumber):
			data = generate(n, '', l=l, t=t, e=e, savefile=False)

			res_data['median'].append(median(data))
			res_data['avr'].append(avr(data))
			res_data['variance'].append(variance(data))
			res_data['assimСoef'].append(assimСoef(data))
			res_data['exces'].append(exces(data))

			res_data['credibility']['calculated'].append(сredibilityAssessment(data, f, l[0]))
			res_data['credibility']['criteria'].append((res_data['credibility']['calculated'][-1]-t[0])*(res_data['credibility']['calculated'][-1]-t[0]))

			for bi in b:
				res_data['radical'][bi]['calculated'].append(generalRadical(data, f, l[0], bi))
				res_data['radical'][bi]['criteria'].append((res_data['radical'][bi]['calculated'][-1]-t[0])*(res_data['radical'][bi]['calculated'][-1]-t[0]))

			# if not m % monteCarloStep:
				#print(f'{m/monteCarloNumber*100}%')

		res_data['median'] = avr(res_data['median'])
		res_data['avr'] = avr(res_data['avr'])
		res_data['variance'] = avr(res_data['variance'])
		res_data['assimСoef'] = avr(res_data['assimСoef'])
		res_data['exces'] = avr(res_data['exces'])

		res_data['credibility']['calculated'] = avr(res_data['credibility']['calculated'])
		res_data['credibility']['criteria'] = avr(res_data['credibility']['criteria'])
		for bi in b:
			res_data['radical'][bi]['calculated'] = avr(res_data['radical'][bi]['calculated'])
			res_data['radical'][bi]['criteria'] = avr(res_data['radical'][bi]['criteria'])

		#print(f'Медиана \tвычисленное: {res_data["median"]}')

		#print(f'Среднее \tвычисленное: {res_data["avr"]}')

		#print(f'Дисперсия \tвычисленное: {res_data["variance"]}')

		#print(f'Коэф аcсим \tвычисленное: {res_data["assimСoef"]}')

		#print(f'Эксцесса \tвычисленное: {res_data["exces"]}')

		ans[n] = res_data

	return ans

def main():

	X = np.arange(-5,5,0.1)
	# проверяемые значение параметра смещения
	t = [0, 1, -3]
	# ошбика для параметра смещения
	er_t = [1, -5, 0]
	# проверяемые значение параметра масштаба
	l = [1, 0.25]
	# ошибка для параметра масштаба
	er_l = [2, 5]
	# степень робастности
	b = [0.1,  0.5,  1]
	# степень засорения
	e = [0.25, 0.5]

	t_data = [(t[i],er_t[i]) for i in range(len(t))]
	l_data = [(l[i],er_l[i]) for i in range(len(l))]

	# for _t, _er_t in t_data:
	
	_t = float(sys.argv[1])
	_er_t = float(sys.argv[2])
	_l = float(sys.argv[3])
	_er_l = float(sys.argv[4])
	
	# print(sys.argv)
	# exit(0)
	
	for _e in e:
		d = {'l':_l, 't':_t, 'er_l':_er_l+_l, 'er_t':_er_t+_t, 'e':_e}

		#print(f'\nСтепень засорения: {_e}\nЧистое распределение')
		d['clear'] = makeExperiment(b,t=[_t,_t],l=[_l,_l])
		#print(('+'*lineLenght))

		#print('\nЗасоренное распределение с симметричным засорением')
		d['symm'] = makeExperiment(b,t=[_t,_t],l=[_l,_er_l+_l],e=_e)
		#print(('+'*lineLenght))

		#print('\nЗасоренное распределение с асимметричным засорением')
		d['asymm'] = makeExperiment(b,t=[_t,_er_t+_t],l=[_l,_er_l+_l],e=_e)
		#print(('+'*lineLenght))

		f_clear = [f((x-_t)/_l) for x in X]
		f_dirty = [f((x-_er_t-_t)/(_er_l+_l)) for x in X]
		f_summe = [(1-_e)*f_clear[i] + _e*f_dirty[i] for i in range(len(X))]
		snap, ax = subplots()
		ax.plot(X, f_clear, label='clear')
		ax.plot(X, f_dirty, label='dirty')
		ax.plot(X, f_summe, label='summ')
		ax.legend()
		snap.savefig(f't_{_t}_{_er_t+_t}_l_{_l}_{_er_l+_l}_e_{_e}.png')

		with open(f'result_{_t}_{_er_t+_t}_l_{_l}_{_er_l+_l}.json', 'a+') as _f:
			_f.write(json.dumps(d) + '\n')

	influence = lambda x, b: integralOfInfluenceRadical(x,_t,_l,f,df,b)

	for bi in b:
		f_robast = [influence(x, bi) for x in X]
		snap = figure()
		plot(X, f_robast)
		snap.savefig(f'b_{bi}_t_{_t}_l_{_l}.png')

if __name__ == '__main__':
	main()