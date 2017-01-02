#!/usr/bin/python

import os
import sys
import commands
import urllib
import md5
import _speech

voice = "lucy"
lang = "en-gb"

def asleep():
    return os.path.isfile("/tmp/karotz.sleep") or os.path.isfile("/usr/openkarotz/Run/karotz.sleep")

def uuid():
    str(commands.getstatusoutput('cat /proc/sys/kernel/random/uuid')[1])
    
def led(primary):
    if not asleep():
        os.system("dbus-send --system --dest=com.mindscape.karotz.Led /com/mindscape/karotz/Led com.mindscape.karotz.KarotzInterface.light string:\""+str(uuid())+"\"  string:\""+primary+"\"")
        
def pulse(primary, pulse):
    if not asleep():
        os.system("dbus-send --system --dest=com.mindscape.karotz.Led /com/mindscape/karotz/Led com.mindscape.karotz.KarotzInterface.pulse string:\""+str(uuid())+"\" string:\""+primary+"\" string:\"000000\" int32:"+str(pulse)+" int32:-1")

def play_mp3(mp3file):
    if not asleep():
        cmd = "/usr/bin/madplay -A6 " + mp3file + " >/dev/null 2>&1"
        return os.system(cmd)

def play_web(url):
    if not asleep():
        return os.system("mplayer -quiet "+url+" >/dev/null 2>/dev/null")
    
def tts(text):
    md5Hash = md5.new(voice + text).hexdigest()
    mp3FileName = "/tmp/" + md5Hash + ".mp3"
    if not os.path.isfile(mp3FileName):
        params = urllib.urlencode({"t": text, "tl": lang})
        baseUrl = "http://responsivevoice.org/responsivevoice/getvoice.php"
        cmd = "wget -q -O %(mp3)s \"%(url)s?%(params)s\"" % { "mp3": mp3FileName, "url": baseUrl, "params": params }
        result = os.system(cmd)
    if os.path.isfile(mp3FileName):
        play_mp3(mp3FileName)

def breath():
    pulse("00FF00", 1400);  
    
def ear_left(position):
    if not asleep():
        os.system("/karotz/bin/ears "+str(position)+" 50 0 0")

def ear_right(position):
    if not asleep():
        os.system("/karotz/bin/ears 0 0 "+str(position)+" 50")
    
def ears(left, right):
    if not asleep():
        os.system("/karotz/bin/ears "+str(left)+" 50 "+str(right)+" 50")
    
def ears_reset():
    os.system("/karotz/bin/ears")
    
def sleep():
    if not asleep():
        ears(5, 5)
        led("000000")
        os.system("touch /tmp/karotz.sleep")
        
def wakeup():
    if asleep():
        os.system("rm /tmp/karotz.sleep")
        ears_reset()
        breath()
        