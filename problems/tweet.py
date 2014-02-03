
class user(object):
    def __init__ (self,name,gender):
        self.name = name
        self.gender = gender
        self.follow_list = []
        self.follow_dict = {}
        self.tweet_dict = {}
        self.list1 = []
    def follow(self,user):
        self.follow_list.append(user)
    def show_follower(self,user):
        for user1 in self.follow_list:
            self.list1.append(user1.name)
            print 'user name==>',user1.name
            print 'gender==>',user1.gender
        self.follow_dict[user.name] = self.list1
    def do_tweet(self,message,user):
        self.tweet_dict[user.name] = message
    def show_tweet(self,user):
        print user.name,'can watch thease tweet==>'
        for user1,msg in self.tweet_dict.items():   
            if user1 in self.follow_dict.keys() and user.name in self.follow_dict.values()[0]:
                print user1,'==>',msg
            else:
                print user.name, "sorry you have  no  tweet"


user1 = user('Manmohan', 'Male')
user2 = user('Varun', 'Male')
user3 = user('Neeraj', 'Male')
user4 = user('Simaran','Female')
user5 = user('Sakhsi', 'Female')



def main():
    user1.follow(user2)
    print user1.name,'followed by',user2.name
    user1.follow(user3)
    print user1.name,'followed by',user3.name
    user1.follow(user4)
    print user1.name,'followed by',user4.name
    print '\n'
    user5.follow(user1)
    print user5.name,'followed by',user1.name
    user5.follow(user2)
    print user5.name,'followed by',user2.name
    user5.follow(user4)
    print user5.name,'followd by',user4.name
    print '\n'
    print user1.name,'followed by==>'
    user1.show_follower(user1)
    print '\n'
    print user5.name,'following==>'
    user5.show_follower(user5)
    user1.do_tweet('I am in banglore',user1)
    user5.do_tweet('I am lived in kanpur',user5)
    user1.show_tweet(user2)
    user1.show_tweet(user3)
    user1.show_tweet(user4)
    user1.show_tweet(user5)
    user5.show_tweet(user1)
    user5.show_tweet(user2)
    user5.show_tweet(user3)
    user5.show_tweet(user4)



if __name__ == '__main__':
    main()
