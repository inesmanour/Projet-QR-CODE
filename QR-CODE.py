####################################################
# Groupe LDDBI
# Inès MANOUR
# Sofia TERKI
# Chargée de TD : Coline GIANFROTTA
# https://github.com/uvsq22104096/Projet_QR_Code.git
####################################################

import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 

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


def carre_de_base():
    """Matrice de pixels qui crée un carré noir de 3x3 pixels enrouré d'une bande 
    blanche entourée d'une bande noire entourée d'une bande blanche à droite et en bas"""

    coin_H_G = [[0,0,0,0,0,0,0,1],
                [0,1,1,1,1,1,0,1],
                [0,1,0,0,0,1,0,1],
                [0,1,0,0,0,1,0,1],
                [0,1,0,0,0,1,0,1],
                [0,1,1,1,1,1,0,1], 
                [0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1]]
    

    coin_H_D=[[1, 0,0,0,0,0,0,0],
              [1,0,1,1,1,1,1,0],
              [1,0,1,0,0,0,1,0], 
              [1,0,1,0,0,0,1,0],
              [1,0,1,0,0,0,1,0],
              [1,0,1,0,0,0,1,0],
              [1,0,1,1,1,1,1,0],
              [1,0,0,0,0,0,0,0]]

    coin_B_G= [[1,1,1,1,1,1,1,1] ,
               [0,0,0,0,0,0,0,1], 
               [0,1,1,1,1,1,0,1], 
               [0,1,0,0,0,1,0,1] ,
               [0,1,0,0,0,1,0,1], 
               [0,1,0,0,0,1,0,1], 
               [0,1,1,1,1,1,0,1],
               [0,0,0,0,0,0,0,1]]

    return coin_H_G , coin_B_G , coin_H_D


  

