from heapq import heappush, heappop
'''
355. Design Twitter
https://leetcode.com/problems/design-twitter/
'''
class Twitter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followings = {} # {userId : set(userId)}
        self.tweets = {} # {userId : [(timestamp, tweetId)]}
        self.timestamp = int("0xffffffff",16)
    
    def postTweet(self,userId,tweetId):
        ts = self.tweets.get(userId,[])
        self.timestamp -= 1 
        ts.append((self.timestamp,tweetId))
        self.tweets[userId] = ts

    def getNewsFeed(self, userId):
        followees = self.followings.get(userId,set())
        followees.add(userId) # follow self
        
        tweets = self.tweets
        res = []
        heap = [] # [(timestamp, index of tweet, tweet list)]
        for f in followees:
            ts = tweets.get(f,[])
            if len(ts) > 0:                 
                heappush(heap,(ts[-1][0], len(ts)-1, ts))

        while len(res) < 10 and len(heap) > 0:
            _,i,ts = heappop(heap)
            res.append(ts[i][1])
            if i > 0:
                heappush(heap,(ts[i-1][0],i-1,ts))
        return res
    
    def follow(self, followerId, followeeId):
        fs = self.followings.get(followerId,set())
        fs.add(followeeId)
        self.followings[followerId] = fs

    def unfollow(self, followerId, followeeId):
        if followerId in self.followings:
            self.followings[followerId].discard(followeeId)

obj = Twitter()
for i in xrange(0,100):
    obj.postTweet(1,-i)
    obj.postTweet(2,-i*10)

print obj.getNewsFeed(1)
print obj.getNewsFeed(2)

obj.follow(1,2)
print obj.getNewsFeed(1)
print obj.getNewsFeed(2)

obj.unfollow(1,2)
print obj.getNewsFeed(1)
print obj.getNewsFeed(2)
