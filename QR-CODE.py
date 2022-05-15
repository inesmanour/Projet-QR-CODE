####################################################
# Groupe LDDBI
# Inès MANOUR
# Sofia TERKI
# Chargée de TD : Coline GIANFROTTA
# https://github.com/uvsq22104096/Projet_QR_Code.git
####################################################

from ast import If, Pass
import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog
from operator import xor


## création des différentes fonctions

#fonctions de base vues en cours
def nbrCol(matrice):
    """Fonction qui renvoie le nombre de colonnes d'une matrice"""
    return len(matrice[0])

def nbrLig(matrice):
    """Fonction qui renvoie le nombre de lignes d'une matrice"""
    return len(matrice)

def saving(matPix, filename):
    """Fonction qui sauvegarde l'image contenue dans matpix dans le fichier filename . Il faut 
    utiliser une extension png pour que la fonction fonctionne sans perte d'information"""
    toSave=pil.Image.new(mode = "1", size = (nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j,i),matPix[i][j])
    toSave.save(filename)

def loading(filename):
    """Fonction qui charge le fichier image filename et renvoie une 
    matrice de 0 et de 1 qui représente l'image en noir et blanc"""
    toLoad=pil.Image.open(filename)
    mat=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]= 0 if toLoad.getpixel((j,i)) == 0 else 1
    return mat


def rotate_gauche(matrice):
   """Fonction qui permet de faire une rotation de 90° à gauche""" 

   global mat_res
   mat_res = [[0] * nbrLig(matrice) for i in range (nbrCol(matrice))]
   for i in range (nbrCol(matrice)):
       for j in range (nbrLig(matrice)):
           mat_res [i][j] = matrice [j][nbrCol(matrice)-1-i]
   saving(mat_res, "test.png")
   return mat_res 


#fonctions crées pour la lecture des QR code

def carre_de_base():
    """Matrice de pixels qui crée un carré noir de 3x3 pixels 
    enrouré d'une bande blanche entourée d'une bande noire 
    entourée d'une bande blanche à droite et en bas """
    # en essayant d'appeler cette fonction dans la fonction 
    # trouver_coin, cette dernière ne fonctionnait pas, on 
    # a donc préférer recréer le carré directement dans la fonction trouver_coin

    carre = [0, 0, 0, 0, 0, 0, 0, 
             0, 1, 1, 1, 1, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 0, 0, 0, 0]
    return carre


def trouver_coin():
    """Fonction qui trouve le coin dans lequel le carre_de_base n'apparait 
    pas et retourne l'image pour avoir les 3 carrés dans les bons coins"""
    global mat
    cpt=0 
    carre = [0, 0, 0, 0, 0, 0, 0, 
             0, 1, 1, 1, 1, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 0, 0, 0, 0]
    
    mat = loading(image_courante)

    #récupération du coin en bas à droite de notre QR code 
    coin_B_D = []
    for i in range (18, 25):
        for j in range (18, 25):
            coin_B_D.append(mat[i][j])

    # faire des rotations pour bien placer le QR code 
    # et avoir les 3 coins bien placés
    while cpt <3:
        if carre == coin_B_D :  
            mat=rotate_gauche(mat)
            coin_B_D =[]
            for i in range (18, 25):
                for j in range (18, 25):
                    coin_B_D.append(mat[i][j])
        cpt+=1

    bon_qr_code = mat  
    
    # sauvegarder la matrice du QR code après rotation dans une nouvelle image
    saving(bon_qr_code, "trouver_coin.png")
    return bon_qr_code
    

