#!/usr/bin/env python3
import tweepy
#consumer_key = 'jitZgZzkD42PETiW4hz3QvA5z'
#consumer_secret = 'OXqH4zvkFNGrtiSekTI5vcj4gehK0WhtKGzi4Oz3c0y4odBZ9H'
consumer_key = 'FtPR0nw9RSKOs9g49Rxuv2zgD'
consumer_secret = 'iOiY5vvbnhol37iR2J6FvVmEniFEvininNX31naoba9zrCEo21'

#access_token_key = '1872893581-ZphrbUVBpXfKSnMBw935UcJTZ84tW1uNejERGYz'
#access_token_secret = 'CD6uyPVIixdnO5jexw7opfWnwwD5rwKW7W5eUoZu4hJLR'
access_token_key = '1083457977636581376-GLesO2bComImwnrvRLvuczkTo3A3dN'
access_token_secret = 'nBdrD09rJfJa16Ja3OAQJmKWL8Q0qy108JmSS1TfILXI9'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--ids', nargs='+')
parser.add_argument('--info', action='store_true')
parser.add_argument('--keywords', nargs='+')
parser.add_argument('--geoloc', action='store_true')
args = parser.parse_args()

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

if args.keywords:
    stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    stream.filter(track=args.keywords)
elif args.geoloc:
    stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    stream.filter(locations=[-86.33,41.63,-86.20,41.74])

def getInfo(ID):
    user = api.get_user(id=ID)
    print("Screen Name: {}".format(user.screen_name))
    print("User Name: {}".format(user.name))
    print("User Location: {}".format(user.location))
    print("User Description: {}".format(user.description.encode('latin-1', 'replace').decode()))
    print("Number of Followers: {}".format(user.followers_count))
    print("Number of Friends: {}".format(user.friends_count))
    print("Number of Statuses: {}".format(user.statuses_count))
    print("User URL: {}\n".format(user.url))

def iterateIDS(idList):
    for ID in idList[0:20]:
        print(api.get_user(id=ID).screen_name)

if args.ids:
    for ID in args.ids:
        if args.info:
            getInfo(ID)
        else:
            print("\nFriends and Followers of {}".format(ID))
            print("\nFriends:")
            iterateIDS(api.friends_ids(id=ID))
            print("\nFollowers:")
            iterateIDS(api.followers_ids(id=ID))

