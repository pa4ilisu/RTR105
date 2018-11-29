#print(vars())

def mana_funkcija(x):
    return sin(x)
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace
from matplotlib import pyplot as plt

x = linspace (0,4,11)
#print(vars())
y = mana_funkcija(x)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcija un tas atvasinajumi')
plt.plot(x,y)
plt.plot(x,y,'ro')
#plt.legend(['funkcija ar starpveribam','funkcijas dazas veribas'])
#plt.show()

# atvasinajumu apreikins, izmantojot funkciajs apreikinu
N = len(x)
delta_x = x[1] - x[0]
derivative = []
print(derivative)
for i in range(N):
    temp = (mana_funkcija (x[i] + delta_x)- mana_funkcija(x[i])) / delta_x
    derivative.append(temp)
    print(derivative)

plt.plot(x,derivative)
plt.plot(x,derivative,'go')
legend = []

legend.append('funkcija ar starpvertibam')
legend.append('funkcija ar dazam vertibam')
legend.append('atvasinajums ar starpvetibam')
legend.append('atvasinajums dazas vertibas')

#plt.legend(legend)
#plt.show()

#atvasinajums caur masivu 
derivative_through_array = []
for i in range(N - 1):
    temp = (y[i+1]- y[i]) / (x[i+1] - x[i])
    derivative_through_array.append(temp)
plt.plot(x[0:N-1],derivative_through_array)
plt.plot(x[0:N-1],derivative_through_array, 'bo')

legend.append('atvasinajums ar starpvetibam(apreikins ar masiv avertibas)')
legend.append('atvasinajums dazas vertibas(apreikins ar masiv avertibas)')

#plt.legend(legend)
plt.legend(legend, loc=3)
plt.show()
         
    

