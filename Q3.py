# TODO DA FARE
import time
n, m, maxSum = list(map(int, input().split()))
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
start_time = time.time()
s = s1+s2
s.sort()
c=0
for i in s:
    maxSum-=i
    c+=1
    if maxSum<=0:
        break
time.sleep(0.1)
print(c)
print(time.time()-start_time-0.1)


# ALTERNATIVE
_input=input
_int=int
_map=map
_list=list
n, m, maxSum = _list(_map(_int, _input().split()))
s1 = _list(_map(_int, _input().split()))
s2 = _list(_map(_int, _input().split()))
count=0
while len(s1)+len(s2)>0:
    c1,c2,c=None,None,None
    if len(s1)>0: c1=s1.pop(0)
    if len(s2)>0: c2=s2.pop(0)
    if c1 is None or c2 is None:
        if c1 is None: c=c2
        else: c=c1
    else:
        c=min([c1,c2])
    maxSum-=c
    count+=1
    if maxSum<=0:
        break
print(count)