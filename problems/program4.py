def myfunction():
	list=[]
	list1=[]
	for i in range(100,999):
		for j in range(100,999):
			c=str(i*j)
			b=c[::-1]
			if(c==b):
				list.append(c)
	print list
	l=len(list)
	for i in range(l):
		p=int(list[i])
		list1.append(p)
	m=max(list1)
	print m
		


if __name__=='__main__':
	myfunction()
