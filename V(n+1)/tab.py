array=[]
def tab(n): # tabulation
	if n==1 or n==2:
		return 1
	else:
		array.append((tab(tab(n-1)) + tab(n-tab(n-1))))
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
