cache={}
def mem(n): # tabulation
	if n == 1 or n==2:
		return 1
	elif n in cache:
		return cache[n]
	else:
		cache[n] = (mem(mem(n-1)) + mem(n-mem(n-1)))
	return cache.values()[-1]

def mem_init():
	mem(1)
	mem(2)
	mem(3)
	mem(4)
	mem(5)
	mem(6)
	mem(7)
	mem(8)
	mem(9)
	mem(10)
	mem(11)
	mem(12)
	mem(13)
	mem(14)
	mem(15)
	mem(16)
	mem(17)
	mem(18)
	mem(19)
	mem(20)
