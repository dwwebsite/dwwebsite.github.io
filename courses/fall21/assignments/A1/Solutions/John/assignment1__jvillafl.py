# John Villaflor - jvillafl - Social Sensing Twitter Data Crawler

# API Key - oYLAblqr2OF5oQyTnZCaEy8mh
# API Secret - D1QxpMXtpfYYDQRE4bLPBsOoWYdmDWcoy7WfUkMdjuIa2J3cUn
# Access Token - 384137613-kVPOqCs7NgHMt3SuSwlHtXW8zUtRlgP5VlbzJJHx
# Access Secret - qxg0VmyUljAhqLt6dR2ZLwUMU7W73dN8uzuXvSUo53j94

### Tweepy Setup ###
import tweepy
auth = tweepy.OAuthHandler("oYLAblqr2OF5oQyTnZCaEy8mh", "D1QxpMXtpfYYDQRE4bLPBsOoWYdmDWcoy7WfUkMdjuIa2J3cUn")
auth.set_access_token("384137613-kVPOqCs7NgHMt3SuSwlHtXW8zUtRlgP5VlbzJJHx", "qxg0VmyUljAhqLt6dR2ZLwUMU7W73dN8uzuXvSUo53j94")
api = tweepy.API(auth)
### End Tweepy Setup ###


users = [34373370, 26257166, 12579252]

### Task 1 ###
#scrape information for the given users
with open("exercise1_output.txt", "w") as ofile:
    for ID in users:
        user = api.get_user(ID)
        ofile.write("Screen Name: "+user.screen_name)
        ofile.write("\nUser Name: "+user.name)
        ofile.write("\nUser Location: "+user.location)
        ofile.write("\nUser Description: "+user.description)
        ofile.write("\nThe Number of Followers: "+ str(user.followers_count))
        ofile.write("\nThe Number of Friends: "+ str(user.friends_count))
        ofile.write("\nThe Number of Statuses: "+ str(user.statuses_count))
        ofile.write("\nUser URL: "+user.url)
        ofile.write("\n\n")

### Task 2 ####
#find 20 followers and 20 friends for each of the example users
with open("exercise2_output.txt", "w") as ofile:
    for ID in users:
        ofile.write("The Followers List for: "+str(ID))
        followers = api.followers_ids(ID)[:20]
        for fID in followers:
            user = api.get_user(fID)
            ofile.write("\n"+user.screen_name)

        ofile.write("\n\nThe Friends List for: "+str(ID))
        friends = api.friends_ids(ID)[:20]
        for fID in friends:
            user = api.get_user(fID)
            ofile.write("\n"+user.screen_name)
        ofile.write("\n\n")

### Task 3 ###
#searching for the keywords Indiana or Weather
with open("exercise3_output_keyword.txt", "w", encoding="UTF-8") as ofile:
    result = api.search(q=("Indiana OR weather"), count=50)
    for tweet in result:
        ofile.write(tweet.text+"\n")

#center of the South Bend region is calculated to be: -86.265, 41.685 with radius of approx. 6km
with open("exercise3_output_geo.txt", "w", encoding="UTF-8") as ofile:
    result = api.search(geocode="41.685,-86.265,5km", count=50)
    for tweet in result:
        ofile.write(tweet.text+"\n")