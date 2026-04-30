class Twitter:

    def __init__(self):
        self.users = defaultdict(set) # userid: set(followerid)
        self.tweets = defaultdict(list) # userid: list(tweets)
        self.orderToId = {}
        self.tweetOrder = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(self.tweetOrder)
        self.orderToId[self.tweetOrder] = tweetId
        self.tweetOrder -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = self.tweets[userId].copy()
        for follower in self.users[userId]:
            if follower == userId:
                continue
            maxHeap.extend(self.tweets[follower])
            
        heapq.heapify(maxHeap)
        feed = []
        while maxHeap and len(feed) < 10:
            tweet = self.orderToId[heapq.heappop(maxHeap)]
            feed.append(tweet)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

"""
This is all about datastructures. Let's reduce the problem
to requirements:

1. Each User should be able to post tweets
2. Each User should have a feed, containing their tweets
and the people they follow tweets
3. Each user should be able to follow and unfollow others

The hardest part will definitely be the feed. How do we form
the feed? One naiive implementation is to get the user's followers
append each of the the tweets that the users have into a single
list, heapify, and then pop 10 times

I wonder if there is a more clever way to generate the feed.

Iteration 1:
{ userid: [ tweet id, ... ] }
posting a tweet would just be adding a tweet to the list
perhaps the tweets are in order

{ userid: set([followerId, ... ]) }
each user should have a list of who they follow. By default
that includes themselves.
Following / Unfollowing means removal / adding to that set

Get newsfeed involves constructing a new list of each
user's tweets (of which they follow) and then running
heapify. After heapify, you can pop 10 times, at most.

"""