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

def searchUser():
      


for i in fichier_donnee:
    prenom,nom,num = i.split(",")
    dict_={"nom":nom, "prenom":prenom, "num":num}
    data.append(dict_)
#print(data)

while True:
  
  ask = input("Quel est votre choix ? ")

  if ask == "0":
    print("Merci d'avoir utilisé RepPhone, au revoir !")
    break
  
  elif ask == "1":
    addUser()
  elif ask == "2":
        
    