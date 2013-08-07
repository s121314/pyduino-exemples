#!/usr/bin/python
# -*- coding: utf-8 -*-

# exemple pyDUino - par X. HINAULT - www.mon-club-elec.fr
# Juin 2013 - Tous droits réservés - GPLv3
# voir : https://github.com/sensor56/pyDuino

# test digitalRead

#from pyduino import * # importe les fonctions Arduino pour Python
from pyduinoMultimedia import * # importe les fonctions Arduino pour Python

# entete declarative
BP=2  # declare la broche a utiliser
APPUI=LOW # valeur broche lors appui

filepathAudio=""

#--- setup --- 
def setup():
  pinMode(BP,PULLUP) # met la broche en entree avec rappel au plus actif
	Serial.println("La broche 2 est en entree avec rappel au plus actif !")
	
	global filepathAudio, filename
	
	# exemples de sons :  wget -4 http://www.mon-club-elec.fr/mes_downloads/pyduino_sons.tar.gz
	
	filepathAudio=homePath()+sourcesPath(AUDIO)+"photo/"
	print filepathAudio
	

# -- fin setup -- 

# -- loop -- 
def loop():
	
	global filepathAudio, filename
	
	if(digitalRead(BP)==APPUI): # si appui
		Serial.println("Appui BP!")
		Serial.println("Joue le son :  " +filepathAudio+"camera-click-1.wav")
		playSound(filepathAudio+"camera-click-1.wav") # joue le son
		delay(250)  # anti-rebond
	
	delay(100) # pause entre 2 lecture du BP
	
# -- fin loop --

#--- obligatoire pour lancement du code -- 
if __name__=="__main__": # pour rendre le code executable 
	setup() # appelle la fonction main
	while(1): loop() # appelle fonction loop sans fin
