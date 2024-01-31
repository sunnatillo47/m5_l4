son = int(input())

c = 0
for n in range(son):
	for i in range(n, son+1):
		if n + i == son:
			c += 1

print(c)