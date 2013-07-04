#!/usr/bin/python
# -*- coding: utf-8 -*-

# exemple pyDUino - par X. HINAULT - www.mon-club-elec.fr
# Juin 2013 - Tous droits réservés - GPLv3
# voir : https://github.com/sensor56/pyDuino

# LED clignote avec delayMicroseconds

from pyduino import * # importe les fonctions Arduino pour Python

# entete declarative
LED=2  # declare la broche a utiliser

#--- setup --- 
def setup():
	pinMode(LED,OUTPUT) # met la broche en sortie
	Serial.println("La broche " +str(LED)+ " est en sortie !")

# -- fin setup -- 

# -- loop -- 
def loop():
	
	digitalWrite(LED,HIGH) # allume la LED
	Serial.println("La LED est allumee !") 
	
	delayMicroseconds(100000) # pause en microsecondes
	
	digitalWrite(LED,LOW) # eteint la LED
	Serial.println("La LED est eteinte !") 
	
	delayMicroseconds(100000) # pause en microsecondes
	

# -- fin loop --

#--- obligatoire pour lancement du code -- 
if __name__=="__main__": # pour rendre le code executable 
	setup() # appelle la fonction setup
	while not noLoop: loop() # appelle fonction loop sans fin




