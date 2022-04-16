import random
import matplotlib.pyplot as plt
import math
import hashlib
import numpy as np

######## zadanie 5 #########

def MinCount(k,h,multizbior):
    M=[]
    for i in range(0,k):
        M.append(1)
    for x in range(0,len(multizbior)):
        if h(multizbior[x]) < M[k-1] and h(multizbior[x]) not in M:
            M[k-1]=h(multizbior[x])
            M.sort()
    if M[k-1]==1:
        i=k
        while M[i-1]==1 and i>0:
            i-=1
        nzd = i
        return nzd
    else:
        nzd = (k-1)/M[k-1]
        return nzd

def randsid(x):
    random.seed(x)
    return random.random()


######## zadanie 6 #########

def md5(x):
    return int(hashlib.md5(str(x).encode()).hexdigest(),16)/2**128

def sha256(x):
    return int(hashlib.sha256(str(x).encode()).hexdigest(),16)/2**256

def randsid8192(x):
    random.seed(x)
    return random.randrange(1000000)%8192/8192

'''
e=1
multizbior=[]
for j in range(1,10000): # mozna tez bez usuwania tylko dodajac wszedzie 1, +1 wyraz
    for q in range(e,e+j):
        multizbior.append(q)    
    MinCount(k,randsid,multizbior)
    multizbior.clear()
    e=e+j
'''
multizbior=[1]
#print('n =',len(multizbior),'nzd:',MinCount(100,randsid,multizbior))
q=1
gut=0
bad=0
var=0
k=200
zakres=10000
alfa = 0.05
ilepoza=alfa*zakres
tabpoza=[]
for u in range (0,int(ilepoza)+1):
    tabpoza.append(-1)
while len(multizbior)<zakres:
    for j in range(0,len(multizbior)):
        multizbior[j] = multizbior[j] + q
    multizbior.append(multizbior[len(multizbior)-1]+1)
    q+=1
   # print('n =',len(multizbior),'nzd:',MinCount(k,randsid,multizbior))
    wynik = MinCount(k,randsid,multizbior)/len(multizbior)
    #do 7 rzeczywistego:
    if abs(wynik-1)>tabpoza[0]:
        tabpoza[0]=abs(wynik-1)
        tabpoza.sort()
    # zliczanie do 5c:    
    #if abs(wynik-1)<0.1:
    #    gut+=1
    #elif abs(wynik-1)>=0.1:
    #    bad+=1
    #wariancja do 7:
    var += (wynik-1)**2
    plt.scatter(len(multizbior),wynik, color='k', marker='.')
#print('k =',k,'; Procent przypadkow |nzd/n -1|<10%:',gut/(bad+gut) *100,'%')
plt.xlim([0,zakres])
plt.xlabel('n')
plt.ylabel('nzd/n')
#plt.ylim(0,1.8)


######## zadanie 7 #########

#Czebyszew:
delta = math.sqrt(var/zakres/alfa)
print('Czebyszew:  Pr[',round(1-delta,2),'< nzd/n <',round(1+delta,2),'] >',1-alfa)
x = np.linspace(0,zakres)
y = 0*x+1+delta
plt.plot(x, y, 'b', label='Czebyszew')
y = 0*x+1-delta
plt.plot(x, y, 'b')

#Rzeczywistosc:
deltarzecz=tabpoza[0]
print('Rzeczywistosc:  Pr[',round(1-deltarzecz,2),'< nzd/n <',round(1+deltarzecz,2),'] >',1-alfa)
y = 0*x+1+deltarzecz
plt.plot(x, y, 'r', label='Rzeczywistosc')
y = 0*x+1-deltarzecz
plt.plot(x, y, 'r')

#Chernoff:
if alfa == 0.05:
    deltachern = 0.195699938834368
elif alfa == 0.01:
    deltachern = 0.249265657097999
elif alfa == 0.005:
    deltachern = 0.560002658800619 # z wolframa:
# e^(200*delta/(1+delta))*(1-(delta/(1+delta)))^200 + e^(-delta*200/(delta-1))*(1-(-delta/(delta-1)))^200 = 0.05
print('Chernoff:  Pr[',round(1-deltachern,2),'< nzd/n <',round(1+deltachern,2),'] >',1-alfa)
y = 0*x+1+deltachern
plt.plot(x, y, 'g', label='Chernoff')
y = 0*x+1-deltachern
plt.plot(x, y, 'g')

plt.legend(loc=4)
plt.show()
