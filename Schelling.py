#The following code portraits the Schelling's Segregation Model

import matplotlib.pyplot as plt
import numpy as np
import random

#Creation of Home
class Home:
    def __init__(self, col):
        self.col=col
        
city=np.array([Home('ks') for i in range(100)], dtype=object).reshape((10,10)) #Determining Size of the Array
occ=np.zeros((80), dtype=np.int) #Number of initial occupied homes
empt=np.zeros((20), dtype=np.int) #Number of initial empty homes
i=0
j=0

while j<80:
    while i<40:
        a=random.randint(0,99)
        x=a%10
        y=a//10
        if city[x,y].col=='ks':
            city[x,y].col='rs'
            occ[j]=a
            i=i+1
            j=j+1
    i=0
    while i<40:
        a=random.randint(0,99)
        x=a%10
        y=a//10
        if city[x,y].col=='ks':
            city[x,y].col='gs'
            occ[j]=a
            i=i+1
            j=j+1
k=0            
j=0
while j<100:
    x = j%10
    y = j//10
    if city[x,y].col=='ks':
           empt[k]=j
           k=k+1
    j=j+1
    
def count(i,j,h):
    gcol=1
    rcol=1
        
    if i+1<10:
        if h[i+1,j].col=='gs':
            gcol=gcol+1
        if h[i+1,j].col=='rs':
            rcol=rcol+1
                        
        if j+1<10:
            if h[i+1,j+1].col=='gs':
                gcol=gcol+1
            if h[i+1,j+1].col=='rs':
                rcol=rcol+1
                            
        if j-1>=0:
            if h[i+1,j-1].col=='gs':
                gcol=gcol+1
            if h[i+1,j-1].col=='rs':
                rcol=rcol+1
                                                  
    if i-1>=0:
        if h[i-1,j].col=='gs':
            gcol=gcol+1
        if h[i-1,j].col=='rs':
            rcol=rcol+1
                       
        if j+1<10:
            if h[i-1,j+1].col=='gs':
                gcol=gcol+1
            if h[i-1,j+1].col=='rs':
                rcol=rcol+1
                           
        if j-1>=0:
            if h[i-1,j-1].col=='gs':
                gcol=gcol+1
            if h[i-1,j-1].col=='rs':
                rcol=rcol+1
                                              
    if j+1<10:
        if h[i,j+1].col=='gs':
            gcol=gcol+1
        if h[i,j+1].col=='rs':
            rcol=rcol+1
                                    
    if j-1>=0:
        if h[i,j-1].col=='gs':
            gcol=gcol+1
        if h[i,j-1].col=='rs':
            rcol=rcol+1
    return(gcol,rcol)

def happ(i1,j1,i2,j2,city):
    h=city
    (gcol1,rcol1)=count(i1,j1,city)
    (gcol2,rcol2)=count(i2,j2,city)
    if h[i2,j2].col=='gs':
        fracself1=gcol1/rcol1
        fracself2=gcol2/rcol2
    else:
        fracself1=rcol1/gcol1
        fracself2=rcol2/gcol2
    
    if (fracself1 > 0.5):
        utilityin = 1.5 - fracself1
    else:
        utilityin = 2 * fracself1
    if (fracself2 > 0.5):
        utilityout = 1.5 - fracself2
    else:
        utilityout = 2 * fracself2
    return(utilityin,utilityout)

def move(lempt,locc, utilityin,utilityout,city,occ,empt):
    x1=(empt[lempt])%10
    y1=(empt[lempt])//10
    x2=(occ[locc])%10
    y2=(occ[locc])//10
    count=0
    if utilityin>utilityout:
        n=empt[lempt]
        empt[lempt]=occ[locc]
        occ[locc]=n
        p=city[x1,y1]
        city[x1,y1]=city[x2,y2]
        city[x2,y2]=p
        count=1
    return(count)

plt.axis
fig,ax=plt.subplots()
plt.ion
while i<100:
    lempt=random.randint(0,19)
    locc=random.randint(0,79)
    x1=(empt[lempt])%10
    y1=(empt[lempt])//10
    x2=(occ[locc])%10
    y2=(occ[locc])//10
    (uin,uout)=happ(x1,y1,x2,y2,city)
    n=move(lempt,locc, uin,uout,city,occ,empt)
    if n==1:
        i=i+1
        k=0
        j=0
        for j in range(10):
            for k in range(10):
                ax.plot([j], [k], city[j,k].col,markersize=13)
        plt.show
        plt.pause(0.001)

