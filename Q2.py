t = int
i = input
money = t(i())
input_prices = list(map(t, i().split()))
ordered_prices = input_prices.copy()
ordered_prices.sort()
count=0
for price in ordered_prices:
    k = input_prices.index(price)+1
    kp = money//price
    k = kp if kp<=k else k
    count+=k
    money-=price*k
print(count)