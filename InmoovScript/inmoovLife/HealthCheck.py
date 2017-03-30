# ##############################################################################
# 								TIMERS ACTION
# ##############################################################################

###############################################################################
# Timer function to autostart webkit microphone every 10seconds
# only if robot not actualy speaking
###############################################################################
HealthCheck = Runtime.start("HealthCheck","Clock")
HealthCheck.setInterval(60000)

def HealthCheck_def(timedata):

	#### modif JPM
	minute = str(timedata)[14:16]
	heure = str(timedata)[11:13]
	if minute =="00" :
		#talkBlocking("il est exactement "+heure+" heure")
		Mheure = random.randint(1,5)
		Mheure2 = (str(Mheure)+".mp3")
		AudioPlayer.playFile(RuningFolder+'/system/sounds/heure/'+heure+'/'+Mheure2)
		
	## lance une humeur au hasard	
	if minute=="08" or minute=="16" or minute=="24" or minute=="33" or minute=="41"or minute=="51":
		nbsurprise = random.randint(1,305)
		surprise = (str(nbsurprise)+".mp3")
		AudioPlayer.playFile(RuningFolder+'/system/sounds/surprise/'+surprise)
	######### fin modif JPM

	if RobotIsErrorMode==1:
		if error_red:
			PlayNeopixelAnimation("Flash Random", 255, 0, 0, 5)
	

HealthCheck.addListener("pulse", python.name, "HealthCheck_def")		
HealthCheck.startClock()

