#!/usr/bin/python
# -*- coding: utf-8 -*-

# exemple pyDuino - par X. HINAULT - www.mon-club-elec.fr
# Juillet 2013 - Tous droits réservés - GPLv3
# voir : https://github.com/sensor56/pyDuino

# tester un code secret saisi dans un numpad

#from pyduino import * # importe les fonctions Arduino pour Python
from pyduinoMultimedia import * # importe les fonctions Arduino pour Python

# entete declarative
code="*123+"
#--- setup --- 
def setup():
  return  # si vide 
	
# -- fin setup -- 

# -- loop -- 
def loop():
	
	# try.. except.. permet d'éviter le blocage si erreur de saisie
	try: 
		reponse=raw_input("Veuillez saisir le code : ")
	except: # erreur
		print ("Veuillez recommencer !")
		return  # sort de la fonction loop
	
	print ("Vous avez saisi : " + reponse ) 
	
	if reponse==code :
		print ("Code bon !")
		pass
	else : 
		print ("Code faux !")
		return # sort de loop
	
	# si le code est bon on se trouve ici...
	print ("Felicitations ! ")
	
	# stoppe loop
	global noLoop
	noLoop=True 
	
# -- fin loop --

#--- obligatoire pour lancement du code -- 
if __name__=="__main__": # pour rendre le code executable 
	setup() # appelle la fonction main
	while not noLoop: loop() # appelle fonction loop sans fin