def trouver_lignes():
    """Fonction qui vérifie que les 2 lignes qui relient
    les carrés des 3 coins apparaisent bien """
    global mat
    mat = loading(image_courante)
    qr_code =[]
    cpt =0
    ligne = [0,1,0,1,0,1,0,1,0]
    
    m_H = []
    m_V = []
    for i in range(8, 16):
        m_H.append(mat[6][i])
        m_V.append(mat[i][6])

    # faire des rotations pour bien placer le QR code 
    # et avoir les 2 lignes bien placées
    while cpt<3:
        if m_H != ligne or m_V != ligne :
            mat = rotate_gauche(mat)
            m_H = []
            m_V = []
            for i in range(8, 16):
                m_H.append(mat[6][i])
                m_V.append(mat[i][6])
        cpt+=1
    qr_code = mat

    # sauvegarder la matrice du QR code après rotation dans une nouvelle image
    saving(qr_code, "trouver_ligne.png")
    return qr_code

########################################################################
# on a essayé d'utiliser la fonction nombre de blocs pour ne lire qu'un certain 
# nombre de blocs mais ça ne marche pas donc on a gardé la fonction qui lit 16 blocs qui est plus bas
"""def lecture_bloc(mat):  
    """ Fonction qui parcourt l’image d’un QR code pour renvoyer 
    l’information lue sous la forme d’une liste de listes de 14 bits"""

    global grande_liste, cpt, liste_bloc, bloc, i , j, condition
    #compteur du nombre de blocs lus
    bloc = 0
    # liste qui va contenir 14 bits
    liste_bloc = []    
    #liste contenant les sous listes de 14 bits
    grande_liste=[]  
    #variable qui compte le nombre de bits lus
    cpt=0

    # initialiser à 24 pour démarrer la lecture en bas a droite
    i=25     
    j=24 

    # nombre de blocs qu'il faut lire
    nb_blocs_exact = nbr_de_blocs(qr_code_filtre)
    if (nb_blocs_exact // 2) % 2 == 0:
        condition = True
    else:
        condition = False

    while bloc < 16: #pour lire au maximum 8 séries de 2 blocs
        if bloc % 4 == 0:
            lecture_droite_gauche(mat)
        else:
            lecture_gauche_droite(mat)

    decoupage_liste(grande_liste)
    recuperer_messages(liste_7_bits)
    type_de_donnees(message)"""
   

"""def lecture_droite_gauche(mat): 
    """Fonction pour lire les blocs de droite à gauche"""
    global cpt, grande_liste, liste_bloc,i, j, condition, bloc  
    for k in range (2):
        # lecture premier bloc de 7 bit)
        if k==0 :
            #ajout du 1er bit
            i = i-1    
            liste_bloc.append(mat[i][j])
            cpt+=1
            while cpt <14: 
                # ajout des 13 prochains bits de ma sous liste de 14 bits 
                if cpt%2 != 0:  
                    # mouvement en haut             
                    i=i-1                      
                    bit= mat [i][j] 
                    liste_bloc.append(bit)
                    cpt+=1
                else:
                    # mouvment en bas
                    i=i+1    
                    # puis mouvement a gauche                 
                    j=j-1
                    bit = mat [i][j]
                    liste_bloc.append(bit) 
                    cpt+=1  
            
            # ajout de la sous liste de 14 bits = un bloc
            grande_liste.append(liste_bloc)
            # un bloc en plus a été lu
            bloc+=1    
            # réinitialisation de la liste bloc et du compteur de bits         
            liste_bloc = []
            cpt = 0
            
        # lecture du second bloc
        else:   
            if condition == True:
                break
            else:
                while cpt<14:
                    if cpt%2 == 0:
                        # mouvement en bas
                        i=i+1                    
                        bit= mat [i][j] 
                        liste_bloc.append(bit)
                        cpt+=1
                    else:
                        # mouvement en haut
                        i=i-1  
                        # puis mouvement a gauche                   
                        j=j-1
                        bit = mat [i][j]
                        liste_bloc.append(bit)
                        cpt+=1   

                # ajout de sous liste de 14 bits = une bloc
                grande_liste.append(liste_bloc)    
                # réinitialisation de la liste bloc et du compteur de bits
                liste_bloc = []
                cpt = 0
                # une fois que un bloc a été lu
                bloc += 1  """
    
    
