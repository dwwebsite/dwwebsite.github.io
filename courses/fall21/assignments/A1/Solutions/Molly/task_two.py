import tweepy

consumer_key = 'TSbkcX5b3ynO7KO8bHRAUxK16'
consumer_secret = 'yqr6CbDqwIOqA2g2VYdUI2is7EASBx94fKtyH6m6VDpca9nhaM'
access_token = '410302481-DLfV5a6yuBCHWMi7yXPha19q2cx1PqVvEHtmUOLX'
access_token_secret = 'HsBmHZ83d9DRMuoa9Sern5TJQrzLK5lKAND1LvHwkGOyP'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_ids = [34373370, 26257166, 12579252]

for user in user_ids:
    count = 0
    user_name = api.get_user(user)
    user_friends = api.friends_ids(user)
    user_followers = api.followers(user)
    print('The Friends List for ', user_name.name, ':')
    print('')
    for x in user_friends:
        y = api.get_user(x)
        print(y.screen_name)
        count += 1
        if count == 20:
            break
    print('')
    print ('The Followers List for ', user_name.name, ':')
    print ('')
    for x in user_followers:
        print (x.screen_name)
    print ('')






