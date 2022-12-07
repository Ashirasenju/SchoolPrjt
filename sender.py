# Importation UI





# Exécution du choix 2
def searchUser():
  pass
# Ici on ouvre le fichier de donnée
fichier_donnee = open('data.txt', 'r+')
# On créé un tableau vide nommé 'data'

# parcourir chaques valeurs du fichier data.txt ; les séparer par des virgules ; les mettre dans un dictionnaire nommé dict et ajouté chaques dictionnaires à la liste data.


# Création du menu des choix
print("""Bonjour Bienvenue dans votre repertoire téléphonique !\n
0- Quitter
1- Ecrire dans le répertoire
2- Rechercher dans le répertoire
""")
# ici on créer une boucle infini afin d'effectuer pour une interface utilisateur simple
# la commande necéssaire s'active selon le choix de l'utilisateur
while True:
  data=[]
  ask = input("Quel est votre choix ? ")
  # Arret de la boucle si le choix est 0
  if ask == "0":
    print("Merci d'avoir utilisé RepPhone, au revoir !")
    break
  elif ask == "1":
    def addUser():
      askprenom=input('Entrez le prénom du nouveau contact :  ')
      asknom=input('Entrez le nom du nouveau contact :  ')
      asknum=input('Entrez le numéro du nouveau contact :  ')
      dict["nom":asknom, "prenom":askprenom, "num":asknum]
      data.append(dict)
      for x in data:
        print(x)
    addUser()
    break
  
  
  elif ask == "2":
    for i in fichier_donnee:
      nom,prenom,num = i.split(",")
      dict = {"nom" : nom, "prenom": prenom, "num": num}
      data.append(dict)
      print(data)

  else:
    print("Ce choix n'existe pas")

