cache={}
result=0
recursive=0
cache[0]=0
cache[1]=0

print "jaja"
def auxiliar_mem(i,n):
	global recursive
	global result

	recursive=1

	if i==n:
		return result
	else:
		result = max(result,max(i*(n-i),mem(n-i)*i))
		auxiliar_mem(i+1,n)
	return result

def mem(n): # tabulation
	global recursive
	global result

	if n==0 or n==1:
		return 0
	elif n in cache:
		return cache[n]
	else:
		cache[n] = auxiliar_mem(1,n)
		result=0
	return cache.values()[-1]

print "hola"
