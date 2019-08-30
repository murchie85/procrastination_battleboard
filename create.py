import os 

f = open("../donotgit/access.txt", "r")
keys = f.read()
f.close()
keys  = keys.split(',')
#print("Access Keys are : " + str(keys))
ACCESS_TOKEN = keys[0]
ACCESS_SECRET = keys[1]


f = open("../donotgit/consumer.txt", "r")
keys = f.read()
keys  = keys.split(',')
#print("Consumer Keys are : " + str(keys))
CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API 
# Captured earlier 

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)



api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = 'elonmusk', count = 100, include_rts = True)

print('Pulling down data.....')                    

status_array=[]
max_count = 10
count = 0

for tweet in tweets:
    count = count + 1
    if count > max_count: break
    current = tweet._json
    # ONLY PULL DOWN REPLIES 
    if current['in_reply_to_status_id'] != None:
        status_array.append(current)
    
print('count is: ' + str(count))
if len(status_array) == 0:
    print('fucked up, not enough data, going to die now...thanks')
    raise   
    
print('Processing complete')

status_array[0].keys()

# PRINT REPORT 


reportfile = "musk" + ".html"
open(reportfile, 'w')
if not os.path.exists(reportfile):
    open(reportfile, 'w')

print_line = str('<font color="white">')
for x in range(0, len(status_array)):
    reply_to_string = status_array[x]['in_reply_to_status_id_str']
    tweet = api.get_status(reply_to_string)
    print_line = print_line + str(tweet.text) 
    print_line = print_line + str('<br><br>')
    print_line = print_line + str('')
    print_line = print_line + str('<b>')
    print_line = print_line  + str(" </font> ")


    print_line = print_line  + str('<font color="orange">')
    print_line = print_line + str(status_array[x]['text'])
    print_line = print_line  + str(" </font> ")

    print_line = print_line  + str('<font color="white">')
    print(status_array[x]['text'])
    print_line = print_line + str('</b>')
    print_line = print_line + str('<br>')
    print_line = print_line + str('--------------------------------')
    print_line = print_line + str('')
    print_line = print_line + str('<br>')

    

print_line = print_line  + str(" </font> ")  
with open(reportfile, 'a') as f:
    f.write(print_line)
f.close()


import os
import subprocess
subprocess.check_call(['open', 'index.html'])