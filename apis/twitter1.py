from urllib import request, parse, error
import twitter
import json
import hidden

api = twitter.Api(consumer_key=hidden.consumer_key,
                  consumer_secret=hidden.consumer_secret,
                  access_token_key=hidden.access_token_key,
                  access_token_secret=hidden.access_token_secret)

statuses = api.GetUserTimeline(0)
print([s.text for s in statuses])
