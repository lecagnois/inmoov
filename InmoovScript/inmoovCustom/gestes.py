
def fingeropen(main):
  leftHand.attach()
  #sleep(5)
  #talkBlocking("servo main gauche activer")
  #speed = vitesse main gauche pouce index majeux ring petit poignet
  i01.setHandSpeed(main,1,1,1,1,1,0.7)
  sleep(3)
  talkBlocking("ok j'ouvre ma main")
  sleep(3)
  i01.moveHand(main,170,170,170,170,150)
  sleep(5)
  # met le poignet a 80
  i01.moveHand(main,170,170,170,170,150,80)
  #sleep(5)
  leftHand.detach()


def fingerclose(main):
  leftHand.attach()
  sleep(5)
  i01.setHandSpeed(main,0.98,1,1,1,1,0.7)
  i01.moveHand(main,0,0,0,0,0,20)
  sleep(5)
  talkBlocking("ma main est fermer")
  #sleep(10)
  leftHand.detach()

def fingermiddle():
  leftHand.attach()
  i01.setHandSpeed("left",0.9,0.9,0.9,1,1,1)
  i01.moveHand("left",30,30,30,40,30,90)
  talkBlocking("ok je vous aicoute")
  leftHand.detach()
  
def compte123():
  leftHand.attach()
  i01.setHandSpeed("left",1,0.95,0.95,1,1,1)
  i01.moveHand("left",170,0,0,0,0) 
  talkBlocking("UN") 
  sleep(3)
  i01.moveHand("left",170,170,0,0,0) 
  talkBlocking("deux")
  sleep(3)  
  i01.moveHand("left",170,170,170,0,0) 
  talkBlocking("trois")    
  #i01.moveHand("left",170,170,170,170,0) 
  #talkBlocking("quatre")   
  #i01.moveHand("left",170,170,170,170,150) 
  #talkBlocking("cinq")   
  sleep(2)
  leftHand.detach()
  
def yeux():
  i01.head.attach()
  sleep(3)
  i01.head.eyeX.moveTo(0)
  talkBlocking("oeil a gauche")    
  sleep(3)
  i01.head.eyeX.moveTo(90)
  talkBlocking("oeil a 90")    
  sleep(3)
  i01.head.eyeX.moveTo(180)
  talkBlocking("oeil a droite")      
  sleep(3)
  i01.head.eyeX.moveTo(110)
  talkBlocking("oeil centre")
  #sleep(3)
  i01.head.detach()
  
def tetedroite():
  i01.head.attach()
  i01.setHeadSpeed(0.6, 0.6)
  i01.moveHead(130,50)
  talkBlocking("tete a droite")
  sleep(5)
  i01.head.eyeX.moveTo(100)
  i01.head.detach()
  
def tetegauche():
  i01.head.attach()
  i01.setHeadSpeed(0.60, 0.0)
  i01.moveHead(70,120)
  talkBlocking("tete a gauche")
  sleep(5)
  i01.head.neck.moveTo(140)
  i01.head.detach()
  
def ciel():
  i01.head.attach()
  i01.setHeadSpeed(0.6, 0.6)
  i01.head.neck.moveTo(180)
  sleep(3)
  talkBlocking("whoooooooo.. toutes les aitoiles")
  i01.head.detach()
   
def bras():
  i01.leftArm.attach()
  i01.setArmSpeed("left", 0.80, 0.80, 0.80, 0.85)
  # parametres biceps , rotate, bras ,omoplate
  talkBlocking("je tourne mon bras")
  sleep(5)
  i01.moveArm("left",30,100,180,0)
  sleep(5)
  talkBlocking("je leve mon bras")
  sleep(5)
  i01.moveArm("left",60,90,160,0)
  sleep(5)
  # position initiale
  talkBlocking("je decend mon bras et le tourne")
  sleep(3)
  i01.moveArm("left",0,75,180,0)
  sleep(2)
  i01.leftArm.detach()
  
