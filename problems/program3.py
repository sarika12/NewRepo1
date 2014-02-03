

'''this is my program'''
def  myfunction():
	n=600852345
	list=[]
	list1=[]
	for m in xrange(2,n):
		count=0
		for i in xrange(1,m):
			if(m%i == 0):
				count=count+1
		if(count == 1):
			list.append(m)
	print list
	a=len(list)
	print a
	print list[a-1]

if __name__=='__main__':
	myfunction()	 
