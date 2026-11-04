class Tweet:
    def __init__(self, tweet_id: int, time: int, next_tweet: Optional["Tweet"] = None):
        self.id = tweet_id
        self.time = time
        self.next = next_tweet

    def __lt__(self, other: "Tweet") -> bool:
        # Higher time (more recent) gets higher priority in heapq
        return self.time > other.time


class Twitter:
    def __init__(self):
        # Maps followerId -> set of followeeIds
        self.follows = defaultdict(set)
        # Maps userId -> head of their tweet linked list (most recent tweet)
        self.tweets = {}
        # Global auto-incrementing timestamp counter
        self.time = 0

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.time += 1
        # Prepend new tweet to the head of the user's tweet list
        previous_head = self.tweets.get(user_id, None)
        new_tweet = Tweet(tweet_id, self.time, previous_head)
        self.tweets[user_id] = new_tweet

    def getNewsFeed(self, user_id: int) -> List[int]:
        news_feed = []
        max_heap = []

        # Feed includes followees + the user themself
        candidates = self.follows[user_id] | {user_id}

        # Step 1: Push the latest tweet of each candidate into the heap
        for uid in candidates:
            if uid in self.tweets:
                heapq.heappush(max_heap, self.tweets[uid])

        # Step 2: Extract up to 10 most recent tweets
        while max_heap and len(news_feed) < 10:
            top_tweet = heapq.heappop(max_heap)
            news_feed.append(top_tweet.id)

            # Advance to that user's next most recent tweet
            if top_tweet.next:
                heapq.heappush(max_heap, top_tweet.next)

        return news_feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id != followee_id:
            self.follows[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        # .discard() removes without raising a KeyError if not present
        self.follows[follower_id].discard(followee_id)