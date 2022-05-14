####################################################
# Groupe LDDBI
# Inès MANOUR
# Sofia TERKI
# Chargée de TD : Coline GIANFROTTA
# https://github.com/uvsq22104096/Projet_QR_Code.git
####################################################

from ast import If
import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog


"""def lectures_bloc(mat):  
    """ Fonction qui parcourt l’image d’un QR code pour renvoyer 
    l’information lue sous la forme d’une liste de listes de 14 bits"""
    global serie, grande_liste, cpt, bloc, impair
    serie = 0
    #liste contenant les sous listes de 14 bits
    grande_liste=[]  
    # liste qui va contenir 14 bits
    bloc = []         
    cpt=0            
    bit = 0
    i=24     # initialiser à 24 pour démarrer la lecture en bas a droite 
    j=24 
    # ajout du premier bit de lecture en bas a droite dans laa liste de 14 bits
    bit = mat [i][j]    
    bloc.append(bit)

    while serie <= 8: #pour lire au maximum 8 séries de 2 blocs
        if serie % 2 == 0:
            lecture_droite_gauche()
        else:
            lecture_gauche_droite()"""


"""def lectures_droite_gauche(mat):
    """Fonction pour lire les blocs de droite à gauche"""
    global serie, cpt, grande_liste, bloc
    bit = 0
#pour la première série de blocs
    while serie <= 8:    # pour lire au plus 8 séries de 2 blocs
        for i in range (2):
            while cpt <14:                # ajout des 13 prochains bits de ma sous liste de 14 bits 
                cpt+=1 
                i=i-1                     # mouvement en haut 
                bit= mat [i][j] 
                bloc.append(bit)
   
                cpt+=1
                i=i+1                     # mouvment en bas 
                j=j-1                     # puis mouvement a gauche
                bit = mat [i][j]
                bloc.append(bit)   
            grande_liste.append(bloc)             # ajout de sous liste de 14 bits = une bloc
            bloc = []
            cpt = 0
        serie += 1"""   #on crée fonction lecture droite gauche et fonction gauche droite on impose condition sur serie paire ou impaire

"""def lectures_gauche_droite(mat):
    """Fonction pour lire les blocs de gauche à droite"""
    global serie, cpt, grande_liste, bloc
    while 14 < cpt < 28:    
        """i -= 1    # pour pouvoir lire le 1er bit
        bloc.append(mat[i][j])
        i -= 1    #pour pouvoir lire le 2e bit
        bloc.append(mat[i][j])
        cpt+=1"""       #problème ça va se refaire à chaque fois #demander quand on monte de 2 pixels si on monte ou on descend
        i=i+1                     # mouvment en bas 
        j=j+1    # puis mouvement a droite
        bit= mat [i][j] 
        bloc.append(bit)
    grande_liste.append(bloc)
    cpt = 0"""







carre = []
image_courante= "qr_code_ssfiltre_ascii_rotation.png"


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


def rotate_gauche():
    mat=loading(image_courante)
    mat_res = [[0, 0, 0, 0] * nbrLig(mat) for i in range (nbrCol(mat))]
    for i in range (nbrLig(mat_res)):
        for j in range (nbrCol(mat_res)):
            mat_res [i][j] = mat [i][nbrCol(mat)-1-i]



def carre_de_base():
    """Matrice de pixels qui crée un carré noir de 3x3 pixels enrouré d'une bande 
    blanche entourée d'une bande noire entourée d'une bande blanche à droite et en bas"""
    #global carre
    """carre = [[0,0,0,0,0,0,0],
             [0,1,1,1,1,1,0],
             [0,1,0,0,0,1,0],
             [0,1,0,0,0,1,0],
             [0,1,0,0,0,1,0],
             [0,1,1,1,1,1,0], 
             [0,0,0,0,0,0,0]]"""
    carre = [0, 0, 0, 0, 0, 0, 0, 
             0, 1, 1, 1, 1, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 0, 0, 0, 0]
    #return carre


def trouver_coin():
    """Fonction qui trouve le coin dans lequel le carre_de_base n'apparait 
    pas et retourne l'image pour avoir les 3 carrés dans les bons coins"""
    carre = [0, 0, 0, 0, 0, 0, 0, 
             0, 1, 1, 1, 1, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 0, 0, 0, 0]
    mat = loading(image_courante)
    coin_B_D = []
    for i in range (18, 25):
        for j in range (18, 25):
            coin_B_D.append(mat[i][j])
    print(coin_B_D)
    if coin_B_D == carre:
        rotate_gauche()
    saving(mat, "photo.png")
    #return matrice
    
    

