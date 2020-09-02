import tweepy
import os # operating system library

def create_api():
  consumer_key = 'VknUcPxCdIy0uZsp2yI7Lbzhg'
  consumer_secret = 'UjntFNP0Fu5tJNM9PMvSlRPwuausRZagZcusW3eTGDscpwdoHR'  
  access_token = '1268858796245487624-8vCczFGIIBmMVW8odfhPeat3690EzR'
  access_token_secret = 'cBxznP6nXfsZaMUvSlEl6szeENq559FOPNgB5Xh2nv2g3'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
# Complete code
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
    user = api.get_user('the_ameen_manna')
    api.update_profile(name=f'Tejas PS|{follower_count(user)} Followers')
    print(f'Updating Twitter Name : Tejas PS|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
    
      
