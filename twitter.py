

# ***`Query Data`***

import tweepy

# consumer keys and access tokens, used for OAuth
consumer_key = 'Your Consumer  Key..'
consumer_secret = 'Your Consumer Secret Key..'
access_token = 'Your Access Token  Key..'
access_token_secret = 'Your Access Token Secret Key..'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# creation of the actual interface, using authentication
api = tweepy.API(auth)

# This give about owner details...
api.update_status('Test')

user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))

user = api.get_user('BJP4Gujarat')

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))

user_friends = user.friends()
for friend in user_friends[:5]:
    print(friend.screen_name)

import pandas as pd

search = tweepy.Cursor(api.search, q="Nepal,corona", result_type="recent").items(2000)
k = pd.DataFrame(search)
k.to_csv("data.csv")

for item in search:
    print(item.text)

# Simplly get data...
search = tweepy.Cursor(api.search, q="corona", result_type="recent", lang="en").items(5)
for item in search:
    print(item.text)
    print(item.created_at)
    print(item.retweet_count)
    print(item.user.name)
    print(item.user.location)
    print(item.metadata['iso_language_code'])
    print(item.metadata['result_type'])
    print(item.source)

import pandas as pd

# Create A file of all tweets text...
search_data = tweepy.Cursor(api.search, q="corona", result_type="recent", lang="en").items(5)
users_locs = [[item.text, item.created_at, item.user.screen_name] for item in search_data]
tweet_text = pd.DataFrame(data=users_locs, columns=['text', 'date', 'username'])
print(tweet_text)
tweet_text.to_csv('text.csv', index=False)

search_words = "nepal, corona"
date_since = "2020-03-01"
date_until = "2020-06-01"
# Collect tweets
tweets = tweepy.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since,
                       ).items(5)
users_locs = [[item.text, item.created_at, item.user.screen_name] for item in tweets]
tweet_text = pd.DataFrame(data=users_locs, columns=['text', 'date', 'username'])
print(tweet_text)
tweet_text.to_csv("text1.csv", index=False)

# ***`Specified Username data`***

# Specified User data...
import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'Your Consumer  Key..'
consumer_secret = 'Your Consumer Secret Key..'
access_token = 'Your Access Token  Key..'
access_token_secret = 'Your Access Token Secret Key..'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
for status in tweepy.Cursor(api.user_timeline, screen_name='@Rushi93418211', tweet_mode="extended").items():
    print(status.full_text)

consumer_key = 'Your Consumer  Key..'
consumer_secret = 'Your Consumer Secret Key..'
access_token = 'Your Access Token  Key..'
access_token_secret = 'Your Access Token Secret Key..'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = "@sahil__2223"
startDate = datetime.datetime(2017, 12, 5, 7, 28, 10)
endDate = datetime.datetime(2020, 2, 24, 19, 2, 28)

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    tmpTweets = api.user_timeline(username, max_id=tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)
print(len(tweets))

consumer_key = 'Your Consumer  Key..'
consumer_secret = 'Your Consumer Secret Key..'
access_token = 'Your Access Token  Key..'
access_token_secret = 'Your Access Token Secret Key..'
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
ter = []
for tweet in public_tweets:
    ter.append(tweet)

user = api.get_user('username')
print(user)

print(user.screen_name)
print(user.followers_count)
for friend in user.followers():
    print(friend.screen_name)

data = []
for friend in tweepy.Cursor(api.friends).items():
    data.append(friend.screen_name)
print(data)

print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print(friend.screen_name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

api.user_timeline(id="@userid")




def update_urls(tweet, api, urls):
    tweet_id = tweet.id
    user_name = tweet.user.screen_name
    max_id = None
    replies = tweepy.Cursor(api.search, q='to:{}'.format(user_name),
                            since_id=tweet_id, max_id=max_id, tweet_mode='extended').items()

    for reply in replies:
        if (reply.in_reply_to_status_id == tweet_id):
            urls.append(get_twitter_url(user_name, reply.id))
            try:
                for reply_to_reply in update_urls(reply, api, urls):
                    pass
            except Exception:
                pass
        max_id = reply.id
    return urls


consumer_key = 'Your Consumer  Key..'
consumer_secret = 'Your Consumer Secret Key..'
access_token = 'Your Access Token  Key..'
access_token_secret = 'Your Access Token Secret Key..'


def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def get_tweet(url):
    tweet_id = url.split('/')[-1]
    api = get_api()
    tweet = api.get_status(tweet_id)
    return tweet


def get_twitter_url(user_name, status_id):
    return "https://twitter.com/" + str(user_name) + "/status/" + str(status_id)


api = get_api()
tweet = get_tweet("https://twitter.com/OfficeofSSC/status/1235133084523085824")
urls = ["https://twitter.com/OfficeofSSC/status/1235133084523085824"]
urls = update_urls(tweet, api, urls)
print(urls)