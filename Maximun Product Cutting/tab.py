def auxiliar_tab(i,n,array,recursive,result):
	if i==n:
		return result
	else:
		result = max(result,max(i*(n-i),tab(n-i,array,recursive,result)*i))
		auxiliar_tab(i+1,n,array,recursive,result)
	return result

def tab(n,array,recursive,result): # tabulation
	if n==0 or n==1:
		return 0
	elif recursive==0:
		array.append(auxiliar_tab(1,n,array,1,0))
		recursive=0
	elif recursive==1:
		return array[n]
	return array[-1]

def tab_init():
	array=[]
	array.append(0)
	array.append(0)
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
	tab(11,array,0,0)
	tab(12,array,0,0)
	tab(13,array,0,0)
	tab(14,array,0,0)
	tab(15,array,0,0)
	tab(16,array,0,0)
	tab(17,array,0,0)
	tab(18,array,0,0)
	tab(19,array,0,0)
	tab(20,array,0,0)
