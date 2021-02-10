import os
import urllib
import tweepy
import requests
from twitter import *
from airtable import airtable

# Get secrets from environment variables
TOKEN = os.environ.get('TOKEN')
TOKEN_SECRET = os.environ.get('TOKEN_SECRET')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
AIRTABLE_BASE = os.environ.get('AIRTABLE_BASE')
AIRTABLE_KEY = os.environ.get('AIRTABLE_KEY')

try:
  # Log to Airtable
  at = airtable.Airtable(AIRTABLE_BASE, AIRTABLE_KEY)

  # Log to Twitter
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(TOKEN, TOKEN_SECRET)

  api = tweepy.API(auth)

  # Get view Today from table Tweets 
  result = at.get(table_name='Tweets',max_records=1,view="Today")

  # Get tweet and image url from Airtable
  tweet = result['records'][0]['fields']['Tweet']
  image_url = result['records'][0]['fields']['Image'][0]['thumbnails']['large']['url']
  
  # Uploading image to Twitter
  filename = 'temp.jpg'
  request = requests.get(image_url, stream=True)
  if request.status_code == 200:
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)
# Post to twitter
  api.update_with_media(filename, tweet)  
except Exception as e:
  print(e)