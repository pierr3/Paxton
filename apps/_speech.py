#!/usr/bin/python

import os
import re
import _karotz

def recognize(file):
    #sending the data to google
    os.system("curl -X POST -A \"Mozilla/5.0\" -o /tmp/speech.txt --header \"Content-Type: audio/x-flac;rate=16000\" --data-binary \"@"+file+"\" \"http://www.google.com/speech-api/v2/recognize?lang=en-UK&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw\"")
    
    #os.system("rm "+file)
    #reading the transcript back
    transcript = open("/tmp/speech.txt").read()
    print transcript
    os.system("rm /tmp/speech.txt")
    pattern = re.compile(r'("transcript":")([\w\s\d\']+)(")')
    if re.search(pattern, transcript):
        os.system("rm "+file)
        return re.search(pattern, transcript).group(2)
    else:
        os.system("rm "+file)
        return "null"
    fi

def convert(file):
    os.system("ffmpeg -i "+file+" /tmp/audio.flac")
    os.system("rm "+file)
    return "/tmp/audio.flac"
    
def start_recording():
    _karotz.ears(6, 6)
    _karotz.led("7D26CD")
    os.system("ffmpeg -f oss -acodec pcm_s16le -ac 1 -ar 16000 -vol 4096 -vn -i /dev/dsp /tmp/rec.wav </dev/null >/dev/null 2>/var/log/ffmpeg.log &")

def stop_recording():
    _karotz.pulse("0000FF", 700)
    _karotz.ears_reset()
    os.system("killall ffmpeg")
    line = recognize(convert("/tmp/rec.wav"))
    print "FOUND: "+line
    use_detection(line)
    _karotz.breath()
    
def use_detection(line):
    line = line.lower()
    if "weather" in line:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.system("python " + os.path.join(dir_path, "a_weather.py"))
    elif "sleep" in line:
        _karotz.tts("good night.")
        _karotz.sleep()
    else:
        _karotz.tts("Sorry, I did not understand that")
    