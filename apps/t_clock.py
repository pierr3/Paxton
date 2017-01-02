#!/usr/bin/python

import _karotz
import datetime

now = datetime.datetime.now()

if now.minute == 0 and not _karotz.asleep():
    d = datetime.strptime(str(now.hour)+":00", "%H:%M")
    _karotz.tts("The time is: " % d.strftime("%I:%M %p"))