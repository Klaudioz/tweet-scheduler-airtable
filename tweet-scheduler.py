from twitter import *
from airtable import airtable

t = Twitter(auth=OAuth(TOKEN, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

at = airtable.Airtable(AIRTABLE_BASE, AIRTABLE_KEY)

result = at.get(table_name='Tweets',max_records=1,view="Today")
tweet = result['records'][0]['fields']['Tweet']

t.statuses.update(status=tweet)