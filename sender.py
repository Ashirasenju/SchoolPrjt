# Importation

# Definition des fonctions
def addUser():
    pass
  
def searchUser():
  pass
# Ici on ouvre le fichier de donnée
fichier_donnee = open('data.txt', 'r+')
data = []
for i in fichier_donnee:
  nom,prenom,num = i.split(",")
  dict = {"nom" : nom, "prenom": prenom, "num": num}
  data.append(dict)
print(data)

print("""Bonjour Bienvenue dans votre repertoire téléphonique !\n
0- Quitter
1- Ecrire dans le répertoire
2- Rechercher dans le répertoire
""")
# ici on créer une boucle infini afin d'effectuer pour une interface utilisateur simple
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
