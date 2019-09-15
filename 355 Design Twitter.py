from heapq import heappush, heappop
'''
355. Design Twitter
https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets,
follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed.
Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.

getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed.
   Each item in the news feed must be posted by users who the user followed or by the user herself.
   Tweets must be ordered from most recent to least recent.
   
follow(followerId, followeeId): Follower follows a followee

unfollow(followerId, followeeId): Follower unfollows a followee.

Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''
class Twitter(object): 
    '''
    !python 2.7
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followings = {} # {follower id: set(followee id)}
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
