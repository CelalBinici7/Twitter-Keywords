import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Türkiye until:2022-02-21 since:2022-02-14"
tweets = []
limit = 10000000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

df.to_csv('şubatHafta2.csv')