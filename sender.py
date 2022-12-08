print("""Bonjour Bienvenue dans votre repertoire téléphonique !\n
0- Quitter
1- Ecrire dans le répertoire
2- Rechercher dans le répertoire
""")
data=[]
fichier_donnee = open('data.txt', 'r+')
def addUser():
      askprenom=input('Entrez le prénom du nouveau contact :  ')
      asknom=input('Entrez le nom du nouveau contact :  ')
      asknum=input('Entrez le numéro du nouveau contact :  ')
      dict1={}
      dict1["nom"]=asknom
      dict1["prenom"]=askprenom
      dict1["num"]=asknum
      data.append(dict1)
      fichier_donnee.write(asknom + "," + askprenom + "," + asknum + "\n")
      print("Utilisateur Ajouté(e)")
for i in fichier_donnee:
    prenom,nom,num = i.split(",")
    dict_={"nom":nom, "prenom":prenom, "num":num}
    data.append(dict_)

def searchUser(nom):
      # ici les .lower() serve a rendre insensible à la casse
      for i in data:
            if i["nom"].lower() == nom.lower():
                  print(i["num"])
                  break
            elif i["prenom"].lower() == nom.lower():
                  print(i["num"])
                  break
            else:
                  ask_2 = input("Se nom n'existe pas... Voulez vous l'ajouter ?")
                  if ask_2 == "oui" or "Oui" or "y":
                        addUser()
                        break
                  else:
                        break

def prettyListUser():
      pass

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