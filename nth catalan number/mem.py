cache={}
result=0
recursive=0

def auxiliar_mem(i,n):
	global result
	global recursive
	if recursive==0:
		result=0
		recursive=1
	if i == n:
		return result
	else:
		result = result + mem(i)*mem(n-i-1)
		auxiliar_mem(i+1,n)
	return result


def mem(n): #memoization
	global recursive
	if n<=1:
		return 1
	elif n in cache:
		return cache[n]
	elif recursive==0:
		cache[n] = auxiliar_mem(0,n)
		recursive=0
	return cache.values()[-1]

def mem_init():
	mem(0)
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
