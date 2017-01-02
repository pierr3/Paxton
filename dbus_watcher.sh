#!/bin/bash

dbus-monitor --system | while read line 2> /dev/null
do
      
     echo "===>"$line     
     # ---------------------
     # BUTTON HANLDER
     # DBUS
     # --------------------- 
     # Long Button Press Detected Start
     # ---------------------          
     echo $line | grep "member=lclick_start"                                         
     if [ $? -eq 0 ]; then                                                     
        python /usr/Paxton/apps/_start_asr.py
        echo "start"
     fi
     
     # ---------------------
     # BUTTON HANLDER
     # DBUS
     # --------------------- 
     # Long Button Press Detected Stop
     # ---------------------          
     echo $line | grep "member=lclick_stop"                                         
     if [ $? -eq 0 ]; then                                                     
        python /usr/Paxton/apps/_stop_asr.py
        echo "stop"
     fi
     
     # --------------------- 
     # Single Click  Detected
     # User Defined Action
     # --------------------- 
      echo $line | grep "member=click"
      if [ $? -eq 0 ]; then
         echo "single"
      fi
      
      # ---------------------  
      # Double Click
      # User Defined Action
      # ---------------------  
      echo $line | grep "member=dclick"
      if [ $? -eq 0 ]; then
         echo "double"
       fi
       
       # ---------------------  
       # Triple Click
       # PreDefined Action
       # ---------------------  
       echo $line | grep "member=tclick"  
       if [ $? -eq 0 ]; then                                       
         echo "triple"
       fi                                              
   
 done
