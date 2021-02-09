import os
from twitter import *
from airtable import airtable

# Get secrets from environment variables
TOKEN= os.environ.get('TOKEN')
TOKEN_SECRET = os.environ.get('TOKEN_SECRET')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET= os.environ.get('CONSUMER_SECRET')
AIRTABLE_BASE = os.environ.get('AIRTABLE_BASE')
AIRTABLE_KEY = os.environ.get('AIRTABLE_KEY')

t = Twitter(auth=OAuth(TOKEN, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
at = airtable.Airtable(AIRTABLE_BASE, AIRTABLE_KEY)

result = at.get(table_name='Tweets',max_records=1,view="Today")
tweet = result['records'][0]['fields']['Tweet']

t.statuses.update(status=tweet)
