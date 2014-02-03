def myfunction():
	num=0
        for i in range(2,600000):
                count =0
                for m in range(1,(i/2)+1):
                        if(i%m==0):
                                count=count+1
                if(count==1):
                        print i,
			num=num+1
		if(num==10001):
			print i 
			break
if __name__=='__main__':
        myfunction() 
