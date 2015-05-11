import tweepy
import codecs
fp = codecs.open("tweets.txt", "w", "utf-8")
consumer_key = ""
consumer_secret = ""
 
access_token =  ""
access_token_secret =  ""

 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)

year = raw_input("Enter your current year:")
month = raw_input("Enter your current month:")
days = raw_input("Enter the current day in numbers:")
location = raw_input("Enter your current location in the form 35.949473,-77.806508,1000km (In quotations).")
day = int(days)
tweetCount = 0
my_tweets = []

for tweet in tweepy.Cursor(api.search,
                           q="*",
                           count=100,
                           result_type="recent",
                           include_entities=True,
                           since_id=year-month-day,
                           geocode=location,
                           lang="en").items():
#
  x = str(unicode(tweet.text).encode("utf-8"))
  #change unicode to string so I can search through them
  splitTweets = x.split(" ")
  expletiveCount = 0
  violentCount = 0
  for tweetWords in splitTweets:
    for curseWords in file("expletives.txt.txt", "r").readlines():
      correctedCurseWords = curseWords.strip("\n")
      if correctedCurseWords == tweetWords:
        expletiveCount = expletiveCount + 1
    for violentWords in file("violentwords.txt", "r").readlines():
      correctedViolentWords = violentWords.strip("\n")
      if correctedViolentWords == tweetWords:
        violentCount = violentCount + 1
      
  if violentCount > 0 and expletiveCount > 0:
    print tweet.user.screen_name, x
    tweetCount = tweetCount + 1
    fp.write(tweet.user.screen_name)
    fp.write(" ")
    fp.write(tweet.text)
    fp.write("/n")
    