def trouver_lignes():
    """Fonction qui vérifie que les 2 lignes qui relient
    les carrés des 3 coins apparaisent bien """
    mat = loading(image_courante)
    ligne_horizontale = [0,1,0,1,0,1,0,1,0]
    ligne_verticale =[[0],[1],[0],[1],[0],[1],[0],[1],[0]]
    m_H = []
    m_V = []
    for i in range(8, 16):
        m_H.append(mat[6][i])
        m_V.append(mat[i][6])
    if m_H != ligne_horizontale or m_V != ligne_verticale:
        rotate_gauche()
    saving(mat, "image.png")


def lecture_bloc(mat):  
    """ Fonction qui parcourt l’image d’un QR code pour renvoyer 
    l’information lue sous la forme d’une liste de listes de 14 bits"""
    global serie, grande_liste, cpt, bloc, impair
    serie = 0
    #liste contenant les sous listes de 14 bits
    grande_liste=[]  
    # liste qui va contenir 14 bits
    bloc = []         
    cpt=0            
    i=24     # initialiser à 24 pour démarrer la lecture en bas a droite 
    j=24 
    # ajout du premier bit de lecture en bas a droite dans laa liste de 14 bits
    bit = mat [i][j]    
    bloc.append(bit)

    while serie <= 8:
        if serie % 2 == 0:
            lecture_droite_gauche()
        else:
            lecture_gauche_droite()


def lecture_droite_gauche(mat):
    """Fonction pour lire les blocs de droite à gauche"""
    global serie, cpt, grande_liste, bloc
#pour la première série de blocs
    while serie <= 8:    # pour lire au plus 8 séries de 2 blocs
        for i in range (2):
            while cpt <14:                # ajout des 13 prochains bits de ma sous liste de 14 bits 
                cpt+=1 
                i=i-1                     # mouvement en haut 
                bit= mat [i][j] 
                bloc.append(bit)
   
                cpt+=1
                i=i+1                     # mouvment en bas 
                j=j-1                     # puis mouvement a gauche
                bit = mat [i][j]
                bloc.append(bit)   
            grande_liste.append(bloc)             # ajout de sous liste de 14 bits = une bloc
            bloc = []
            cpt = 0
        serie += 1   #on crée fonction lecture droite gauche et fonction gauche droite on impose condition sur serie paire ou impaire

def lecture_gauche_droite(mat):
    """Fonction pour lire les blocs de gauche à droite"""
    global serie, cpt, grande_liste, bloc
    while 14 < cpt < 28:    
        """i -= 1    # pour pouvoir lire le 1er bit
        bloc.append(mat[i][j])
        i -= 1    #pour pouvoir lire le 2e bit
        bloc.append(mat[i][j])
        cpt+=1"""       #problème ça va se refaire à chaque fois #demander quand on monte de 2 pixels si on monte ou on descend
        i=i+1                     # mouvment en bas 
        j=j+1    # puis mouvement a droite
        bit= mat [i][j] 
        bloc.append(bit)
    grande_liste.append(bloc)
    cpt = 0



# programme principal
#print(trouver_coin())
print(trouver_lignes())

######################################################################################################
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

image_courante= "qr_code_ssfiltre_ascii_rotation.png"


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
   global mat_res # ne pas initialiser avec un mat=Loading(image_courante sinon lors de la 2e rotation on reviens sur initiale et n'enregistre pas la premiere rotation 
   mat_res = [[0] * nbrLig(matrice) for i in range (nbrCol(matrice))]
   for i in range (nbrCol(matrice)):
       for j in range (nbrLig(matrice)):
           mat_res [i][j] = matrice [j][nbrCol(matrice)-1-i]
   saving(mat_res, "test.png")
   return mat_res 



