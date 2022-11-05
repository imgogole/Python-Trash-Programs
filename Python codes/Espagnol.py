from random import *
from difflib import SequenceMatcher
import os
from json import dump

# Après une forte envie de ne pas apprendre son vocabulaire,
# I'm Gogole décida de code un programme pour le lui faire apprendre
# Par contre si tu veux apprendre sans te faire questionner bah juste...
# Non... j'avais la flemme.
# Et si tu veux d'autre vocabulaire, pareil.

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

#Keys must be spanish
#Values must be french
#If you inverse them, the programm will consider spanish as french and and vice versa
voc = {
    "El entorno" : "L'environnement",
    "Tener papeles" : "Avoir les papiers",
    "Indocumentado/Sin papeles" : "Sans-papier/Sans papier",
    "Cambiar" : "Changer",
    "Encontrar" : "Trouver",
    "Burlarse de" : "Se moquer de",
    "Echar de menos" : "Manquer",
    "Un juego de palabras" : "Un jeu de mot",
    "Acostumbrarse" : "S'habituer",
    "Integrarse" : "S'intégrer",
    "Rechazar" : "Rejeter",
    "El rechazo" : "Le rejet",
}
#voc = dump() blabla

class Points :
    points = 0

vocEsp = []
vocFr = []

def AreStringsAlmostEquals(x, y) :
    return SequenceMatcher(a = x, b = y).ratio()
   
for key, value in zip(voc.keys(), voc.values()) :
    vocEsp.append(key.lower())
    vocFr.append(value.lower())

def ask(ch = 0) :
    choice = randint(0, len(voc.keys()) - 1)
    language = ch
    if ch == 0 :
        language = randint(1, 2)
    if language == 1 :
        #Espagnol => Français
        question = vocEsp[choice].capitalize()
        answer = vocFr[choice].split("/")
        ans = input(f"(Espagnol) {question} => ")
        hasAnswer = False
        for ansP in answer :
            if AreStringsAlmostEquals(ans.lower().strip(), ansP.strip()) > 0.87 :
                hasAnswer = True
        if hasAnswer :
            Points.points += 1
            a = ", mais cela s'écrit \"" + '" or "'.join(answer) + "\"" if AreStringsAlmostEquals(ans.lower().strip(), ansP.strip()) != 1.0 else ''
            print(f"=== Bonne réponse{a}")
        else :
            print(f"=== Mauvaise réponse : {'/'.join(answer).capitalize()}")
    elif language == 2 :
        #Français => Espagnol
        question = vocFr[choice].capitalize()
        answer = vocEsp[choice].split("/")
        ans = input(f"(Français) {question} => ")
        hasAnswer = False
        for ansP in answer :
            if AreStringsAlmostEquals(ans.lower().strip(), ansP.strip()) > 0.87 :
                hasAnswer = True
        if hasAnswer :
            Points.points += 1
            a= ", mais cela s'écrit \"" + '" or "'.join(answer) + "\"" if AreStringsAlmostEquals(ans.lower().strip(), ansP.strip()) != 1.0 else ''
            print(f"=== Bonne réponse{a}")
        else :
            print(f"=== Mauvaise réponse : {'/'.join(answer).capitalize()}")
T = True

while T :
    Points.points = 0
    ans = int(input("Que voulez-vous apprendre ?\n(1) Espagnol => Français\n(2) Français => Espagnol\n(3) Les deux\n(4) Hardcore mode, j'ai très envie de me faire défoncer.\n(5) J'ai fini\nVotre réponse : "))
    if ans == 1 :
        for i in range(20) :
            ask(1)
        print(f"Vous avez fait {Points.points} bonnes réponses sur 20.")
    elif ans == 2 :
        for i in range(20) :
            ask(2)
        print(f"Vous avez fait {Points.points} bonnes réponses sur 20.")
    elif ans == 3 :
        for i in range(20) :
            ask()
        print(f"Vous avez fait {Points.points} bonnes réponses sur 20.")
    elif ans == 4 :
        print("==================================================")
        print("Mode HARDCORE")
        print("==================================================")
        for i in range(1, 51) :
            ask()
            input(">>> Appuyez sur entrée pour continuer")
            os.system("cls")
        print(f"Vous avez fait {Points.points} bonnes réponses sur 50.")
    else :
        print("T'es le meilleur, tu vas réussir.\nN'abandonne pas :)")
        T = False
