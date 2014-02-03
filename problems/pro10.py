def my_main():
	sum=0	
	for i in range(2,2000000):
		flag=1
		for j in range(2,int(i**0.5)+1):
			if(i%j==0):
				flag=0
				break
		if(flag==1):
			sum=sum+i
			print sum



if __name__=='__main__':
	my_main()
