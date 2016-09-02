from random import randint

def odd(n):
	return n % 2

allNums = []
for eachNum in range(9):
	allNums.append(randint(1, 99))

print allNums
#print filter(lambda n: n % 2, allNums)
print [n for n in allNums if n % 2]
