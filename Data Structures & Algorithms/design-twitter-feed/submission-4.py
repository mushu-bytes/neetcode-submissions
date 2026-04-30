class Twitter:

    def __init__(self):
        self.users = defaultdict(set) # userid: set(followerid)
        self.tweets = defaultdict(list) # userid: list(tweets)
        self.tweetOrder = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.tweetOrder, tweetId])
        self.tweetOrder -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.users[userId].add(userId)
        maxHeap = []
        for follower in self.users[userId]:
            if follower in self.tweets:
                index = len(self.tweets[follower]) - 1
                order, tweetId = self.tweets[follower][index]
                heapq.heappush(maxHeap, [order, tweetId, index - 1, follower])
            
        heapq.heapify(maxHeap)
        feed = []
        while maxHeap and len(feed) < 10:
            order, tweetId, index, follower = heapq.heappop(maxHeap)
            feed.append(tweetId)
            if index >= 0:
                order, tweetId = self.tweets[follower][index]
                heapq.heappush(maxHeap, [order, tweetId, index - 1, follower])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

