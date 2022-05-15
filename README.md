# Projet-QR-CODE
######################

Chargé de TD: Coline Gianfrotta


**GROUPE LDDBI :

MANOUR INES 


TERKI SOFIA 

Lien du github : https://github.com/uvsq22103405/Projet-QR-CODE.git

######################

**Principe du projet :** 

   Le projet consiste à programmer un lecteur de QR code 
   
   
**Découpage du projet:**
	
	On a découpeé en 3 branches le projet pour une meilleur communication et partage de nos idées de code. 
	
	La branche principale qui est le main est le résultat final de notre programmation, accompagné de branches nommées Sofia et Ines permettant d'y mettre nos débuts de recherches sans marcher l'une sur l'autre. 


**Explication et détails du programme :**


***Structure générale*** : 

	-Import des librairies 
	
	-Définition des fonctions 
	
	-Programme principal

***Details et explications des fonctions :***

	-def nbrCol():
	"""Fonction qui renvoie le nombre de colonnes d'une matrice"""

	-def nbrLig( ):
	"""Fonction qui renvoie le nombre de lignes d'une matrice »""

	-def saving():
	"""Fonction qui sauvegarde l'image contenue dans matpix dans le fichier filename . Il faut 
    utiliser une extension png pour que la fonction fonctionne sans perte d'information"""

	-def loading():
	"""Fonction qui charge le fichier image filename et renvoie une 
    matrice de 0 et de 1 qui représente l'image en noir et blanc"""

	-def rotate_gauche():
	""Fonction qui permet de faire une rotation de 90° à gauche """

	-def carre_de_base():
	"""Matrice de pixels qui crée un carré noir de 3x3 pixels enrouré d'une bande 
    blanche entourée d'une bande noire entourée d'une bande blanche à droite et en bas s"""

	-def trouver_coin():
	"""Fonction qui trouve le coin dans lequel le carre_de_base n'apparait 
    pas et retourne l'image pour avoir les 3 carrés dans les bons coins"""

	-def trouver_lignes():
	"""Fonction qui vérifie que les 2 lignes qui relient
    les carrés des 3 coins apparaisent bien """

	-def lecture_bloc():  
	""" Fonction qui parcourt l’image d’un QR code pour renvoyer 
    l’information lue sous la forme d’une liste de listes de 14 bits"""

	-def lecture_droite_gauche():
	"""Fonction pour lire les blocs de droite à gauche""

	-def lecture_gauche_droite():
	"""Fonction pour lire les blocs de gauche à droite ""

	-def decoupage_liste( ):
	"" Fonction qui permet de découper la liste des blocs lus (14 bits) en deux listes de 7 blocs pour pouvoir appliquer le code Hamming (7,4) par la 		suite """

	-def decoder_Hamming( ) :
	""Fonction qui prend en entrée une liste de 7 bits ( 4 bits de message + 3 bits de correction) et qui renvoie les 4 bits de message de correction""

	-def recuperer_messages( ) :
	""Fonction qui récupère les 4 bits de messages après correction s’il a une erreur ""

	-def type_de_donnees():
	""Fonction qui permet de determiner le type de donées (numériques ou brutes ) et de convertir les bits en hexadecimal ou ASCII""

	-def filtres():
	"""Fonction qui choisit le filtre en fonction 
    des bits de contrôle et applique le filtre"""

	-def application_filtre():
	"""Fonction qui permet d'appliquer le filtre en faisant 
    un XOR entre les pixels du filtre et ceux du QR code"""


	-def nbr_de_blocs():
	"" Fonction qui permet de stocker le nombre de blocs à décoder"""

	-def conversionEntier():
	""Fonction qui permet de convertir une liste de bits (binaire) en décimal """
	
	
	
	
	
**Problèmes rencontrés:**
		
		-on a essayé d'utiliser la fonction nombre de blocs pour ne lire qu'un certain nombre de blocs mais cela ne marche pas , nous avons donc gardé la fonction qui lit 16 blocs qui est visible plus bas dans le code 
		- Lorsque nous essayons de décoder Le QR  code il ne contient pas une suite de valeurs hexadecimales qui commence par 14BAD mais par d'autre valeurs hexadecimales.



Signature: Ce programme a été réalisé par Sofia Terki et Inès Manour dans le cadre d’un projet du module IN202. 14/05/22