def biceps():
  i01.leftArm.attach()
  talkBlocking("je leve mon biceps")
  sleep(5)
  i01.moveArm("left",85,75,180,0)
  sleep(2)
  i01.leftArm.detach()

  
def action():
  tetedroite()
  sleep(2)
  tetegauche()
  sleep(2)
  biceps()
  sleep(2)
  compte123()
  sleep(2)
  bras()
  sleep(2)
  main = "left"
  fingerclose(main)
  yeux()
     
def bonjour():
	# affecte l'heure systeme a la variable local de type entier nommer heure 
	heure = int(time.strftime('%H'))
	# affiche le resultat dans debug python 
	print heure
	# conditions si
	if heure == 12 :
		talkBlocking("bonjour jean pierre ,il est plus de " + str(heure) +" heure . il est temps de sortir les fourchettes")	
		if heure == 16 :
			talkBlocking("bonjour jean pierre ,il est plus de " + str(heure) +" heure . c est l heure du goutest")
		if heure == 20 :
			talkBlocking("bonjour jean pierre ,il est plus de " + str(heure) +" heure . je vais faire la soupe")
	else :
		talkBlocking("bonjour jean pierre ,il est plus de " + str(heure) +"heure .")

def gym():
	x =0
	i01.leftArm.attach()
	while x < 3:
		i01.moveArm("left",90,75,180,0)
		sleep(5)
		i01.moveArm("left",0,75,180,0)
		sleep(5)
		x=x+1
	talkBlocking("je suis fatiguai")
	i01.leftArm.detach()
	
def loto(phrase,the,chance,fin):
     table1  = [(random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)),(random.randint(1,49))]
     tablefin = []  
     doublon = []

     for i in table1:  
         if i not in tablefin:
             tablefin.append(i) #supprime les doublons
         else:
             doublon.append(i) #extraire les doublons
     d = len(doublon)
     while d > 0:
     #nouveau tirage
         doublon = []
         table1  = [(random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)), (random.randint(1,49)),(random.randint(1,49))]
         # recherche doublon
         for i in table1:
             if i not in tablefin:
                  tablefin.append(i) #supprime les doublons
             else:
                 doublon.append(i) #extraire les doublons
             # si il existe doublon d+1 et vite la table
             if (len(doublon)==1)or(len(doublon)==2)or(len(doublon)==3)or(len(doublon)==4)or(len(doublon)==5):       
                 talkBlocking("j ai trouver un doublon , je refais un tirage")
                 d = d+1
                 doublon =[]
             else:
                 d = 0
             break   
     # tri la table avant de la dire        
     table1.sort() 
     talkBlocking(phrase)
     talkBlocking(the+str(table1[0]))
     talkBlocking(the+str(table1[1]))
     talkBlocking(the+str(table1[2]))
     talkBlocking(the+str(table1[3]))
     talkBlocking(the+str(table1[4]))	
     talkBlocking(chance+str(random.randint(1,9)))
     talkBlocking(fin)

def allume(phrase):
	try: 
		talk("je controle le serveur .")
		# adresse ip de votre serveur raspeberry
		u = os.popen("ping -n 1 192.168.1.27")
		result = u.read()
		if result.count("perte 0") == 1 and result.count("Impossible") == 0:
			print ("ok")
			talk(phrase)
			url = 'http://192.168.1.27/lumieres.php'
			urllib.urlopen(url)
		else:
			talk("le serveur est hors service") 
			print("ko")   
	except IOError:
		talk("le serveur est hors service")
		
def eteins(phrase):
     try: 
         talk("je controle le serveur .")
         # adresse ip de votre serveur raspeberry
         u = os.popen("ping -n 1 192.168.1.27")
         result = u.read()
         if result.count("perte 0") == 1 and result.count("Impossible") == 0:
             print ("ok")
             talk(phrase)
             url = 'http://192.168.1.27/lumiereoffs.php'
             urllib.urlopen(url)
             
         else:
             talk("dommage le serveur est hors service") 
             print("ko")   
             
     except IOError:
         talk("dommage le serveur est hors service")
		 
