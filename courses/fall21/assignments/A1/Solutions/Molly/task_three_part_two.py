import tweepy

consumer_key = 'TSbkcX5b3ynO7KO8bHRAUxK16'
consumer_secret = 'yqr6CbDqwIOqA2g2VYdUI2is7EASBx94fKtyH6m6VDpca9nhaM'
access_token = '410302481-DLfV5a6yuBCHWMi7yXPha19q2cx1PqVvEHtmUOLX'
access_token_secret = 'HsBmHZ83d9DRMuoa9Sern5TJQrzLK5lKAND1LvHwkGOyP'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

coordsLong = (-86.33 + -86.22) / 2
coordsLong = str(coordsLong)
coordsLat = (41.63 + 41.74) / 2
coordsLat = str(coordsLat)
rad = '16km'
coords = coordsLat + ',' + coordsLong + ',' + rad
coords = str(coords)
count = 0

g = api.search(geocode=coords)
for result in g:
    print (result.text)
    count += 1
    if count == 50:
        break



