import tweepy

consumer_key = 'TSbkcX5b3ynO7KO8bHRAUxK16'
consumer_secret = 'yqr6CbDqwIOqA2g2VYdUI2is7EASBx94fKtyH6m6VDpca9nhaM'
access_token = '410302481-DLfV5a6yuBCHWMi7yXPha19q2cx1PqVvEHtmUOLX'
access_token_secret = 'HsBmHZ83d9DRMuoa9Sern5TJQrzLK5lKAND1LvHwkGOyP'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_ids = [34373370, 26257166, 12579252]
for x in user_ids:
    user = api.get_user(x)
    print ('Screen Name:', user.screen_name)
    print('User Name:', user.name)
    print('User Location:', user.location)
    print('User Description', user.description)
    print('The Number of Followers:', user.followers_count)
    print('The Number of Friends:', user.friends_count)
    print('The Number of Statuses:', user.statuses_count)
    print('User URL:', user.url)
    print ('')




