n = int(input())
prices = list(map(int, input().split()))
c=0
for i in range(n):
    for j in range(n):
        if j<=i: continue
        d = j-i
        if d==1:
            c+=1
        elif all((prices[k]<prices[i] and prices[k]<prices[j]) for k in range(i+1, j)):
            c+=1
print(c)