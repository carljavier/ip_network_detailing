#########################################################################################
#																						#
#	Project: Subnet Network IP Detailing												#
#	Description: Simple tool to begin IPv4 Address detailing for your entire network.	#
#																						#
#	Author:																				#
#	Date:																				#
#	Version:																			#
#																						#
#########################################################################################


import ipcalc


##########################
# Network requirement variables 
#
##########################
#
# Network RFC1918 base: 
#   Class A - 10.X.X.X/8? 
#   Class B - 172.16.X.X/12?
#   Class C - 192.168.X.X/16?
classA="10.0.0.0/8"
classB="172.16.0.0/12"
classC="192.168.0.0/24"

items = {'a', 'b', 'c'}

classNetwork=classA

validClass = False

while validClass != True:
	print "Select which Class Nework Addressing:"
	print "a)\tClass A " + classA
	print "b)\tClass B " + classB
	print "b)\tClass C " + classC
	class_choice = input(":\t")
	print class_choice
		
	if class_choice in items:
		classNetwork=items[class_choice]
		validClass = True
		break
	else:
		print("please select a valid option")



#
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
#
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
