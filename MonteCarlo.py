import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import random
#print(random.__doc__)
#print(random.uniform.__doc__)

N = 1000
a = 0
b = 5

#paseido-gadijumi skaitlu generatora grauds 

x = random.uniform(a,b,N)

'''

random.seed(1)

x = random.uniform(a,b,N)

k = [0,0,0,0,0]
for i in range(N):
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] <2:
        k[1] =k[1] + 1
    elif x[i] <3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1
    else:
        k[4] = k[4] + 1
print(k)
'''

y = random.uniform(a,b,N)
from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('aaaaaa')
#plt.plot(x,y, 'ko')
#plt.show()
N1=0
for i in range (N):
    if y[i] < x[i]:
        plt.plot(x[i],y[i],'go')
    else:
        plt.plot(x[i],y[i],'ko')
S_zinamais = (b-a) * (b-a)
S_nezinamais = 1. * S_zinamais *N1/N
print (S_nezinamais)
plt.show()
    
        
