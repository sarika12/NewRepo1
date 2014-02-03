def my_main():
	sum=0
	for i in range(2,2000000):
		count=0
		k=i
		for j in range(1,(k/2)+1):
			if(k%j==0):
				count=count+1
			if(count==2):
				break
		if(count==1):
			sum=sum+i
			print sum


if __name__=='__main__':
	my_main()