def mailsend(amis):
	try:
		talkBlocking(amis)
		# creation d un dictionnaire des amis
		dico = {"jean-pierre":"lecagnois@wanadoo.fr","colette":"collinette@wanadoo.fr"}
		# message si pas trouver
		if (dico.get(amis) == None):
			print("Amis inconnu dans l annuaire")
			talkBlocking("personne inconnu au bataillon")
		else:
			print (dico.get(amis))
			talkBlocking(" fais parti de tes amis ")
			global ami 
			ami = (dico.get(amis))
			sleep(2)
			chatBot.getResponse("SYSMAIL")
			sleep(2)
			
	except IOError:
		talk("le serveur est hors service , mail non transmis")
	except OSError:
		talkBlocking("oups il y a une erreur")
	except ValueError:
		talkBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise

def envoi(message):
	try:
		codage = 'UTF-8' # <= modif
		fromaddr = "lecagnois@wanadoo.fr"
		toaddr = ami
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Message de InMOOV"
		msg['Charset'] = codage  # <= modif
		msg['Content-Type'] = 'text/plain; charset=UTF-8' # <--modif
		body = message
		if ami == "lecagnois@wanadoo.fr":
			typetexte = 'text/plain' # <= modif
		else:
			typetexte = 'plain'
		msg.attach(MIMEText(body, typetexte, 'UTF-8')) # <= modif
		#msg.attach(MIMEText(body, 'text/plain'))
		
		# valeur du serveur smtp securise ou pas
		#server = smtplib.SMTP('smtp.gmail.com', 587)
		server = smtplib.SMTP('smtp-msa.orange.fr', 587)
		#server.starttls()
		server.login(fromaddr, "antara06")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		talkBlocking("mel transmis a " + ami)
		server.quit()
		server.close()
	
	except IOError:
		talk("le serveur est hors service , mail non transmis")
	except OSError:
		talkBlocking("oups il y a une erreur")
	except ValueError:
		talkBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise

		
def anniversaire():
	#date en francais
	locale.setlocale(locale.LC_TIME,'')
	talkBlocking(time.strftime('Nous sommes le %A %d %B %Y,',time.localtime())) 
	
	# la clef du dico sera la date systeme
	anniversaire = time.strftime('%m-%d')
	jour = int(time.strftime('%d'))
	mois = int(time.strftime('%m'))
	annee = int(time.strftime('%Y'))
     
	# creation d un dictionnaire anniversaire entrer ici vos parents et amis (index :donnees)
	dico = {"03-06":"jean-pierre 1959" ,"03-14":"francis 1961" , "09-06":"colette 1948" , "09-05": "francis 1960"}	
	# mise en forme des dates
	madate= datetime.datetime(annee,mois,jour)
	jour7 = datetime.timedelta(days = +7)
	jour1 = datetime.timedelta(days = +1)
	rappel = str((madate + jour7))[5:10]
	rappel2 = str((madate + jour1))[5:10]
	
	sleep(2)
	
	if (dico.get(rappel) != None):
		agedico = int(dico.get(rappel)[-4:])
		prenom = (dico.get(rappel)[:-4])
		age = annee - agedico 
		talkBlocking("c est lanniversaire de " + prenom + str(age) +" ans dans 7 jours")

	if (dico.get(rappel2) != None):
		agedico = int(dico.get(rappel2)[-4:])
		prenom = (dico.get(rappel2)[:-4])
		age = annee - agedico 
		talkBlocking("demain c est lanniversaire de " + prenom + str(age) +" ans")

	if (dico.get(anniversaire) != None):
		agedico = int(dico.get(anniversaire)[-4:])
		prenom = (dico.get(anniversaire)[:-4])
		age = annee - agedico 
		talkBlocking("bon anniversaire " + prenom + str(age) +" printemps ,tu les fais pas")

	if ((dico.get(rappel) == None) and (dico.get(rappel2) == None) and (dico.get(anniversaire) == None)):
		talkBlocking("c est lanniversaire de personne")
		
