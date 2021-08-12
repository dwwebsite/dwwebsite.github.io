import tweepy


#class MyStreamListener(tweepy.StreamListener):
#    def on_status(self, status):
#        print(status.text)
#    def on_error(self, status_code):
#        if status_code == 420:
#            #returning False in on_data disconnects the stream
#            return False


consumer_key = 'TSbkcX5b3ynO7KO8bHRAUxK16'
consumer_secret = 'yqr6CbDqwIOqA2g2VYdUI2is7EASBx94fKtyH6m6VDpca9nhaM'
access_token = '410302481-DLfV5a6yuBCHWMi7yXPha19q2cx1PqVvEHtmUOLX'
access_token_secret = 'HsBmHZ83d9DRMuoa9Sern5TJQrzLK5lKAND1LvHwkGOyP'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#myStream.filter(track=['Indiana'], async=True)
#myStream.filter(track=['weather'], async=True)

keywords = ['Indiana', 'weather']
count = 0

for word in keywords:
    s = api.search(word)
    for result in s:
        print(result.text)
        print('')
        count += 1
        if count == 50:
            break


