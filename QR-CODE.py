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
    #coin en haut à gauche
    coin_H_G = [[0,0,0,0,0,0,0,1],
                [0,1,1,1,1,1,0,1],
                [0,1,0,0,0,1,0,1],
                [0,1,0,0,0,1,0,1],
                [0,1,0,0,0,1,0,1],
                [0,1,1,1,1,1,0,1], 
                [0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1]]
    
    #coin en haut à droite
    coin_H_D=[[1,0,0,0,0,0,0,0],
              [1,0,1,1,1,1,1,0],
              [1,0,1,0,0,0,1,0], 
              [1,0,1,0,0,0,1,0],
              [1,0,1,0,0,0,1,0],
              [1,0,1,0,0,0,1,0],
              [1,0,1,1,1,1,1,0],
              [1,0,0,0,0,0,0,0]]

    #coin en bas à guauche
    coin_B_G=[[1,1,1,1,1,1,1,1],
              [0,0,0,0,0,0,0,1], 
              [0,1,1,1,1,1,0,1], 
              [0,1,0,0,0,1,0,1],
              [0,1,0,0,0,1,0,1], 
              [0,1,0,0,0,1,0,1], 
              [0,1,1,1,1,1,0,1],
              [0,0,0,0,0,0,0,1]]

    return coin_H_G , coin_B_G , coin_H_D


def trouver_coin():
    """Fonction qui trouve le coin dans lequel le carre_de_base n'apparait 
    pas et retourne l'image pour avoir les 3 carrés dans les bons coins"""
    global mat
    coin_B_D = []
    for i in range (17, 25):
        for j in range (17, 25):
            coin_B_D.append(mat[i][j])
            if coin_B_D == coin_B_G or coin_B_D == coin_H_D or coin_B_D == coin_H_G:
                rotate_gauche("test_coin.png")

def trouver_lignes():
    """Fonction qui vérifie que les 2 lignes qui relient
    les carrés des 3 coins apparaisent bien """
    global mat
    ligne_horizontale = [0,1,0,1,0,1,0,1,0]
    ligne_verticale =[[0],[1],[0],[1],[0],[1],[0],[1],[0]]
    m_H = []
    m_V = []
    for i in range(8, 16):
        m_H.append(mat[6][i])
        m_V.append(mat[i][6])
    if m_H != ligne_horizontale or m_V != ligne_verticale:
        rotate_gauche("test_coin.png")
