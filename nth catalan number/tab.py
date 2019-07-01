def auxiliar_tab(i,n,array,recursive,result):
	if i == n:
		return result
	else:
		result = result + tab(i,array,recursive,result)*tab(n-i-1,array,recursive,result)
		auxiliar_tab(i+1,n,array,recursive,result)
	return result

def tab(n,array,recursive,result):
	if n<=1:
		return 1
	elif recursive==0:
		array.append(auxiliar_tab(0,n,array,1,0))
		recursive=0
	elif recursive==1:
		return array[n]
	return array[-1]


def tab_init():
	array=[]
	array.append(1)
	array.append(1)
	tab(0,array,0,0)
	tab(1,array,0,0)
	tab(2,array,0,0)
	tab(3,array,0,0)
	tab(4,array,0,0)
	tab(5,array,0,0)
	tab(6,array,0,0)
	tab(7,array,0,0)
	tab(8,array,0,0)
	tab(9,array,0,0)
	tab(10,array,0,0)
