"""
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，
能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 
    检索最近的十条推文。
    每个推文都必须是由此用户关注的人或者是用户自己发出的。
    推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户

"""


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users_id = set()      # 用户
        self.tweets_id = list()    # 推文
        self.users_follow = {}    # key: user_id follow: [user_id]
        self.tweets_dict = {}   # key: tweet_id author: user_id

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.checkMenber(userId)
        self.tweets_id.append(tweetId)
        self.tweets_dict[tweetId] = userId  # author

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if self.checkMenber(userId):
            count = 0
            News = []
            for tweet in self.tweets_id[::-1]:
                author = self.tweets_dict[tweet]
                # 是自己或关注对象的推文
                if author == userId or author in self.users_follow[userId]:
                    News.append(tweet)
                    count += 1
                if count == 10:
                    break
            return News
        else:
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.checkMenber(followerId)
        self.checkMenber(followeeId)
        self.users_follow[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if self.checkMenber(followerId):
            try:
                self.users_follow[followerId].remove(followeeId)
            except:
                pass

    def checkMenber(self, userId):
        """
        检查是否有该用户，无则添加
        """
        if userId not in self.users_id:
            self.users_id.add(userId)
            self.users_follow[userId] = []  # follow, post
            return False
        return True


if __name__ == "__main__":
    # Your Twitter object will be instantiated and called as such:
    obj = Twitter()
    obj.postTweet(1, 5)
    print(obj.getNewsFeed(1))

    obj.follow(1, 2)
    obj.postTweet(2, 6)
    print(obj.getNewsFeed(1))

    obj.unfollow(1, 2)
    print(obj.getNewsFeed(1))