def carre_de_base():
    """Matrice de pixels qui crée un carré noir de 3x3 pixels enrouré d'une bande 
    blanche entourée d'une bande noire entourée d'une bande blanche à droite et en bas"""
    global carre
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
    global mat_res
    global bon_qr_code, mat
    cpt=0 
    carre = [0, 0, 0, 0, 0, 0, 0, 
             0, 1, 1, 1, 1, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 0, 0, 0, 1, 0,
             0, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 0, 0, 0, 0]
    
    
    mat = loading(image_courante)
    coin_B_D = []
    for i in range (18, 25):
        for j in range (18, 25):
            coin_B_D.append(mat[i][j])
    print(coin_B_D,'print de trouver coin')
    
    while cpt <3:
        if carre == coin_B_D :  # boucle pour ne pas que ca s'arrte au premier rotate mais fin d'arret qd c'est bien placer:
            mat=rotate_gauche(mat)
            coin_B_D =[]
            for i in range (18, 25):
                for j in range (18, 25):
                    coin_B_D.append(mat[i][j])
        cpt+=1
    bon_qr_code = mat # use toto qu'on return pour utiliser notre image avec le coin vide bien placé ensuite 
  
    saving(bon_qr_code, "photo.png")
    return bon_qr_code
    
    
    
def trouver_lignes():
    """Fonction qui vérifie que les 2 lignes qui relient
    les carrés des 3 coins apparaisent bien """
    mat = loading(image_courante)
    qr_code =[]
    cpt =0
    ligne = [0,1,0,1,0,1,0,1,0]
    
    m_H = []
    m_V = []
    for i in range(8, 16):
        m_H.append(mat[6][i])
        m_V.append(mat[i][6])

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
    print("hello")
    saving(qr_code, "code.png")
    return qr_code

########################################################################


##################################################
def lecture_bloc(mat):  
    """ Fonction qui parcourt l’image d’un QR code pour renvoyer 
    l’information lue sous la forme d’une liste de listes de 14 bits"""
    global serie, grande_liste, cpt, bloc, i , j
    serie = 0
    #liste contenant les sous listes de 14 bits
    grande_liste=[]  
    # liste qui va contenir 14 bits
    bloc = []         
    cpt=0
    # initialiser à 24 pour démarrer la lecture en bas a droite
    i=25     
    j=24 
    while serie < 8: #pour lire au maximum 8 séries de 2 blocs
        if serie % 2 == 0:
            lecture_droite_gauche(mat)
        else:
            lecture_gauche_droite(mat)
    return grande_liste
   




def lecture_droite_gauche(mat): ### faire meme concept que le gauche droite
    """Fonction pour lire les blocs de droite à gauche a partir de la seconde itération"""
    global serie, cpt, grande_liste, bloc,i, j  #pour la première série de blocs
    """i = 25
    j = 24
    bloc = []
    cpt = 0
    grande_liste = []
    serie = 0"""
    for k in range (2):
        if k==0 :# lecture premier bloc de 7 bit)
            i = i-1    # pour pouvoir lire le 1er bit
            bloc.append(mat[i][j])
            cpt+=1
            while cpt <14: 
                if cpt%2 != 0:               # ajout des 13 prochains bits de ma sous liste de 14 bits 
                    i=i-1                     # mouvement en haut 
                    bit= mat [i][j] 
                    bloc.append(bit)
                    cpt+=1
                else:
                    i=i+1                     # mouvment en bas
                    j=j-1
                     # puis mouvement a gauche
                    bit = mat [i][j]
                    bloc.append(bit) 
                    cpt+=1  
                #print(cpt) 
            
            grande_liste.append(bloc)             # ajout de sous liste de 14 bits = une bloc
            bloc = []
            cpt = 0
            
        else:  # lecture du second bloc 
            while cpt<14:
                if cpt%2 == 0:
                    i=i+1                     # mouvement en bas
                    bit= mat [i][j] 
                    bloc.append(bit)
                    cpt+=1
                else:
                    i=i-1                     # mouvment en haut
                    j=j-1
                    print("j=", j)                     # puis mouvement a gauche
                    bit = mat [i][j]
                    bloc.append(bit)
                    cpt+=1   
                print(cpt)


            grande_liste.append(bloc)             # ajout de sous liste de 14 bits = une bloc
            bloc = []
            cpt = 0
    serie += 1  
    
    



