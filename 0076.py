arr = [int(n) for n in input().split()]
priz_price = int(input())
c = 0
for n in arr:
	if n > 1000:
		c += 1

if c == 0:
	if priz_price - sum(arr) > 0:
		print(priz_price - sum(arr))