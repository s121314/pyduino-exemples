#!/usr/bin/python
# -*- coding: utf-8 -*-

# exemple pyDuino - par X. HINAULT - www.mon-club-elec.fr
# Juillet 2013 - Tous droits réservés - GPLv3
# voir : https://github.com/sensor56/pyDuino

# Serveur TCP générant une page HTML + Javascript affichant un graphique avec la librairie dygraphs.

from pyduino import * # importe les fonctions Arduino pour Python

# entete declarative

ipLocale=Ethernet.localIP() # auto - utilise l'ip de l'interface eth0 du systeme
 
#ipLocale='192.168.2.3' # manuel - attention : utiliser la meme IP qu'une interface reseau du systeme
# pour connaitre les interfaces reseau sur le systeme : utiliser la commande $ ifconfig

print ipLocale # affiche l'adresse IP 

port=8080 # attention port doit etre au dessus de 1024 sinon permission refusee par securite - 8080 pour http

serverHTTP=EthernetServer(ipLocale, port) # crée un objet serveur utilisant le port 8080 = port HTTP > 1024

#--- setup --- 
def setup():
	global serverHTTP, ipLocale, port
	
	#serverHTTP.begin(10) # initialise le serveur - fixe nombre max connexion voulu
	serverHTTP.begin() # initialise le serveur - nombre max connexion par defaut = 5
	
	print ("Serveur TCP actif avec ip : " + ipLocale + " sur port : " + str(port) )
#--- fin setup

# -- loop -- 
def loop():
	
	global serverHTTP
	
	print ("Attente nouvelle connexion entrante...")
	clientDistant, ipDistante = serverHTTP.clientAvailable() # attend client entrant 
	# code bloque ici tant que pas client ! Si present, on recupere d'un coup objet client ET son ip
	
	print "Client distant connecte avec ip :"+str(ipDistante) # affiche IP du client

	#--- requete client ---
	requete=serverHTTP.readDataFrom(clientDistant) # lit les donnees en provenance client d'un coup
	
	print requete # affiche requete recue
	
	#--- reponse serveur --- 
	reponse=( # ( ... ) pour permettre multiligne.. 
	httpResponse() # entete http OK 200 automatique fournie par la librairie Pyduino
	
	# contenu page - ici date / heure du serveur et mesure nalogique A2
	+
	
	pageHTML() # voir la fonction separee - pour clarte du code
	
	+"\n") # fin reponse 
	
	serverHTTP.writeDataTo(clientDistant, reponse) # envoie donnees vers client d'un coup
	
	print "Reponse envoyee au client distant : "
	#print (bytes(reponse))
	print (reponse) # affiche la reponse envoyee
	
	#serverHTTP.close()
	# remarque : le socket = serveur doit rester ouvert
	
	# quand on quitte l'application: la connexion TCP reste active un peu donc erreur si re-execution trop rapide du code
	# on peut utiliser un port voisin dans ce cas... 

	delay(10) # entre 2 loop()
	
# -- fin loop --

#--- fonction fournissant la page HTML --- 
def pageHTML():
	
	# code Python a executer avant envoyer page 
	
	# donnees types
	dataGraph=""
	
	# utiliser options plutot que premiere ligne 
	#dataGraph=(
	#"""
	#"Date,Temperature\\n" +
#""")
	
	# donnees sous forme d'une chaine
	# format "x,y\n"
	
	for i in range(1000):
		# format "x,y\n"
		dataGraph=dataGraph+"\""+str(i)+","+str(i)+"\\n \"+" + "\n" # le 2eme \n est dans la page HTML, le premier dans la chaine des donnees

	dataGraph=dataGraph+"\""+str(i)+","+str(i)+"\\n \"" + "\n" # derniere ligne sans le plus
	
	
	# donnees sous forme d'un tableau 
	# [ [1,10,100], [2,20,80], [3,50,60], [4,70,80] ]
	# dans ce cas, utiliser l'instruction labels:
	
	# attention : le plus est dans la chaine 
	
	# options du graphique Dygraph a utiliser
	optionsGraph="""
	labels: [ "x", "y="]
	"""
	pageHTML=( # debut page HTML 
"""
<!DOCTYPE html >
<html>
        <head>

        <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> <!-- Encodage de la page  -->

        <script language="javascript" type="text/javascript">
        <!-- 
                        
        // code javascript par X. HINAULT - www.mon-club-elec.fr - tous droits reserves - 2013 - GPL v3

        function path(jsFileNameIn) { // fonction pour fixer chemin absolu                              
			var js = document.createElement("script");
			js.type = "text/javascript";
			//js.src = " http://www.mon-club-elec.fr/mes_javascripts/dygraphs/"+jsFileNameIn; // <=== serveur externe - modifier chemin ++ si besoin
			//js.src = "http://127.0.0.1/javascript/dygraphs/"+jsFileNameIn; // serveur local
			//js.src = "javascript/rgraph/"+jsFileNameIn; // chemin local  - fichier doit etre a la racine serveur
			js.src = "http://"+window.location.hostname+":80"+"/javascript/dygraphs/"+jsFileNameIn; // si utilisation server http local port 80

			document.head.appendChild(js);                                  
			//alert(js.src); // debug

		} // fin fonction path


		//---- fichiers a charger ---                            
		path('dygraph-combined.js'); // fichier simplifiant acces a tous les fichiers de la librairie dygraph

		window.onload = function () { // au chargement de la page


			//var valeurs = new Array(102,511,255,127,63,32); // tableau valeurs par defaut


			colorSets = [ // definition des set de couleurs a utiliser
			['#284785', '#EE1111', '#8AE234'], // 1er jeu de couleur - couleur utilisee dans ordre trace des courbes
			['rgb(255,0,0)', 'rgb(0,255,0)', 'rgb(0,0,255)'], // 2eme jeu de couleur - format rgb
			null
			]

			g = new Dygraph( // cree l'objet du graphique

			// containing div
			document.getElementById("graphdiv"), // objet div utilise appele par son nom

			// CSV ou chemin fichier CSV.

			// donnees valides au format x,y1, y2, ..., yn \n
			// x = horodatage ou chiffre
			// horodatages valides : voir http://dygraphs.com/data.html#csv
"""
	+ 
	dataGraph 
	+
""",

			//-- parametres a utiliser pour le graphique
			{
"""
	+ 
	optionsGraph
	+
"""
			} // fin parametres


			); // fin declaration Dygraph


		} // fin onload
		
	
	-->      
    </script>  

    <title>Test Dygraphs</title>

    </head>

    <body>

    <div id="graphdiv"></div>
    <br />
    Test de graphique Dygraphs : affichage de 1000 valeurs y=x


    </body>
</html>          
"""
)  # fin page HTML
	return pageHTML # la fonction renvoie la page HTML



#--- obligatoire pour lancement du code -- 
if __name__=="__main__": # pour rendre le code executable 
	setup() # appelle la fonction setup
	while not noLoop: loop() # appelle fonction loop sans fin
