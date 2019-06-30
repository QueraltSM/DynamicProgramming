array=[]
result = 0
recursive=0
array.append(0)
array.append(0)

def auxiliar_tab(i,n):
	global recursive
	global result

	recursive=1

	if i==n:
		return result
	else:
		result = max(result,max(i*(n-i),tab(n-i)*i))
		auxiliar_tab(i+1,n)
	return result

def tab(n): # tabulation
	global recursive
	global result

	if n==0 or n==1:
		return 0
	elif recursive==0:
		array.append(auxiliar_tab(1,n))
		recursive=0
		result=0
	elif recursive==1:
		return array[n]
	return array[-1]

def tab_init():
	tab(1)
	tab(2)
	tab(3)
	tab(4)
	tab(5)
	tab(6)
	tab(7)
	tab(8)
	tab(9)
	tab(10)
	tab(11)
	tab(12)
	tab(13)
	tab(14)
	tab(15)
	tab(16)
	tab(17)
	tab(18)
	tab(19)
	tab(20)
