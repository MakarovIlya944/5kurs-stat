import numpy as np

### If r < 1-e 
###    origin raspredelenie [0]
### else
###    zasorennoe raspredelenie [1]
### symetric one t diff l
### assemetric diff t diff l
def generate(n, filename, l=[1,1], t=[0,0], e=0, savefile=True):
    res = []
    if savefile:
        with open(filename, 'w') as f:
            for i in range(n):
                if np.random.random(1) <= (1 - e):
                    _l = l[0]
                    _t = t[0]
                else:
                    _l = l[1]
                    _t = t[1]
                x = np.log(np.tan(np.pi * np.random.random(1) / 2))
                x = x*_l+_t
                f.write(f'{x[0]}\n')
                res.append(x)
    else:
        for i in range(n):
            if np.random.random(1) <= (1 - e):
                _l = l[0]
                _t = t[0]
            else:
                _l = l[1]
                _t = t[1]
            x = np.log(np.tan(np.pi * np.random.random(1) / 2))
            x = x * _l + _t
            res.append(x)
    return res