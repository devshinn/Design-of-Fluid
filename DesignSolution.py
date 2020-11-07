#!/usr/bin/env python
# coding: utf-8
import pickle
from pylab import log10, pi, sqrt
import random
file = open('table_data.bin','rb'); table = pickle.load(file);file.close()

chen_f = lambda Ree,jdd: (-2.0*log10(jdd/3.7065 - 5.0452/Ree * log10((jdd**1.1098)/2.8257 +5.8506/(Ree**0.8981))))**-2 #Re>2100일경우

minor_loss = {'edged inlet':0.5,'Re-entrant inlet': 1, 'Well rounded inlet':0.05, 'Exit':1, '90º Elbow':0.22,'45º Elbow':0.17,'Globe valve':10,'Gate valve':0.15,'Basket strainer':1.3}

# -------------------------------- 압력차 ---------------------------------------------
def Pressure_drop(Q, L, dz,liquid_type, pipe_standard, merterial, loss):
    k = 0
    if len(loss)==1:
        k = int(loss[0])
    else:
        for i in range(len(loss)):
            if loss[i]== 0:
                pass
            else:
                k += minor_loss[loss[i][0]]*loss[i][1]


    mu= table[1][liquid_type];   
    rho=table[0][liquid_type];    
    D= table[2][pipe_standard];     
    ep= table[3][merterial];     
    A = (pi*D**2)/4
    V=(Q)/A
    jd = ep/D
    Re = rho*V*D/mu

    
    if Re <=2100: #충류일경우 f = 64/Re, 아닐 경우 chen식 사용
        f = 64/Re
        dp = ((rho*V**2)/2) * (f*L/D + k) - dz/(rho*9.81)
    else:
        f = chen_f(Re,jd)
        dp = ((rho*V**2)/2)*(f*L/D + k) - dz/(rho*9.81)
        dp = dp*10**-3
    print(f'A:{A}, V: {V}, rho{rho}, mu: {mu},  D: {D}, jd: {jd}, K: {k}, Re:{Re}, f: {f}')

    return dp

#--------------------------------유량------------------------

def Flow_rate(dp, L, dz, liquid_type, pipe_standard, merterial, loss):
    k = 0
    if len(loss)==1:
        k = int(loss[0])
    else:
        for i in range(len(loss)):
            if loss[i]== 0:
                pass
            else:
                k += minor_loss[loss[i][0]]*loss[i][1]
            
    mu= table[1][liquid_type];   rho=table[0][liquid_type];    D= table[2][pipe_standard];     ep= table[3][merterial];     A = (pi*D**2)/4 ;    jd = ep/D
    

    f = random.uniform(0.007, 0.05); es = 1;af = 10; V=1
    while es>0.000001:
        v1 = 2*dp/rho
        v2 = 2*dz*9.81;
        v3 = (f*L/D) + k
        V = sqrt((v1+v2)/v3)
        Re = rho*V*D/mu
        f = chen_f(Re,jd)
        es = abs(af-f)
        af= f

        print(V)
        Re = Re = rho*V*D/mu
    if Re <=2100: #충류일경우 f = 64/Re
        f = 64/Re
        v1 = 2*dp/rho
        v2 = 2*dz*9.81;
        v3 = (f*L/D) + k
        V = sqrt((v1+v2)/v3)
    Flow = (A*V)
    return Flow


# --------------------------------------------------------지름----------------------------------
def Pipe_diameter(dp,Q, L, dz, liquid_type, merterial, loss):
    k = 0
    if len(loss)==1:
        k = int(loss[0])
    else:
        for i in range(len(loss)):
            if loss[i]== 0:
                pass
            else:
                k += minor_loss[loss[i][0]]*loss[i][1]


    mu= table[1][liquid_type];   rho=table[0][liquid_type];  ep= table[3][merterial];

    D = random.uniform(0.001, 0.2); es = 10; af = 10
    while es>0.0001:
        A = (pi*D**2)/4; V=Q/A;  jd = ep/D
        Re = rho*V*D/mu; 
        f = chen_f(Re,jd)
        es = abs(af-f)
        af= f
        D = (((dp/(rho*9.81) + dz)*((9.81+9.81)/V**2) - k)/(f*L))**-1

    if Re <=2100: #충류일경우 f = 64/Re
        A = (pi*D**2)/4; V=Q/A;  jd = ep/D
        Re = rho*V*D/mu; 
        f = 64/Re
        D = (((dp/(rho*9.81) + dz)*((9.81+9.81)/V**2) - k)/(f*L))**-1

    return D




