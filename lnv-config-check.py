#!/usr/bin/python
#
# python test script that pings all machines listed in a script
# Srivats Iyer, Cumulus Networks, 7/5/2016
#

import sys
import os

print " "
print "1)  Print Bridge configuration "
print "2)  Print vxsnd status "
print " "

while True:
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #choice was successfully parsed!
        #exiting loop...
        break

if choice == 1 :
  os.system("sudo /sbin/brctl show")
elif choice == 2 :
  os.system("sudo /usr/sbin/service vxsnd status")  


raw_input()
