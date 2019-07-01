cache={}
def mem(m,n,cache): # memoization
	if m==0 or n == 0:
		return 1
	if cache.get((m,n)) is not None:
		return cache[m,n]
	else:
		cache[m,n] = (mem(m-1,n,cache) + mem(m-1,n-1,cache) + mem(m,n-1,cache))
	return cache[m,n]

def mem_init():
	mem(0,0,{})
	mem(0,1,{})
	mem(0,2,{})
	mem(0,3,{})
	mem(1,0,{})
	mem(1,1,{})
	mem(1,2,{})
	mem(1,3,{})
	mem(2,0,{})
	mem(2,1,{})
	mem(2,2,{})
	mem(2,3,{})
	mem(3,0,{})
	mem(3,1,{})
	mem(3,2,{})
	mem(3,3,{})
