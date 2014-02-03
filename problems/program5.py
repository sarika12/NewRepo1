def myfunction():
	count =0
	for n in range(360360,99999999):
		m=n
		count=0
		for i in range(1,21):
			if(m%i==0):
				count=count+1
		
		if(count==20):
			print n
			break

if __name__=='__main__':
	myfunction()

