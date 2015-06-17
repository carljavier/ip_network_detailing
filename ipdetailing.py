#########################################################################################
#																						#
#	Project: Subnet Network IP Detailing												#
#	Description: Simple tool to begin IPv4 Address detailing for your entire network.	#
#																						#
#	Author:	Carl Javier																	#
#	Date:																				#
#	Version:																			#
#																						#
#########################################################################################


import ipcalc, sys
from ipfunctions import *


##########################
# Network requirement variables 
#
##########################
#
# Network RFC1918 base: 
#   Class A - 10.X.X.X/8? 
#   Class B - 172.16.X.X/12?
#   Class C - 192.168.X.X/16?
classA="10.X.X.X/8"
classB="172.16.X.X/12"
classC="192.168.X.X/24"

items = {'0', '1', '2'}

classNetwork= classA,classB,classC
class_choice='4'

validClass = False

while validClass != True:
	print "Select which Class Nework Addressing:"
	print "0)\tClass A " + classA
	print "1)\tClass B " + classB
	print "2)\tClass C " + classC
	class_choice = int(raw_input(":\t"))
	
		
	if class_choice < 3:
            print "You chose " + classNetwork[class_choice]
            validClass = True
        else:
            print("please select a valid option\n\n\n")


print "Please choose the X values for your Base Class Network: " + classNetwork[class_choice]
network=[10,0,0,0] #Set a default of none was chosen


print "Select which Class Nework Addressing:"
print "0)\tChoose to replace X in Class Network: " + classNetwork[class_choice]
print "1)\tChoose to keep the default Class Network: " + classNetwork[class_choice]

#Create Choice for Default Network Setup

if class_choice == 0:
    print "You chose Base Class Network: "  + classNetwork[class_choice] + " \n\nPlease choose X.X.X"
    network= [10,0,0,0]
    count = 0
    for x in network:
        if network[count] == 0:
            network[count] = validOctate(int(raw_input("Choose first X between 0 - 255:\t")))
            ####NEED TO WRITE A Function to Check for Valid 0 - 255 values
        count += 1
    print "Network is " + str(network)

if class_choice == 1:
    print "You chose Base Class Network: "  + classNetwork[class_choice] + " \n\nPlease choose X.X"
    network= [172,16,0,0]
    count = 0
    for x in network:
        if network[count] == 0:
            network[count] = validOctate(int(raw_input("Choose first X between 0 - 255:\t")))
            ####NEED TO WRITE A Function to Check for Valid 0 - 255 values
        count += 1
    print "Network is " + str(network)


if class_choice == 2:
    print "You chose Base Class Network: "  + classNetwork[class_choice] + " \n\nPlease choose X.X"
    network= [192,168,0,0]
    count = 0
    for x in network:
        if network[count] == 0:
            network[count] = validOctate(int(raw_input("Choose first X between 0 - 255:\t")))
            ####NEED TO WRITE A Function to Check for Valid 0 - 255 values
        count += 1
    print "Network is " + str(network)
    

print "\n\n\n\n\nNetwork Number Chosen is: " + str(network[0])+ "." + str(network[1]) + "." + str(network[2])+ "." + str(network[3])

#################################
# Number of Sites/Locations?
#   Custom VLAN Creation Setup? (Yes/No)
#       Number of VLANs per Site/Locations?
#       Name of VLAN:
#       Number of end points in <Insert Name of Vlan> ?
#   If Custom Vlans per Site/Locations not specified 
#                   then go through default Vlans per site:
#       Data VLan: (Yes/No)
#            Number of PCs/Users?
#       Voice VLAN Required? (Yes/No)
#           Assume number of voice devices == number of PC/Users
#       Wireless VLan Required? (Yes/No)
#           Assume number of voice devices == number of PC/Users
#
# Expected growth of users per VLAN?
#           Specify Percentage? 10 - 90% ?
#
# VLAN IP Address Options per Vlans
#       Gateway Address: First Address? Last Address?
#           Number of addresses to reserve (High or Low)? (Future Use)
################################


NoOfSites = abs(int(raw_input("Choose number of sites for entire network:\t")))

print "\n\nCreate custom VLANs per site (Y)\n\nChoose default VLANs per site (N)"
customVlans=validYesNo(raw_input(":\t"))
noVlans = 2 #default is 2 vlans - voice and data
vlanName = ["data","voice"] #default name of Vlans
vlanNumber = [1,100] #default vlan numbers
vlanSize = [255,255] #default size of vlans

if customVlans == "Y":
    
    for x in range(NoOfSites):
        print "\n\nSITE " + str(x+1) + " Configuration"
        noVlans = int(raw_input("\n\nEnter number of VLANs per site:\t"))
        vlanName = []
        vlanNumber = [] 
        vlanSize = []
        for a in range(noVlans):
            print "\n\nVLAN " + str(x+1) + " Configuration"
            confirm = "N"
            while confirm != "Y": 
                vlanName.append(str(raw_input("\n\nEnter VLAN Name:\t")).strip())
                vlanNumber.append(int(raw_input("\n\nEnter VLAN Number:\t")))
                vlanSize.append(int(raw_input("\n\nEnter VLAN Size (eg How many users/nodes in VLAN?):\t")))
                #Confirm to user Vlan details correct
                print "\nVLAN name: " + str(vlanName[a])
                print "\nVLAN number" + str(vlanNumber[a])
                print "\nVLAN Size " + str(vlanSize[a])
                confirm = validYesNo(raw_input("\n\nAre the above details correct? (Y/N)\t:\t")) #Problem when select No, need to overwrite same variables, not append to List
            





 

##########################
# WAN Link IP Addressing? 
#   (Yes if required to provide addressing / No if Service Provider has DHCP)
#   If Yes, Use <Number of Sites/Locations>
#           
#
##########################   
# Management Device Network Addressing?
#   (Yes/No)
#   If Yes, Use <Number of Sites/Locations>
#
##########################
# DataCenter or Cloud Network Adressing?
#   Number of DataCentres/Site Locations?
#   Special Network address from RFC1918? Suggest a few suggestions (Do not include Branch Addressing)
#   If DataCentre incorporate, suggest a DataCentre/Cloud specialist design
#
##########################
#
