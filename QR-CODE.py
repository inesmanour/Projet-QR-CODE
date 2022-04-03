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
    global mat
    toLoad=pil.Image.open("test_coin.png")
    mat=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]= 0 if toLoad.getpixel((j,i)) == 0 else 1
    return mat

def rotate_gauche():
    global mat
    mat_res = [[0, 0, 0, 0] * nbrLig(mat) for i in range (nbrCol(mat))]
    for i in range (nbrLig(mat_res)):
        for j in range (nbrCol(mat_res)):
            mat_res [i][j] = mat [i][nbrCol(mat)-1-i]

def carre_de_base():
    """Matrice de pixels qui crée un carré noir de 3x3 pixels enrouré d'une bande 
    blanche entourée d'une bande noire entourée d'une bande blanche à droite et en bas"""
    global coin_H_G, coin_B_G, coin_H_D
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

    coin_B_G= [[1,1,1,1,1,1,1,] ,
              [0,0,0,0,0,0,0, 1], 
              [0,1,1,1,1,1,0,1], 
              [0,1,0,0,0,1,0,1] ,
              [0,1,0,0,0,1,0,1], 
              [0,1,0,0,0,1,0,1], 
              [0,1,1,1,1,1,0,1],
              [0,0,0,0,0,0,0,1]]

    return coin_H_G , coin_B_G , coin_H_D


def trouver_carre():
    """Fonction qui trouve le coin dans lequel le carre_de_base n'apparait 
    pas et retourne l'image pour avoir les 3 carrés dans les bons coins"""
    global mat
    for i in range (18, 25):
        for j in range (18, 25):
            while mat [i][j] == coin_H_G or mat [i][j] == coin_H_D or mat [i][j] == coin_B_G:
                rotate_gauche("test_coin.png")

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