"""def lecture_gauche_droite(mat):
    """Fonction pour lire les blocs de gauche à droite"""
    global cpt, grande_liste, liste_bloc, bloc, i, j 

    for k in range (2):
        # lecture du premier bloc
        if k==0:  
            # ajout du 1er bit
            i = i-1    
            liste_bloc.append(mat[i][j])
            cpt+=1
            while cpt<14:
                # ajout des 13 prochains bits de ma sous liste de 14 bits  
                if cpt%2 != 0:   
                    i = i-1    
                    liste_bloc.append(mat[i][j])
                    cpt+=1 
                else:     
                    # mouvment en bas 
                    i=i+1                     
                    # puis mouvement à droite
                    j=j+1    
                    bit= mat [i][j] 
                    liste_bloc.append(bit)
                    cpt+=1
            
            # ajout de la sous liste de 14 bits = un bloc
            grande_liste.append(liste_bloc)
            # un bloc en plus a été lu
            bloc+=1
            # réinitialisation de la liste bloc et du compteur de bits
            liste_bloc = []
            cpt = 0

        # lecture du deuxieme bloc
        else :   
            if condition == False:
                break
            else:
                while cpt <14:
                    #ajout des 13 prochains bits
                    if cpt%2 == 0:    
                        i = i-1    
                        liste_bloc.append(mat[i][j])
                        cpt+=1    
                    else:  
                        # mouvment en bas
                        i=i+1 
                        # puis mouvement à droite                     
                        j=j+1    
                        bit= mat [i][j] 
                        liste_bloc.append(bit)
                        cpt+=1
            
                # ajout de la sous liste de 14 bits = une bloc
                grande_liste.append(liste_bloc)
                # un boc en plus a été lu
                bloc+=1
                # réinitialisation de la liste bloc et du compteur de bits
                liste_bloc = []
                cpt = 0"""

########################################################################
def lecture_bloc(mat):  
    """ Fonction qui parcourt l’image d’un QR code pour renvoyer 
    l’information lue sous la forme d’une liste de listes de 14 bits"""

    global serie, grande_liste, cpt, bloc, i , j
    #compteur du nombre de séries de 2 blocs lues
    serie = 0
    # liste qui va contenir 14 bits
    bloc = []    
    #liste contenant les sous listes de 14 bits
    grande_liste=[]  
    #variable qui compte le nombre de bits lus
    cpt=0

    # initialiser à 24 pour démarrer la lecture en bas a droite
    i=25     
    j=24 

    while serie < 8: #pour lire au maximum 8 séries de 2 blocs
        if serie % 2 == 0:
            lecture_droite_gauche(mat)
        else:
            lecture_gauche_droite(mat)

    decoupage_liste(grande_liste)
    recuperer_messages(liste_7_bits)
    type_de_donnees(message)
   

def lecture_droite_gauche(mat): 
    """Fonction pour lire les blocs de droite à gauche"""
    global serie, cpt, grande_liste, bloc,i, j  
    for k in range (2):
        # lecture premier bloc de 7 bit)
        if k==0 :
            #ajout du 1er bit
            i = i-1    
            bloc.append(mat[i][j])
            cpt+=1
            while cpt <14: 
                # ajout des 13 prochains bits de ma sous liste de 14 bits 
                if cpt%2 != 0:  
                    # mouvement en haut             
                    i=i-1                      
                    bit= mat [i][j] 
                    bloc.append(bit)
                    cpt+=1
                else:
                    # mouvment en bas
                    i=i+1    
                    # puis mouvement a gauche                 
                    j=j-1
                    bit = mat [i][j]
                    bloc.append(bit) 
                    cpt+=1  
            
            # ajout de la sous liste de 14 bits = un bloc
            grande_liste.append(bloc)    
            # réinitialisation de la liste bloc et du compteur de bits         
            bloc = []
            cpt = 0
            
        # lecture du second bloc
        else:   
            while cpt<14:
                if cpt%2 == 0:
                    # mouvement en bas
                    i=i+1                    
                    bit= mat [i][j] 
                    bloc.append(bit)
                    cpt+=1
                else:
                    # mouvement en haut
                    i=i-1  
                    # puis mouvement a gauche                   
                    j=j-1
                    bit = mat [i][j]
                    bloc.append(bit)
                    cpt+=1   

            # ajout de sous liste de 14 bits = une bloc
            grande_liste.append(bloc)    

            # réinitialisation de la liste bloc et du compteur de bits
            bloc = []
            cpt = 0
    # une fois que deux blocs ont été lus
    serie += 1  
    
    