def qr_code_de_base():
    "matrice de pixels 25 sur 25 originel avec les 4 coins bien placés et les 2 lignes qui relient les coins "
    qr_code= [[0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0],
          [0,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 0,1,1,1,1,1,0],
          [0,1,0,0,0,1,0, 1,1,1,1,1,1,1,1,1,1,1, 0,1,0,0,0,1,0],
          [0,1,0,0,0,1,0, 1,1,1,1,1,1,1,1,1,1,1, 0,1,0,0,0,1,0],
          [0,1,0,0,0,1,0, 1,1,1,1,1,1,1,1,1,1,1, 0,1,0,0,0,1,0],
          [0,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0, 1,0,1,0,1,0,1,0,1,0,1, 0,0,0,0,0,0,0],

          [1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],

          [0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [0,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [0,1,0,0,0,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [0,1,0,0,0,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [0,1,0,0,0,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [0,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1],
          [0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1]]

   
def test_image():
    " test de l'image  pour voir s'il correspond bien au qr code de base "

              
# if l'image toload( dans le cas ou les coins ne st pas a leur place)correspond qr code de base rien faire 
# else : changer les coordonnes des coins pour les avoir bien place = deplacer par rotation
# pour cela placer un compteur :au maximum yaura 3 rotation psq dans le cas ou il ressemble pas a celui de base on l'arrete qd mm a 3
#on doit changer les 8 premieres col et lignes de chaque coins , le reste que des 1 =white pas besoin de chnagements
#on sait que ya 4 possibilité de coins vides donc 4 conditions de rotation avec un 
#
#  faire translation vers la droite 
#mettre un tampon du qr load quon va tester pour prendre les partie quon veut puisq lors de la rotation les coins auront plus leurs dernire bande blanche allant vers l'interieur ##

# exemple 
def translate():
    #i = nb ligne
    #j= nb colonne

    debut
    #tampon = qr_tester
    #change la valeur  de i pour aller directement sur les valeurs de i voulues !
    for i in range(x):
        # change la valeur  de j pour aller directement sur les valeurs de j voulues !
        for j in range (y):
            #change les valeurs de liste en i et j voulue !
            l[i][j]= # un truc
    condition tester si qr_testter== qr_base




    
def trouver_carre():
    """Fonction qui trouve le coin dans lequel le carre_de_base n'apparait 
    pas et retourne l'image pour avoir les 3 carrés dans les bons coins"""
    pass

def trouver_lignes():
    """Fonction qui vérifie que les 2 lignes qui relient
    les carrés des 3 coins apparaisent bien """
    pass

def code_de_Hamming(message): 
    """Fonction qui en entrée reçoit un message de 4 bits et et qui renvoie 
    une liste de 7 bits (4bits de message et 3 bits de contrôle)"""
    #calcul des bits de contrôle
    c1 = message[0] ^ message[1] ^ message[3]   
    c2 = message[0] ^ message[2] ^ message[3]
    c3 = message[1] ^ message[2] ^ message[3]
    #on positionne les bits de message et de contrôle
    res = [c1, c2 , message[0], c3, message[1], message[2], message[3]]
    return res

def decoder_Hamming(bits): 
    """Fonction qui en entrée a une liste de 7 bits et qui renvoie 
    les 4 bits d'informations obtenus après correction d'erreur"""

    #calcul des bits de parité
    p1 = bits[2] ^ bits[4] ^ bits[6] 
    p2 = bits[2] ^ bits[5] ^ bits[6]
    p3 = bits[4] ^ bits[5] ^ bits[6]
    #position de l'erreur s'il y en a une (0 sinon)
    num = int(p1!=bits[0]) + int(p2 != bits[1])*2 + int(p3!=bits[3])*4 

    if num in [3, 5, 6, 7]: #si la position de l'erreur est sur la position d'un bit de message on corrige
        bits[num-1] = int(not bits[num-1])  
        print("Correction d'un pixel corrompu en position " + str(num)+ "\n")
    return [bits[2], bits[4], bits[5], bits[6]]

------------
" une fonction qui parcourt l’image d’un QR code pour renvoyer l’information lue sous la forme d’une liste de listes de 14 bits"
def lecture_bloc(mat):  
    liste_bloc=[]   # grande liste contenant sous listes de 14 bits
    cpt=0            
    i=24             # initialiser a 24 24 pour demarrer en bas a droite la lecture 
    j=24 
    
    bit = mat [i][j]           # ajout du premier bit de lecture en bas a droite dans ma liste_tampon de 14bit
    liste_tampon.append(bit)
    
while cpt <14:                # ajout des 13 prochains bits de ma sous liste de 14bit 
    
    cpt+=1 
    j=j-1                  # mouvement a droite 
    bit= mat [i][j] 
    liste_tampon.append(bit)
   
    cpt+=1
    i=i-1                     # mouvment en haut 
    j=j+1                    # puis mouvement a droite  
    bit = mat [i][j]
    liste_tampon.append(bit)
    
liste_bloc.append(liste_tampon)             # ajout de sous liste de 14 bits = une bloc

while i!=0 and j!=0 :     # si nous nous ne trouvons pas a la fin de la lecture , lecture du prochain bloc 
    liste_tampon=[]       # donc nouvelle liste vide qu'on remplira 
    
    while cpt <15:        # remplir avec 14bits notre nvlle sous liste de 14 bits 
    
    cpt+=1
    j=j-1       #mouvment a gauche 
    bit= mat [i][j] 
    liste_tampon.append(bit)
   
    if i=0:                     # une contrainte-> lorsqu'on est en haut pouvoir redescendre en bas pour continuer la lecture 
        cpt=cpt+1
        i=24                    # quand on est en bas -->ligne 24 psq la derniere ligne 
        j=j-1                   # but cela se fait que lorsque on a i=0 et j=j-1 
        bit=mat[i][j]
        liste_tampon.append(bit)
        cpt+=1   
        j=j-1                   #mouvment a gauche
        bit= mat [i][j] 
        liste_tampon.append(bit)
        
        
    cpt+=1          # si pas de contrainte continuer la lecture 
    i=i-1 
    j=j+1   
    bit = mat [i][j]
    liste_tampon.append(bit)
    
 liste_bloc.append(liste_tampon) # ajout des sous listes de 14 bits ( lecture de bloc) dans une grand liste 
  
######## lecture bloc fct 

def lecture_bloc(mat):  
    """ Fonction qui parcourt l’image d’un QR code pour renvoyer 
    l’information lue sous la forme d’une liste de listes de 14 bits"""
    global serie, grande_liste, cpt, bloc, impair , i , j , 
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

    '''la 1er lecture''' 
    #lecture des deux premiers blocs a part pcq porbleme quand faudra add le prochain premier bit donc initailiser la premiere lecture a part
    for k in range (2):
        while cpt <13:                # ajout des 13 prochains bits de ma sous liste de 14 bits 
            
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
        serie += 1 

    
    while serie <= 8: #pour lire au maximum 8 séries de 2 blocs
        if serie % 2 == 0:
            lecture_droite_gauche()
        else:
            lecture_gauche_droite()
   




def lecture_droite_gauche(mat): ### faire meme concept que le gauche droite
    """Fonction pour lire les blocs de droite à gauche a partir de la seconde itération"""
    global serie, cpt, grande_liste, bloc,i, j  #pour la première série de blocs
    
    i -= 1    # pour pouvoir lire le 1er bit
    bloc.append(mat[i][j])

    for k in range (2):

        if k==0 :# lecture premier bloc de 7 bit)
            while cpt <13:                # ajout des 13 prochains bits de ma sous liste de 14 bits 
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

        else:  # lecture du second bloc 
            while cpt<14:
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
            serie += 1  
    
    



def lecture_gauche_droite(mat):
    """Fonction pour lire les blocs de gauche à droite"""
    global serie, cpt, grande_liste, bloc, i, j 

    i -= 1    # pour pouvoir lire le 1er bit
    bloc.append(mat[i][j])
    
    for k in range (2):
        
        if k==0:  # condition pour lire le premier bloc 
            while cpt<13:    
                i -= 1    #pour pouvoir lire le 2e bit
                bloc.append(mat[i][j])
                cpt+=1      

                i=i+1                     # mouvment en bas 
                j=j+1    # puis mouvement a droite
                bit= mat [i][j] 
                bloc.append(bit)

            grande_liste.append(bloc)
            bloc = []
            cpt = 0

        else :  # lecture du deuxieme bloc (--> serie complete de 2 blocs lues) 
            while cpt<14:    
                i -= 1    #pour pouvoir lire le 2e bit
                bloc.append(mat[i][j])
                cpt+=1      

                i=i+1                     # mouvment en bas 
                j=j+1    # puis mouvement a droite
                bit= mat [i][j] 
                bloc.append(bit)


            grande_liste.append(bloc)
            bloc = []
            cpt = 0
            serie+=1

   
    
     

   
    
    
    
    
 
        
        
   
