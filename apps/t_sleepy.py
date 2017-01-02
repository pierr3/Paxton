#!/usr/bin/python

import _karotz
import datetime

now = datetime.datetime.now()
sleepAt = now.replace(hour=23, minute=0, second=0, microsecond=0)
wakeAt = now.replace(hour=10, minute=0, second=0, microsecond=0)

if now > sleepAt or now < wakeAt:
    if not _karotz.asleep():
        _karotz.sleep()
        
if _karotz.asleep() and now > wakeAt and now < sleepAt:
        _karotz.wakeup()