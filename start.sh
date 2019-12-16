#REM C:/Users/i.makarov.2015/Desktop/matstat/5kurs-stat/venv/Scripts/python.exe main.py 
#C:/Users/i.makarov.2015/Desktop/matstat/5kurs-stat/venv/Scripts/python.exe main.py 0 1 1 2
t=(0 1 -3)
# ошбика для параметра смещения
er_t=(1 -5 0)
# проверяемые значение параметра масштаба
l=(1 0.25 10)
# ошибка для параметра масштаба
er_l=(2 5 0.5)
for i in {0..2};
do
for j in {0..2};
do
# echo ${t[i]} ${er_t[i]} ${l[j]} ${er_l[j]}
C:/Users/i.makarov.2015/Desktop/matstat/5kurs-stat/venv/Scripts/python.exe main.py ${t[i]} ${er_t[i]} ${l[j]} ${er_l[j]} &
done;
done;
#pause