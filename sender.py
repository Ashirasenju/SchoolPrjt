# Importation

# Definition des fonctions
def addUser():
    pass
  
def searchUser():
  pass
# Ici on ouvre le fichier de donnée
fichier_donnee = open('data.txt', 'r+')
# On créé un tableau vide nommé 'data'
data = []
# # parcourir chaques valeurs du fichier data.txt ; les séparer par des virgules ; les mettre dans un dictionnaire nommé dict et ajouté chaques dictionnaires à la liste data.
for i in fichier_donnee:
  nom,prenom,num = i.split(",")
  dict = {"nom" : nom, "prenom": prenom, "num": num}
  data.append(dict)
print(data)
# Création du menu des choix
print("""Bonjour Bienvenue dans votre repertoire téléphonique !\n
0- Quitter
1- Ecrire dans le répertoire
2- Rechercher dans le répertoire
""")
# ici on créer une boucle infini afin d'effectuer pour une interface utilisateur simple
# la commande necéssaire s'active selon le choix de l'utilisateur
while True:
  ask = input("Quel est votre choix ? ")
  # Arret de la boucle si le choix est 0
  if ask == "0":
    print("Merci d'avoir utilisé RepPhone, au revoir !")
    break
  if ask == "1":
    addUser()
  elif ask == "2":
    searchUser()
#coucou