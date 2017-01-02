#!/usr/bin/python

import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

print "Executing all apps"

for filename in os.listdir(os.path.join(dir_path, 'apps')):
    if filename.startswith("t_"):
        print "Executing app " + os.path.join(dir_path, 'apps',  filename)
        os.system("python " + os.path.join(dir_path, 'apps',  filename))