def lecture_gauche_droite(mat):
    """Fonction pour lire les blocs de gauche à droite"""
    global serie, cpt, grande_liste, bloc, i, j 

    for k in range (2):
        # lecture du premier bloc
        if k==0:  
            # ajout du 1er bit
            i = i-1    
            bloc.append(mat[i][j])
            cpt+=1
            while cpt<14:
                # ajout des 13 prochains bits de ma sous liste de 14 bits  
                if cpt%2 != 0:   
                    i = i-1    
                    bloc.append(mat[i][j])
                    cpt+=1 
                else:     
                    # mouvment en bas 
                    i=i+1                     
                    # puis mouvement à droite
                    j=j+1    
                    bit= mat [i][j] 
                    bloc.append(bit)
                    cpt+=1

            # ajout de la sous liste de 14 bits = un bloc
            grande_liste.append(bloc)

            # réinitialisation de la liste bloc et du compteur de bits
            bloc = []
            cpt = 0

        # lecture du deuxieme bloc
        else :   
            while cpt <14:
                #ajout des 13 prochains bits
                if cpt%2 == 0:    
                    i = i-1    
                    bloc.append(mat[i][j])
                    cpt+=1    
                else:  
                    # mouvment en bas
                    i=i+1 
                    # puis mouvement à droite                     
                    j=j+1    
                    bit= mat [i][j] 
                    bloc.append(bit)
                    cpt+=1
            
            # ajout de la sous liste de 14 bits = une bloc
            grande_liste.append(bloc)

            # réinitialisation de la liste bloc et du compteur de bits
            bloc = []
            cpt = 0

    # une fois que deux blocs ont été lus
    serie+=1


def decoupage_liste(grande_liste):
    """Fonction qui permet de découper la liste des blocs 
    lus (14 bits) en deux listes de 7 blocs pour pouvoir 
    appliquer le code de Hamming (7,4) par la suite """
    global liste_7_bits
    #liste contenant des sous-listes de 7 bits
    liste_7_bits = []

    for liste in grande_liste:
        liste_7_bits.append(liste[0:7])
        liste_7_bits.append(liste[7:])

#######################################################################
def decoder_Hamming(bits):
    """Fonction qui prend en entrée une liste de 7 bits 
    (4bits de message + 3 bits de correcton) et qui renvoie 
    les 4 bits de message après correction"""

    p1 = bits[0] ^ bits[1] ^ bits[2] 
    p2 = bits[0] ^ bits[2] ^ bits[3]
    p3 = bits[1] ^ bits[2] ^ bits[3]

    #position de l'erreur s'il y en a une (0 sinon)
    num = int(p1!=bits[0]) + int(p2 != bits[1])*2 + int(p3!=bits[3])*4 

    #si la position de l'erreur est sur la position 
    #d'un bit de message on corrige
    if (num == 3):
        bits[0] = int (not bits[0])
        #print("correction d'un pixel corrompu 1\n")
    if (num == 5):
        bits[1] = int (not bits[1])
        #print("correction d'un pixel corrompu 2\n")
    if (num == 6):
        bits[2] = int (not bits[2])
        #print("correction d'un pixel corrompu 3\n")
    if (num == 7):
        bits[3] = int (not bits[3])
        #print("correction d'un pixel corrompu 4\n")
    return bits[:4]

