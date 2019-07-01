def mem(n,cache): # memoization
	if n == 1:
		return 1
	elif n in cache:
		return cache[n]
	else:
		cache[n] = 1+mem(n-mem(mem(n-1,cache),cache),cache)
	return cache.values()[-1]

def mem_init():
	cache={}
	cache[0]=1
	mem(1,cache)
	mem(2,cache)
	mem(3,cache)
	mem(4,cache)
	mem(5,cache)
	mem(6,cache)
	mem(7,cache)
	mem(8,cache)
	mem(9,cache)
	mem(10,cache)
	mem(11,cache)
	mem(12,cache)
	mem(13,cache)
	mem(14,cache)
	mem(15,cache)
	mem(16,cache)
	mem(17,cache)
	mem(18,cache)
	mem(19,cache)
	mem(20,cache)
