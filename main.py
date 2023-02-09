import csv
from random import randint

#début de sélection aléatoire de 30 questions
def lecture_fichier(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        return [ligne for ligne in csv.reader(fichier)]


qcm = lecture_fichier("QCM.txt")
select = []
questions = []

while len(select) < 30:
    e= randint(0,29)
    if e not in select:
        select.append(e)


for x in select:
    q = qcm[x]

    questions.append(q)

#fin de sélection.
#Les questions choisies sont stockées dans la liste 'questions'

#Commence à poser les questions et demander les réponses
score=0
nb=0

for quest in questions:
    nb+=1
    a = quest[0]
    a=a.split(';;')
    question, reponse = a[0].split("A-")
    print('Question n°',nb, ' : ',"A-",question)
    print(reponse)
    
    rep = input("Entrez votre réponse : ")
    if rep == a[1]:
        print('Bonne réponse')
        score+=1
    else:
        print('Mauvaise réponse')

print("Vous avez",score,"bonne réponses sur 30")
input()
