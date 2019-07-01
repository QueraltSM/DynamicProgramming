def auxiliar_mem(i,n,cache,result):
	if i==n:
		return result
	else:
		result = max(result,max(i*(n-i),mem(n-i,cache,result)*i))
		auxiliar_mem(i+1,n,cache,result)
	return result

def mem(n,cache,result): # memoization
	if n==0 or n==1:
		return 0
	elif n in cache:
		return cache[n]
	else:
		cache[n] = auxiliar_mem(1,n,cache,0)
	return cache.values()[-1]

def mem_init():
	cache={}
	cache[0]=0
	cache[1]=0
	mem(1,{},0)
	mem(2,{},0)
	mem(3,{},0)
	mem(4,{},0)
	mem(5,{},0)
	mem(6,{},0)
	mem(7,{},0)
	mem(8,{},0)
	mem(9,{},0)
	mem(10,{},0)
