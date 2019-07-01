def tab(m,n,array): # tabulation
	if m==0 or n == 0:
		return 1
	else:
		array.append(tab(m-1,n,array) + tab(m-1,n-1,array) + tab(m,n-1,array))
	return array[-1]

def tab_init():
	tab(0,0,[])
	tab(0,1,[])
	tab(0,2,[])
	tab(0,3,[])
	tab(1,0,[])
	tab(1,1,[])
	tab(1,2,[])
	tab(1,3,[])
	tab(2,0,[])
	tab(2,1,[])
	tab(2,2,[])
	tab(2,3,[])
	tab(3,0,[])
	tab(3,1,[])
	tab(3,2,[])
	tab(3,3,[])
