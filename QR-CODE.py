####################################################
# Groupe LDDBI
# Inès MANOUR
# Sofia TERKI
# Chargée de TD : Coline GIANFROTTA
# https://github.com/uvsq22104096/Projet_QR_Code.git
####################################################

import tkinter as tk

def carre_de_base():
    """Matrice de pixels qui crée un carré noir de 3x3 pixels 
    enrouré d'une bande blanche entourée d'une bande noire"""
    matrice = [[(0,0,0,0)]*7] * 7
    for i in range (2, 6):
        matrice[1][i] = (255, 255, 255, 255) 
        matrice[5][i] = (255, 255, 255, 255)
        matrice[i][1] = (255, 255, 255, 255)
        matrice[i][5] = (255, 255, 255, 255)
    return matrice

def fonction():
    matrice1 = [[(255, 255, 255, 255)]*7]*7
    for j in range (len(matrice1)):
        matrice1[0][j] = (0,0,0,0)
        matrice1[j][0] = (0,0,0,0)
        matrice1[5][j] = (0,0,0,0)
        matrice1[j][5] = (0,0,0,0)
    for i in range (2, 5):
        for e in range(2, 5):
            matrice1[i][e] = (0,0,0,0)
    return matrice1

print(fonction())
