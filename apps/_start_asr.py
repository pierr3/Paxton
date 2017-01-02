#!/usr/bin/python

import _karotz
import _speech

if not _karotz.asleep():
    _speech.start_recording()