def lecture_gauche_droite(mat):
    """Fonction pour lire les blocs de gauche à droite"""
    global serie, cpt, grande_liste, bloc, i, j 

    for k in range (2):
        
        if k==0:  # condition pour lire le premier bloc 
            i = i-1    # pour pouvoir lire le 1er bit
            bloc.append(mat[i][j])
            cpt+=1
            while cpt<14: 
                if cpt%2 != 0:   
                    i = i-1    #pour pouvoir lire le 2e bit
                    bloc.append(mat[i][j])
                    cpt+=1 
                else:     
                    i=i+1                     # mouvment en bas 
                    j=j+1    # puis mouvement a droite
                    bit= mat [i][j] 
                    bloc.append(bit)
                    cpt+=1

            grande_liste.append(bloc)
            bloc = []
            cpt = 0

        else :  # lecture du deuxieme bloc (--> serie complete de 2 blocs lues) 
            while cpt <14:
                if cpt%2 == 0:    
                    i = i-1    #pour pouvoir lire le 2e bit
                    bloc.append(mat[i][j])
                    cpt+=1    
                else:  
                    # mouvment en bas
                    i=i+1 
                    # puis mouvement a droite                     
                    j=j+1    
                    print("j=", j)
                    bit= mat [i][j] 
                    bloc.append(bit)
                    cpt+=1
            grande_liste.append(bloc)
            bloc = []
            cpt = 0
    serie+=1

def decoupage_liste(grande_liste):
    global liste_7_bits
    liste_7_bits = []
    for liste in grande_liste:
        liste_7_bits.append(liste[0:7])
        liste_7_bits.append(liste[7:])
    #print("liste de 7 bits= ", liste_7_bits)

######################################################################################
def decoder_Haming(bits): #en entrée on a une liste de 7 bits messages + correction
    """La fonction décoder doit renvoyer le message corrigé s'il y a erreur"""
    p1 = bits[0] ^ bits[1] ^ bits[2] 
    p2 = bits[0] ^ bits[2] ^ bits[3]
    p3 = bits[1] ^ bits[2] ^ bits[3]

    #position de l'erreur s'il y en a une (0 sinon)
    num = int(p1!=bits[0]) + int(p2 != bits[1])*2 + int(p3!=bits[3])*4 #pour avoir la position de l'erreur en décimale d'où *2 et *4

    #si la position de l'erreur est sur la position d'un bit de message on corrige
    #not c comme booléen renvoie 0 ou 1
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
    message = []
    for elem in liste_7_bits:
        message.append(decoder_Haming(elem))
    #print("message= ", message)

#######################################################################################
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

"""J'ai essayé de faire la question 5 mais je ne suis pas sûre d'avoir vraiment compris ce qui 
est demandé et en plus je ne sais pas trop comment lire 8bits par 8bits """

#######################################################################################
def filtres(mat):
    """Fonction qui choisit le filtre en fonction 
    des bits de contrôle et applique le filtre"""
    global filtre
    pix1 = mat[22][8]
    pix2 = mat[23][8]

    #filtre tout noir
    if pix1 == 0 and pix2 == 0:
        filtre = [[0]*25] * 25
        application_filtre()

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
        application_filtre()

    #filtre avec alternance lignes horizontales noires et lignes blanches            
    elif pix1 == 1 and pix2 == 0:
        filtre = [[0]*25, [1]*25] * 12 + [[0]*25]
        application_filtre()

    #filtre avec alternance lignes verticales noires et lignes blanches
    elif pix1 == 1 and pix2 == 1:
        filtre = [[0,1,0,1]*6 +[0]] * 25
        application_filtre()

def application_filtre(mat):
    """Fonction qui permet d'appliquer le filtre en faisant 
    un XOR entre les pixels du filtre et ceux du QR code"""
    res = []
    for i in range(25):
        for j in range(25):
            res.append(mat[i][j] ^ filtre[i][j])
    saving(res, "filtre.png")
    return res

###########################################################################
"""def nbr_series(mat):
    liste = [mat[13][0],mat[14][0],mat[15][0],mat[16][0],mat[17][0]]
    nbserie = conversionEntier(liste)
    print("Le nommbre de blocs à décoder est", nb_blocs)
    return nb_blocs"""

def conversionEntier(liste):
    """Fonction """
    res = 0
    liste.reverse()
    for i in range (len(liste)):
        res+= liste[i]*(2**i)
    return res



# programme principal
#print(trouver_lignes())
trouver_coin()
print(lecture_bloc(mat))
decoupage_liste(grande_liste)
recuperer_messages(liste_7_bits)
type_de_donnees(message)