def recuperer_messages(liste_7_bits):
    """Fonction qui récupère les 4 bits de messages 
    après correction s'il y avait une erreur"""
    global message
    # liste qui va contenir les sous_listes de 4 bits de 
    # message obtenus après décodage de Hamming
    message = []
    for elem in liste_7_bits:
        message.append(decoder_Hamming(elem))
    

##################################################################
def type_de_donnees(message):
    pix = mat[24][8]
    donnees = []
    liste = []
    if pix == 0:
        for elem in message:  
            donnees.append(hex(int(elem, 2)))  
    elif pix == 1:
        k = 0
        while k < nbrLig(message):
            #pour avoir une liste de 8 bits de message
            liste.append(message[k]+message[k+1])
            k+=2
        for elem in liste:
            donnees.append(chr(conversionEntier(elem)))
    print("données=", donnees)



####################################################################
def filtres(mat):
    """Fonction qui choisit le filtre en fonction 
    des bits de contrôle et applique le filtre"""
    global qr_code_filtre

    pix1 = mat[22][8]
    pix2 = mat[23][8]

    #filtre tout noir
    if pix1 == 0 and pix2 == 0:
        filtre = [[0]*25] * 25
        print("filtre tout noir")

    #damier
    elif pix1 == 0 and pix2 == 1:
        filtre = []
        for i in range(25):
            if i%2 ==0:
                liste = [0,1,0,1]*6 +[0]
                filtre.append(liste)
            else:
                liste = [1,0,1,0]*6 +[1]
                filtre.append(liste)
        print("dammier")
    

    #filtre avec alternance lignes horizontales noires et lignes blanches            
    elif pix1 == 1 and pix2 == 0:
        filtre = [[0]*25, [1]*25] * 12 + [[0]*25]
        print("lignes horizontales")

    #filtre avec alternance lignes verticales noires et lignes blanches
    elif pix1 == 1 and pix2 == 1:
        filtre = [[0,1,0,1]*6 +[0]] * 25
        print("lignes verticales")
    
    
    # création de la liste qui contiendra les bits résultant du xor entre le QR code et le filtre
    qr_code_filtre = []
    for i in range (25):
        qr_code_filtre.append([0]*25)

    #application du filtre en faisant un XOR entre les pixels du filtre et ceux du QR code 
    for i in range(25):
        for j in range(25):
            qr_code_filtre[i][j] = (mat[i][j]) ^ (filtre[i][j])

    #saving(res, "filtre.png")
    print ("res=", qr_code_filtre)
    return qr_code_filtre

###########################################################################
def nbr_de_blocs(mat):
    """Fonction qui permet de ctocker le nombre de blocs à décoder"""
    #liste contenant les 5 bits codant 
    # pour le nombre de blocs à décoder
    liste = [mat[13][0],mat[14][0],mat[15][0],mat[16][0],mat[17][0]]

    nb_blocs = conversionEntier(liste)
    print("Le nombre de blocs à décoder est", nb_blocs)
    return nb_blocs

def conversionEntier(liste):
    """Fonction qui permet de convertire une 
    liste de bits (binaire) en décimal"""
    res = 0
    liste.reverse()
    for i in range (len(liste)):
        res+= liste[i]*(2**i)
    return res



##programme principal: 

#choix du QR code à lire
image_courante= "qr_code_ssfiltre_ascii_rotation.png"

#vérifier que le QR code est dans le bon sens
trouver_lignes()
trouver_coin()
#application du filtre pour avoir une image plus nette
filtres(mat) #essayer d'appliquer les filtres dans la fonction trouver coin!!!!!!!!!!!!!!!!!!!!!
#lecture du QR code
lecture_bloc(qr_code_filtre)
nbr_de_blocs(qr_code_filtre)


