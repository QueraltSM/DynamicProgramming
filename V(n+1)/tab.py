def tab(n,array): # tabulation
	if n==1:
		return 1
	else:
		array.append(1+tab(n-tab(tab(n-1,array),array),array))
	return array[-1]

def tab_init():
	array=[]
	array.append(1)
	tab(1,array)
	tab(2,array)
	tab(3,array)
	tab(4,array)
	tab(5,array)
	tab(6,array)
	tab(7,array)
	tab(8,array)
	tab(9,array)
	tab(10,array)
	tab(11,array)
	tab(12,array)
	tab(13,array)
	tab(14,array)
	tab(15,array)
	tab(16,array)
	tab(17,array)
	tab(18,array)
	tab(19,array)
	tab(20,array)
