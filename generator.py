import numpy as np

def generate(n, l=1, t=0):
    res = []
    with open(f'data_{n}','w') as f:
        for i in range(n):
            x = np.log(np.tan(np.pi * np.random.random(1) / 2))
            x = x*l+t
            f.write(f'{x}\n')
            res.append(x)
    return res