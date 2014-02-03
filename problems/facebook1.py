class myclass:
	member={'neeraj':'12345','kumar':'6789','manmohan':'77777'}
	list1=[]
	def __init__(self,name,passw):
		self.uname=name
		self.upass=passw
		self.nuser=''
		self.a=''
		self.user()
	def user(self):
		
		if self.uname in self.member.keys() and self.upass in self.member.values() :
			print "welcome to user"
			self.getrequest()
		else:
			print "enter correct user name and password"
	

	def getrequest(self):
		request=raw_input("do you want to know user name in facebook press=Y=>")
		if request == 'y':
			print self.member.keys()
			self.nuser=raw_input("which user you want to send request=>")
		if self.nuser in self.member:
			print 'your request send successfully', self.nuser
			self.addfriend_request()			


		else:
			print 'no such type of user'
		
	def addfriend_request(self):
		self.a=raw_input("do you want to accept friend request press y=>")
		if self.a=='y':
			self.list1.append(self.nuser)
			self.showfriend()
			'''print self.list1'''
		else :
			print "friend request is discard"
	def showfriend(self):
		b=raw_input("do you want to show friend press y=>")

		if b=='y':
			print 'these are some user',self.list1
							
