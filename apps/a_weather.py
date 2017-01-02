#!/usr/bin/python

import _karotz
import urllib2, urllib, simplejson


city_id = "615702"

if not _karotz.asleep():
    _karotz.ears(17, 17)

    baseurl = "http://query.yahooapis.com/v1/public/yql?"
    yql_query = "select item.condition from weather.forecast where woeid = "+city_id+" and u='c'"
    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
    result = urllib2.urlopen(yql_url).read()
    data = simplejson.loads(result)

    weather = data["query"]["results"]["channel"]["item"]["condition"]["text"]
    temperature = data["query"]["results"]["channel"]["item"]["condition"]["temp"]

    _karotz.tts("The weather is currently: "+weather+". The outside temperature is: "+temperature+" degrees.")
    
    _karotz.ears_reset()