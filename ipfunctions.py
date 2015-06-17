#########################################################################################
#																						#
#	Project: Subnet Network IP Detailing												#
#	Description: Functions for IPDetailing Tool 										#
#																						#
#	Author:	Carl Javier																	#
#	Date:																				#
#	Version:																			#
#																						#
#########################################################################################

import sys

def validOctate ( x ):
   "Check if octate is between 0 - 255"
   while x > 255:
       print "You choose a value too large, \n\n"
       x = int(raw_input("Enter Value between 0 - 255:\t\t"))
      
   return x

def validYesNo ( x ):
    "Check if Yes/No answered correctly"
    x=x.strip()
    print x
    while x != "Y" and x != "N" :
        print "Please choose an incorrect value \n\n"
        x = str(raw_input("Enter \"Y\" or \"N\":\t\t")).strip()
    
    return x
    