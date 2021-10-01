from itertools import combinations
from math import floor, sqrt

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def prod(list):
    r=1
    for l in list:
        r*=l
    return r

n = int(input())
brokers = list(map(int, input().split()))

c=0

def split(l):
    new_list = []
    for i in range(0, len(l)//2+1):
        combs = set(combinations(l,i))
        for c in combs:
            new_list.append((sorted(list(c)), sorted(list(l-set(c)))))
    return new_list

spl = split(set(brokers))[1:]

for s in spl:
    if gcd(prod(s[0]), prod(s[1]))==1:
        c+=1

if c==0:
    print("NO\n0")
else:
    print("YES\n"+str(c*2))