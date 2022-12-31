
#Creation du menu
print("""Bonjour Bienvenue dans votre repertoire téléphonique !\n
0- Quitter
1- Ecrire dans le répertoire
2- Rechercher dans le répertoire
3- Lister les contacts
""")
data=[]
#ouverture du fichier data.txt correspondant au repertoire telephonique 
fichier_donnee = open('data.txt', 'r+')

#creation de la fonction permettant d'ajouter un contact au repertoire telephonique
def addUser():
      # Demande des données à travèrs des inputs
      askprenom=input('Entrez le prénom du nouveau contact :  ')
      asknom=input('Entrez le nom du nouveau contact :  ')
      asknum=input('Entrez le numéro du nouveau contact :  ')
      dict1={}
      dict1["nom"]=asknom
      dict1["prenom"]=askprenom
      dict1["num"]=asknum
      # Assignation des données au dictionnaire
      data.append(dict1)
      # Ecriture des données sur le fichier
      fichier_donnee.write(asknom + "," + askprenom + "," + asknum + "\n")
      print("Utilisateur Ajouté(e)")
for i in fichier_donnee:
    prenom,nom,num = i.split(",")
    dict_={"nom":nom, "prenom":prenom, "num":num}
    data.append(dict_)

#creation de la fonction permettant de rechercher un contact et d'en ajouter si le contact n'existe pas
def searchUser(nom):
      # ici les .lower() servent à rendre insensible à la casse(donc ca ne tient pas compte des majuscules et minuscules )
      for i in data:
            if i["nom"].lower() == nom.lower():
                  print(i["num"])
                  break
            elif i["prenom"].lower() == nom.lower():
                  print(i["num"])
                  break
            else:
                  ask_2 = input("Ce nom n'existe pas... Voulez vous l'ajouter ?")
                  if ask_2 == "oui" or "Oui" or "y":
                        addUser()
                        break
                  else:
                        break
# Creation d'une fonction supplementaire permettant simplement de voir la liste de contact de manière agréable.
def prettyListUser():
      for i in data:
            name = i["nom"]
            first_name = i["prenom"]
            Numero = i["num"]
            print(f"{name} {first_name} -> {num}")      

while True:
  
  ask = input("Quel est votre choix ? ")

  if ask == "0":
    print("Merci d'avoir utilisé RepPhone, au revoir !")
    break
  
  elif ask == "1":
    addUser()
  elif ask == "2":
    n = input("Quelle est le nom à chercher ?")
    searchUser(n)
  elif ask == "3":
      prettyListUser()