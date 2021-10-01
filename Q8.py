from itertools import combinations

n,k,d,m = list(map(int, input().split()))
prediction = list(map(int, input().split()))

def getInvestmentValue(days):
    pred = prediction.copy()
    multiplied = []
    for day in days: # index of the day of the operation
        pred[day]=0
        for i in range(1, d+1):
            if day+i<len(pred) and (day+i not in multiplied):
                pred[day+i]*=m
                multiplied.append(day+i)
    return sum(pred)

operation_days = list(combinations(range(0, n), k))
max_value = 0
for o in operation_days:
    v = getInvestmentValue(o)
    if v>max_value:
        max_value=v

print(max_value)