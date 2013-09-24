#!/usr/bin/python
# -*- coding: utf-8 -*-

# exemple pyDuino - par X. HINAULT - www.mon-club-elec.fr
# Juin 2013 - Tous droits réservés - GPLv3
# voir : https://github.com/sensor56/pyDuino

# test Listfiles

from pyduino import * # importe les fonctions Arduino pour Python

# entete declarative
noLoop==True

#--- setup --- 
def setup():
	
	#dirPath=homePath() 
	dirPath=homePath()+"data/text"
	print dirPath
	
	for filename in listfiles(dirPath):
		print filename
	
	
# -- fin setup -- 

# -- loop -- 
def loop():
	return  # si vide
	
# -- fin loop --

#--- obligatoire pour lancement du code -- 
if __name__=="__main__": # pour rendre le code executable 
	setup() # appelle la fonction main
	while not noLoop: loop() # appelle fonction loop sans fin