def photo(msg):
	# parametrage opencv sur camera 0
	#opencv = Runtime.createAndStart("opencv","OpenCV")
	i01.opencv.addFilter("pdown","PyramidDown")
	i01.opencv.setDisplayFilter("pdown")
	i01.opencv.setCameraIndex(0)
	i01.opencv.capture()
	talkBlocking(msg)

	sleep(2)
	talkBlocking("attention le petit oiseau va sortir")
	sleep(4)
	#ajouter le fichier click.mp3 dans ../system/sound
	AudioPlayer.playFile(RuningFolder+'/system/sounds/click.mp3')
	# declarer la variable photofilename dans .../system/statusglaobal.py
	global photoFileName
	photoFileName = i01.opencv.recordSingleFrame()
	print "nom du fichier :" , photoFileName
	
	#suppresion des filtres et arret capture
	i01.opencv.removeFilters()
	sleep(1)
	i01.opencv.stopCapture()
	sleep(1)
	
	talkBlocking("merci la photo est enregistrer , veux tu envoyer un mel au concepteur")
	sleep(2)
	#answer = "veux tu envoyer la photo au concepteur"
	#chatBot.getResponse("say " + answer) #on demande a programAB de faire le perroquet ! 	
	#chatBot.getResponse("SYSREPONSE" + photoFileName)
	
def photoui():
   print ('envoie du mail avec piece jointe') 
   #fromaddr = "lecagnois@gmail.com"
   fromaddr = "lecagnois@wanadoo.fr"
   toaddr = "lecagnois@wanadoo.fr"
   msg = MIMEMultipart()
   msg['From'] = fromaddr
   msg['To'] = toaddr
   msg['Subject'] = "phographie"

   body = "envoie d un mail de InMoov avec piece jointe"
   msg.attach(MIMEText(body, 'multipart/mixed'))

   filename = photoFileName
   sleep(1)
   attachement = open("d:/MRL9/inmoov-master/" + photoFileName,"rb")
                   
   part = MIMEBase('application', 'octet-stream')
   part.set_payload((attachement).read())
   encoders.encode_base64(part)
   part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
   msg.attach(part)
   #server = smtplib.SMTP('smtp.gmail.com', 587)
   server = smtplib.SMTP('smtp-msa.orange.fr', 587)
   #server.starttls()
   #server.login(fromaddr, "/Mimi6cu")
   server.login(fromaddr, "antara06")
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr, text)
   server.quit()
   talkBlocking("mel transmis au concepteur " )
   print ('message envoye')

