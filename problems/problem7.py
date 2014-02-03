def myfunction():
	for i in range(2,36):
		print i
		count =0
		for m in range(1,i/2):
			if(i/m==0):
				count=count+1
		if(count==1):
			print i
			
if __name__=='__main__':
	myfunction() 
