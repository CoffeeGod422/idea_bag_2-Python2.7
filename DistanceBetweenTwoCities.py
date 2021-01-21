import math
def deg2rad(deg):
	a=float(deg*(math.pi/180))
	return a
def DistanceInKM(lat1,lon1,lat2,lon2): #Calculate distance by the Haversine formula and return distance value in KM Format
	dLat=deg2rad(float(lat2)-float(lat1))
	dLon=deg2rad(float(lon2)-float(lon1))
	a=(math.sin(dLat/2.0)*math.sin(dLat/2)+math.cos((deg2rad(float(lat1))))*math.cos(deg2rad(float(lat2)))*math.sin(dLon/2)*math.sin(dLon/2))
	c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
	D=float(6371*c)
	return D

def spaceraws(num): #efficient blank space raws function to decorate output
	for i in range(num):
		print ("")


t2=False
while (t2!=True):	#while loop that will keep running until the user type N when asked if the code should run again to change measure unit (see line:76) or if manualy type exit (see line:31)
	t1=False
	t2=False
	print ("Please State The Output unit mesure"+"\n"+"\n"+"1.Milimeter"+"\n"+"2.Centimeter"+"\n"+"3.Meter"+"\n"+"4.Kilometer"+"\n"+"5.Miles"+"\n"+"6.LightYear")


	usr_input=raw_input("state Unit measure: ")
	spaceraws(2)
	while (t1!=True):	# while loop that will keep running as long as the user gives the command to recalculate and not changing the measure unit (see lines:76-78)
		try:
			if (str(usr_input)=="exit" or str(usr_input)=="ex" or str(usr_input)=="quit" or str(usr_input)=="q"):
				print("BYE")
				t1=True
				t2=True
			else:
				a=int(usr_input)  #checking if the user input is valid, and if not, an appropiate message will appear
				print("#LOCATION 1")
				lat1=raw_input("Please specify Latitude1: ")
				lon1=raw_input("Please specify Longitude1: ")

				spaceraws(2)

				print("#LOCATION 2")
				lat2=raw_input("Please specify Latitude2: ")
				lon2=raw_input("Please specify Longitude2: ")

				Distance=DistanceInKM(lat1,lon1,lat2,lon2)



				#print output based on which measure unit the user inserted
				if (int(usr_input)==1):
					print ("Distance = "+str(Distance*1000000)+"Mm")
					spaceraws(4)

				if (int(usr_input)==2):
					print ("Distance = "+str(Distance*100000)+"Cm")
					spaceraws(4)

				if (int(usr_input)==3):
					print ("Distance = "+str(Distance*1000)+"M")
					spaceraws(4)

				if (int(usr_input)==4):
					print ("Distance = "+str(Distance)+"Km")
					spaceraws(4)

				if (int(usr_input)==5):
					print ("Distance = "+str(Distance*0.621371192)+"Miles")
					spaceraws(4)

				if (int(usr_input)==6):
					print ("Distance = "+str(Distance*(1.05702341*(pow(10,-13))))+"LightYears")
					spaceraws(4)

				#user interaction about should the code run again or terminate
				user_answer=raw_input("Do you want to calculate again?[Y/n]: ")
				if (user_answer=="Y" or user_answer=="y"):
					#user interaction about if the code should rerun to change measure unit
					user_answer_reunit=raw_input("change measure unit?[Y/n]: ")
					spaceraws(2)

					if (user_answer_reunit=="Y" or user_answer_reunit=="y"):
						t1=True
					if (user_answer_reunit=="N" or user_answer_reunit=="n"):
						t1=False

				if (user_answer=="N" or user_answer=="n"):
					t1=True
					t2=True

		#errors handler
		except:
			print ("====================")
			print ("something went wrong, pherhaps your input was invalid")
			print ("====================")
			spaceraws(0)
			t1=True
			



	