def photoa(destinataire):
	try:
		talkBlocking(destinataire)
		print destinataire
		# creation d un dictionnaire des amis
		dico = {"jean-pierre":"lecagnois@wanadoo.fr" , "colette":"collinette@wanadoo.fr"}
		# message si pas trouver
		if (dico.get(destinataire) == None):
			print("Amis inconnu dans l annuaire")
			talkBlocking("personne inconnu au bataillon")
		else:
			print (dico.get(destinataire))
			talkBlocking(" fais parti de tes amis  regarde moi dans les yeux")
			i01.opencv.addFilter("pdown","PyramidDown")
			i01.opencv.setDisplayFilter("pdown")
			i01.opencv.setCameraIndex(0)
			i01.opencv.capture()
			sleep(2)
			talkBlocking("attention le petit oiseau va sortir")
			sleep(5)
			AudioPlayer.playFile(RuningFolder+'/system/sounds/click.mp3')
			photoFileName = i01.opencv.recordSingleFrame()
			i01.opencv.removeFilters()
			sleep(1)
			i01.opencv.stopCapture()
			sleep(1)
			talkBlocking("merci la photo est enregistrer  Envoi de la photo a " + destinataire)
			sleep(2)
			# ici envoi du mail avec piece jointe
			#fromaddr = "lecagnois@gmail.com"
			fromaddr = "lecagnois@wanadoo.fr"
			toaddr = (dico.get(destinataire))
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = toaddr
			msg['Subject'] = "photo souvenir"
			body = "tu a une photo en attente"
			msg.attach(MIMEText(body, 'multipart/mixed'))
			filename = photoFileName
			attachement = open("d:/MRL9/inmoov-master/" + photoFileName,"rb")
            #encodage du mail      
			part = MIMEBase('application', 'octet-stream')
			part.set_payload((attachement).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
			msg.attach(part)
			# valeur du serveur smtp securise ou pas
			#server = smtplib.SMTP('smtp.gmail.com', 587)
			server = smtplib.SMTP('smtp-msa.orange.fr', 587)
			#server.starttls()
			#server.login(fromaddr, "/Mimi6cu")
			server.login(fromaddr, "antara06")
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()
			server.close()
			talkBlocking("photo transmis a " + destinataire)

	except IOError:
		talkBlocking("le serveur est hors service  mail non transmis")

def liremail(destinataire):
	try :
		
		# creation d un dictionnaire des amis
		dico = {"jean-pierre":'(FROM "lecagnois")',"colette":'(FROM "collinette")', "robot":'(FROM "inmoov")'}
		# message si pas trouver
		if (dico.get(destinataire) == None):
			print("Amis inconnu dans l annuaire")
			talkBlocking("personne inconnu au bataillon")
		else:
			mail = imaplib.IMAP4_SSL('imap.orange.fr')
			# imaplib module implements connection based sur protocol IMAPv4 
			mail.login('lecagnois@wanadoo.fr', 'antara06')
			mail.list() 
			mail.select('inbox') # Connecter a inbox.
			(status,nbMessages) = mail.select('INBOX')
			print("connecter inbox")
			
			#Rechercher message dans expediteur
			result, data = mail.uid('search', None, (dico.get(destinataire)))
			#result, data = mail.uid('search', None, '(FROM "lecagnois")')
			i = len(data[0].split()) # data[0] supprime espace
			Totalmsg = re.findall('\d+', str(nbMessages))[0]
			print (result + ' Nombre de messages = ' + str(Totalmsg))
			talkBlocking("il y a  au total "+str(Totalmsg)+ " messages dans ta boite mail ")
			print("trouver : " +str(i))
			talkBlocking("jai trouver " + str(i) + " message de " + destinataire )

			for x in range(i):
				latest_email_uid = data[0].split()[x] # ID unique étiquette sélectionnée
				result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
				# Récupérer le corps de courrier électronique pour l'ID donné
				raw_email = email_data[0][1]

				# boucle 1 
				raw_email_string = raw_email.decode('utf-8')
				# Convertit  d'octet en chaîne 
				email_message = email.message_from_string(raw_email_string)

				#boucler à travers toutes les multiparties disponibles dans le mail
				for part in email_message.walk():
					if part.get_content_type() == "text/plain": # ignore html
						body = part.get_payload(decode=True)
						print(body.decode('utf-8'))
						Mreponse = (body.decode('utf-8'))
						talkBlocking("message " + str(x+1) +". "+ Mreponse)
					if part.get_content_type() == "multipart/mixed" : # ignore piece jointe
						 body = part.get_payload(decode=False)
						
					else:
						continue
        
			if i == 0 :
				print("pas de messages")
				talkBlocking("pas de message a bientot")
			#fermeture IMAP
			print ("deconnecter du serveur")
			imaplib.IMAP4.close
			imaplib.IMAP4.logout
		
	except IOError:
		talkBlocking("le serveur est hors service")
	except OSError:
		talkBlocking("oups il y a une erreur")
	except ValueError:
		talkBlocking("oups il y a une erreur ")
	except:
		print(sys.exc_info()[0])
		raise

       

