array=[]
result=0
recursive=0
array.append(1)
array.append(1)

def auxiliar_tab(i,n):
	global result
	global recursive
	if recursive==0:
		result=0
		recursive=1
	if i == n:
		return result
	else:
		result = result + tab(i)*tab(n-i-1)
		auxiliar_tab(i+1,n)
	return result

def tab(n):
	global recursive
	if n<=1:
		return 1
	elif recursive==0:
		array.append(auxiliar_tab(0,n))
		recursive=0
	elif recursive==1:
		return array[n]
	return array[-1]


def tab_init():
	tab(0)
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
