#!/usr/bin/python
# -*- coding: utf-8 -*-

# exemple pyDuino - par X. HINAULT - www.mon-club-elec.fr
# Aout 2013- Tous droits réservés - GPLv3
# voir : https://github.com/sensor56/pyDuino

# Creer un fichier de donnees horodatees de test sur 24H

from pyduino import * # importe les fonctions Arduino pour Python
import datetime # pour operations facilitees sur date/heure

# entete declarative
noLoop=True

#--- setup --- 
def setup():
	
	myDataPath=("data/text/")
	
	path=homePath()+myDataPath  # chemin du répertoire à utiliser
	filename="test1440.txt" # nom du fichier
	filepath=path+filename # chemin du fichier
	
	print filepath
	
	if exists(filepath):
		print "Le fichier existe : le contenu va etre efface"
	else :
		print "Le fichier n'existe pas : le fichier va etre cree"
	
	# date/heure de reference
	refTime=datetime.datetime.strptime(today("/",-1),"%Y/%m/%d") # creation datetime.datetime de reference - date jour a minuit
	print refTime
	
	#myFile=open(filepath,'a') # ouverture pour ajout de texte
	myFile=open(filepath,'w') # ouverture pour ecriture avec effacement contenu
	
	#-- ajout de chaines au fichier 
	
	for t in range(1440) : # defile 1440 minutes theoriques
		dataValue=str(random(0,1023)) # genere une valeur aleatoire entiere
		
		dataTime=refTime+datetime.timedelta(0, t*60) # jours, secondes - ici toutes les minutes
		# l'utilisation de datetime et timedelta permet une manipulation simplifiee des intervalles de dates 
		
		# format de donnees utilise : aaaa/mm/jj HH:MM:SS , val \n
		dataLine=str(dataTime)+","+dataValue+"\n" # format datetime aaaa/mm/jj HH:MM:SS
		#print dataLine - debug
		myFile.write(dataLine) # ecrit la ligne dans le fichier
	
	myFile.close() # fermeture du fichier en ecriture
	
	#-- lecture du fichier -- 
	myFile=open(filepath,'r') # ouverture en lecture
	print ("Contenu du fichier : ")
	myFile.seek(0) # se met au debut du fichier
	print myFile.read() # lit le fichier
	
	myFile.close() # fermeture du fichier
	
	# NB : on peut aussi ouvrir le fichier dans l'editeur pour verifier son contenu 
	
# -- fin setup -- 

# -- loop -- 
def loop():
	return  # si vide
	
# -- fin loop --

#--- obligatoire pour lancement du code -- 
if __name__=="__main__": # pour rendre le code executable 
	setup() # appelle la fonction main
	while not noLoop: loop() # appelle fonction loop sans fin




