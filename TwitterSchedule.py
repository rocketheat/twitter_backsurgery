# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 08:03:24 2017

@author: Ghaith Habboub

@Topic: Twitter Query for Spine Surgery

@Description: This is a twitter query for anyperson who mention spine surgery
"""

import twitter
import json
import schedule
import time
import pprint

# These are the REST API parameters
consumerKey= 'tFznFsSwD7rsfS1Xwnec50j2g'
consumerSecret='oCrNm4FcmTiAr7ylIsWS0S4d6XHlO9hRmH4sLxKQ6JZDpOxQeu'
OauthToken= '813509115423195136-ifRGdypYAIwpzAyxI0UayE7jHUWsteM'
OauthSecret= 'Ja0Ju6rgbMYgVCDi3sRpG5eHHONIsBza3CKGx5krpVSP6'

authinfo = twitter.oauth.OAuth(OauthToken, OauthSecret, consumerKey, consumerSecret)
twitterAPI = twitter.Twitter(auth=authinfo)

def twitterschedule():
    topicsearch = twitterAPI.search.tweets(q="#backsurgery")
    pprint.pprint(topicsearch)
    with open('./data.txt', 'a') as outfile:
        json.dump(topicsearch, outfile)
    interval = "****+++****"
    with open('./data.txt', 'a') as outfile:
        json.dump(interval, outfile)

schedule.every(1).minutes.do(twitterschedule)

while True:
    schedule.run_pending()
    print('still working')
    time.sleep(10)
