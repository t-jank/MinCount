import random
import matplotlib.pyplot as plt
import math
import hashlib

######## zadanie 1 #########

def MinCount(k,h,multizbior):
    M=[]
    for i in range(0,k):
        M.append(1)
    for x in range(0,len(multizbior)):
        if h(x) < M[k-1] and h(x) not in M:
            M[k-1]=h(x)
            M.sort()
    if M[k-1]==1:
        i=k
        while M[i-1]==1 and i>0:
            i-=1
        nzd = M[i-1]
        return nzd
    else:
        nzd = (k-1)/M[k-1]
        return nzd

def randsid(x):
    random.seed(x)
    return random.random()


def md5(x):
    return int(hashlib.md5(str(x).encode()).hexdigest(),16)/2**128

def sha256(x):
    return int(hashlib.sha256(str(x).encode()).hexdigest(),16)/2**256


k=100
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
zakres=1000
while len(multizbior)<zakres:
    for j in range(0,len(multizbior)):
        multizbior[j] = multizbior[j] + q
    multizbior.append(multizbior[len(multizbior)-1]+1)
    q+=1
    #print('n =',len(multizbior),'nzd:',MinCount(k,randsid,multizbior))
    wynik = MinCount(k,sha256,multizbior)/len(multizbior)
    if j>k and abs(wynik-1)<0.1:
        gut+=1
    elif j>k and abs(wynik-1)>=0.1:
        bad+=1
    plt.scatter(len(multizbior),wynik, color='k', marker='.')
print('k =',k,'; Procent przypadkow |nzd/n -1|<10%:',gut/(bad+gut) *100,'%')
plt.xlim([k,zakres])
plt.ylim(0.6,1.4)
plt.xlabel('n')
plt.ylabel('nzd/n')
plt.show()
