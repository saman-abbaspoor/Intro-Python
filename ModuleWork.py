from math import cos as cosine
from math import sin as sine

def cal(X,Y):
    C=cosine(X)
    S=sine(Y)
    print('The Cosine is:', C, ', and the Sine is:', S)
    return C,S


[Co, Si]=cal(0,90)

print(Co,Si)
