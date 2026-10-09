class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        result = []
        users = []

        users.append(userId)
        if userId in self.following:
            for followee in self.following[userId]:
                users.append(followee)
        
        for user in users:
            if user in self.tweets:
                for time, tweetId in self.tweets[user]:
                    heapq.heappush(heap, [-time, tweetId])
        
        while heap and len(result) < 10:
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)