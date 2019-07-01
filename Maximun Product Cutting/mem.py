def auxiliar_mem(i,n,cache,recursive,result):
	recursive=1
	if i==n:
		return result
	else:
		result = max(result,max(i*(n-i),mem(n-i,cache,recursive,result)*i))
		auxiliar_mem(i+1,n,cache,recursive,result)
	return result

def mem(n,cache,recursive,result): # memoization
	if n==0 or n==1:
		return 0
	elif n in cache:
		return cache[n]
	else:
		cache[n] = auxiliar_mem(1,n,cache,recursive,result)
		result=0
	return cache.values()[-1]

def mem_init():
	cache={}
	cache[0]=0
	cache[1]=0
	mem(0,cache,0,0)
	mem(1,cache,0,0)
	mem(2,cache,0,0)
	mem(3,cache,0,0)
	mem(4,cache,0,0)
	mem(5,cache,0,0)
	mem(6,cache,0,0)
	mem(7,cache,0,0)
	mem(8,cache,0,0)
	mem(9,cache,0,0)
	mem(10,cache,0,0)
