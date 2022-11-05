from random import randint
import json
import time as Time

StudentsName = ["GIRONDIN", "PRUNE", "XAVIER", "DE LAQUITAINE", "REFARD", "KAZER", "EMILIEN", "ROCHENAIN", "BIZENTIN", "KESPARD", "ARAMIN", "HADACH", "FRANCOIS", "DANIEL", "JULIA", "NARTIMES", "BLANC", "MULER", "FRIGIEL", "GIANT", "HAZIM"]
StudentsFirstname = ["Antoine", "Tom", "Thomas", "Pierre", "Stéphane", "Emma", "Emmanuel", "Julie", "Juliette", "Hugo", "Raphaël", "Gaspard", "Aurélien", "Emilien", "Maxime", "Max", "Justine", "Justin", "Eve", "Adam", "Mané"]

class Format :
    @staticmethod
    def Line(time = 1) :
        for _ in range(time) :
            print("=========================================================")
    @staticmethod
    def Taret(time = 1) :
        for _ in range(time) :
            print("_________________________________________________________")
    @staticmethod
    def Return(time = 1) :
        for _ in range(time) :
            print("\n", end = "")

class Classroom :
    Name = "Unnamed classroom"
    Graduation = 0
    Students = []
    isStudentsGenerated = False
    def __init__ (self, name) :
        self.Name = name
    def GenerateNewStudentsList(self) :
        del self.Students[:]
        for _ in range(15) :
            StudentAge = randint(15, 18)
            self.Students.append({"Nom" : StudentsName[randint(0, len(StudentsName) - 1)], "Prénom" : StudentsFirstname[randint(0, len(StudentsFirstname) - 1)], "Age" : StudentAge, "Marks" : None, "Warning" : 0})
        self.isStudentsGenerated = True
    def ShowStudents(self) :
        for i, student in zip(range(len(self.Students)), self.Students) :
            Say(f"({i}) Nom : {student['Nom']}, Prénom : {student['Prénom']}, Age : {student['Age']}")

class Student :
    FirstName = "Unnamed Student"
    LastName = "Unnamed Student"
    Age = 0
    GeneralMark = 0
    Warnings = 0
    def __init__ (self, fname, lname, age, gmark, wrn) :
        self.FirstName = fname
        self.LastName = lname
        self.Age = age
        self.GeneralMark = gmark
        self.Warnings = wrn

class InitMe :
    Name = "Unnamed Player"
    Firstname = "Unnamed Player"
    Gender = 0
    Age = 0
    Subject = 0
    Inventory = []
    Money = 0
    Appelation = "Mr"
    IsSick = False
    IsLate = False
    TimeLate = 0
    WasAbsent = False
    Mails = []
    MailsSended = []
    def __init__ (self, name, firstname, gender, subject) :
        self.Name = name
        self.Firstname = firstname
        self.Gender = gender
        self.Age = 30
        self.Subject = subject
        self.Money = 1500
        if gender == 0 :
            self.Appelation = "Mr"
        else :
            self.Appelation = "Mme"
    def ShowInventory(self) :
        Say(f"Argent : {self.Money}€")
        if len(self.Inventory) == 0 :
            Say("Inventaire (Vide)")
        else :
            Say(f"Inventaire ({len(self.Inventory)}) :")
            for i, item in zip(range(len(self.Inventory)), self.Inventory) :
                Say(f"  ({i}) x{item['Count']} {item['Name']}")
    def HasItem(self, name, count = 1) :
        if len(self.Inventory) == 0 :
            return False
        for item in self.Inventory :
            if item["Name"] == name and item["Count"] >= count :
                return True
        return False
    def AddItem(self, name, count = 1) :
        hasAlreadyItem = False
        index = 0
        if len(self.Inventory) != 0 :
            for item in self.Inventory :
                if item["Name"] == name :
                    hasAlreadyItem = True
                    index = self.Inventory.index(item)
        if hasAlreadyItem :
            self.Inventory[index]["Count"] += count
        else :
            self.Inventory.append({"Name" : name, "Count" : count})
    def AddMail(self, subject, content) :
        self.Mails.append({subject: content})
    def WriteMail(self, subject, content) :
        self.MailsSended.append({subject: content})
    def DeleteMail(self, index, deleteAll = False) :
        if deleteAll :
            del self.Mails[:]
            Say("Deleted all mails")
        else :
            del self.Mails[index]
            Say(f"Deleted {index}th mail")
        
        
def Say(message) :

    """Print a message. Must be a string"""

    print(message)

def Ask(message) :

    """Ask to the user a question followed by two points in order to form your question.
    \nMessage is free"""

    answer = input(f"{message} : ")
    return answer

def Wait(message = "Appuyez sur Entrée pour continuer...") :
    return input(message)

def ForceAsk(message, answers) :

    """Ask to the user a question followed by many proposition.
    \nQuestion must be string and Answers must be an iterable. Return a number present the iterable. The function is looped if the user didn't responde by a number given in the available answers"""

    hasAnswered = False
    answersAvailable = ""
    for i, ans in zip(range(len(answers)), answers) :
        answersAvailable = answersAvailable + f"({i}) {ans}\n"
    while not hasAnswered :
        try :
            answer = int(input(f"{message} :\n{answersAvailable}Votre réponse : "))
            for i in range(len(answers)) :
                if answer == i :
                    hasAnswered = True
            if not hasAnswered :
                Format.Line()
                Say("Veillez répondre par les réponses données.")
                Format.Line()
        except :
            Format.Line()
            Say("Veillez répondre par les réponses données.")
            Format.Line()
    return answer

def Namation(name, isUpper = False) :
    name = name.replace(" ", "")
    if isUpper :
        return name.upper()
    else : 
        return name

def Credits() :
    Format.Line()
    Say("Class Room Simulator - by I'm Gogole")
    Format.Line()
    Format.Return()

def Loading() :
    time = randint(2, 8)
    tips = ["Vous avez des probabilités à chaque évenements qui déclencheront des possibilités à récuperer des items ou de l'argent."]
    tip = tips[randint(0, len(tips) - 1)]
    Say(f"Astuce : {tip}")
    Format.Line()
    Say("Chargement...")
    Format.Line()
    Time.sleep(time)

def Mail() :
    Format.Line(2)
    Say("Messagerie électronique")
    Ans = ForceAsk("Que souhaitez-vous faire aujourd'hui ? :)", [f"Lire mes mails ({len(Me.Mails)})", "Envoyer un mail", "Supprimer mes mails", "Quitter"])
    if Ans == 0 :
        Format.Line()
        Say("Lire vos messages.")
        Format.Line()
        Ans = int(Ans)
        if len(Me.Mails) == 0 :
            Say("Vous n'avez aucun mail")
            Wait()
            Mail()
            return
        else :
            for i in range(len(Me.Mails)) :
                mailName = list(Me.Mails[i].keys())[0]
                Say(f"  ({i}) Objet : {mailName}")
            Format.Line()
            Ans = ForceAsk(f"Que souhaitez vous lire ?", [*list(range(len(Me.Mails))), "Quitter"])
        if Ans == len(Me.Mails) :
            Mail()
            return
        else :
            mailName = list(Me.Mails[Ans].keys())[0]
            mailObject = list(Me.Mails[Ans].values())[0]
            Format.Line()
            Say(f"Object : {mailName}")
            Format.Taret()
            Say(f"     {mailObject}")
            Wait()
            Mail()
            return
    elif Ans == 1 :
        Format.Line()
        Say("Envoyez un message à votre établissement.")
        Format.Taret()
        isOk = False
        while not isOk :
            Object = Ask("Donnez un objet à votre mail")
            Message = Ask("Ecrivez votre message")
            Ans = ForceAsk("Voulez-vous envoyer votre message ?", ["Oui", "Hein ? Non ça va pas !", "Annuler"])
            if Ans == 0 :
                isOk = True
                Me.AddMail(Object, Message)
            elif Ans == 1 :
                pass
            elif Ans == 2:
                isOk = True
                Mail()
                return
        Say("Votre message a été envoyé avec succès !")
        Wait()
        Mail()
        return
    elif Ans == 2 :
        Format.Line()
        Say("Supprimer vos messages.")
        Format.Line()
        if len(Me.Mails) == 0 :
            Say("Vous n'avez aucun mail")
            Wait()
            Mail()
            return
        for i in range(len(Me.Mails)) :
            mailName = list(Me.Mails[i].keys())[0]
            Say(f"  ({i}) Objet : {mailName}")
        Format.Line()
        Ans = ForceAsk(f"Que souhaitez vous supprimer ?", [*list(range(len(Me.Mails))), "Tous supprimer", "Quitter"])
        if Ans == len(Me.Mails) :
            Me.DeleteMail(0, True)
            Mail()
            return
        elif Ans == len(Me.Mails) + 1 :
            Mail()
            return
        else :
            Me.DeleteMail(Ans)
            Mail()
            return
    elif Ans == 3 :
        Say("Vous quittez votre boîte mail, à bientôt !")
        Format.Line(2)
        return
        

Credits()
isOk = False
ClassesAvailable = ["Terminale","Première","Seconde"]
SubjectsAvailable = ["Français", "Philosophie", "Mathématiques", "Histoire Géographie", "Anglais", "Physiques", "SVT", "Vie scolaire"]
GendersAvailable = ["Homme", "Femme"]
AppelationGender = ["Mr", "Mme"]

while not isOk :

    NameClass = Ask("Commencez par donner un nom à votre nouvelle classe")
    MyClass = Classroom(NameClass)
    GraduationClassInt = ForceAsk("Choisissez une classe", ClassesAvailable)
    MyClass.Graduation = GraduationClassInt
    GraduationClass = ClassesAvailable[GraduationClassInt]
    Format.Line()
    isOkInt = ForceAsk(f"Bienvenue dans la classe {NameClass} de {GraduationClass} !", ["Super !", "J'ai besoin de modifier ma classe."])
    if isOkInt == 0 :
        isOk = True
        Format.Line()
        Say("Maintenant, essayons de se connaître.")
        Format.Line()

isOk = False

while not isOk :
    
    MyName = Ask("Donnez vous un nom de famille")
    MyName = Namation(MyName, True)
    MyFirstName = Ask("Donnez vous un prénom")
    MyFirstName = Namation(MyFirstName)
    GenderInt = ForceAsk("Choisissez un genre", GendersAvailable)
    SubjectInt = ForceAsk("Choisissez une matière", SubjectsAvailable)
    Appelation = AppelationGender[GenderInt]
    Format.Line()
    isOkInt = ForceAsk(f"Bienvenue {Appelation} {MyName}, professeur principal de {SubjectsAvailable[SubjectInt]} !", ["Super !", "J'ai besoin de modifier mon profil."])
    if isOkInt == 0 :
        Me = InitMe(MyName, MyFirstName, GenderInt, SubjectInt)
        isOk = True
        Format.Line()

class Date :
    Days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    Months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    
    DayAccurate = 0
    DayMonth = 0
    Month = 8
    Year = 2022
    Day = Days[DayAccurate % 7]

def NewDay(ReturnDate = True) :
    Date.DayAccurate = Date.DayAccurate + 1
    Date.DayMonth = (Date.DayAccurate % 30) + 1
    if Date.DayMonth == 1 :
        Date.Month = (Date.Month + 1) % 12
    Date.Day = Date.Days[Date.DayAccurate % 7]
    if Date.DayMonth == 1 and Date.Month == 1 :
        Date.Year = Date.Year + 1
    if ReturnDate :
        return f"{Date.Day} {Date.DayMonth} {Date.Months[Date.Month]} {Date.Year}"

def ReturnDay() :
    return f"{Date.Day} {Date.DayMonth} {Date.Months[Date.Month]} {Date.Year}"

def AnnonceDate(time = 0) :
    Format.Line()
    Say(f"{NewDay()}\nUn nouveau jour se lève")
    Format.Line()
    Time.sleep(time)

def Shop() :
    # Le shop du jeu.
    # Lorsque le shop est ouvert, la valeur à laquelle vous avez la permission d'acheter des articles est égale à Me.ItemSlot
    # De la class InitMe.
    
    "Veillez vous assurer d'avoir au moins le strict minimum d'argent pour pouvoir acheter ce qu'il vous plaît :)"

Say("C'est la rentrée, vous êtes le premier arrivé au lycée pour ajuster les préparatifs. Votre liste d'élèves est sur le bureau mais vous ne l'avez pas encore regardé.")
Ans = None
while Ans != 0 :
    Ans = ForceAsk("Que souhaitez vous faire ?", ["Ne rien faire", "Génerer une liste d'élèves (aléatoire)", "Regarder son inventaire"])
    Format.Line()
    if Ans == 1 :
        MyClass.GenerateNewStudentsList()
        MyClass.ShowStudents()
        Format.Line()
        Wait(f"Quel magnifique classe de {ClassesAvailable[MyClass.Graduation]} vous allez devoir supporter !\nAppuyez sur Entrée pour continuer.")
        Format.Line()
    elif Ans == 2 :
        Me.ShowInventory()
        Format.Line()
        Wait()
        Format.Line()

if not MyClass.isStudentsGenerated :
    MyClass.GenerateNewStudentsList()

Loading()
Semester = 0
DayBeforeImNoLongerSick = 0


# Différents types de mails

RandomMails = {
    "La fête du Kebab !": f"Rejoignez nous dans la fête du kebab !\n20 rue DesMajosés ce {ReturnDay()} à 18h !\nNe tardez pas ! La sauce blanche est bientôt fini !",
    "Don de sang": "Si vous plaît vous pouvez faire un don ?\nC'est pour le travail.",
    "Nicolas": "Salut c'est nicolas, tu peux cliquer sur ce lien pas du tout inquiétant ?\nhttp://adfly.56.co/redirection_by_ddos_attack/\nMerci d'avance !",
    "Inspection des maisons": f"Bonjour Monsieur {Me.Name}, vous nous devez 1500€.\nVous pouvez régler d'ici 2098.\nBonne journée sympathique !",
    "Gâteaux": "J'aime les gâteaux !",
    "DM de maths": "Bonjour Monsieur c'est Daniel, est-ce que vous pouvez me mettre un 20/20 pour mon DM de maths ?\nPar contre je sais pas si je l'ai bien envoyé à un prof de maths sinon vous pouvez ne pas dire\nque je vous ai envoyé un mail ?\nMerci.",
    "Terminales survivants du chaos": "On s'appelle Groot, Emilie et Sylvain et nous avons survécu à un crash aérien.\nEst-ce que, vu qu'on a survécu, vous pouvez nous donner 100 000€ de dons ?\nN'oublions pas que nous avons survéu à un chaose."
}

def MailReceive(isRandom = True, mailIndex = 0) :
    if isRandom :
        mail = randint(0, len(RandomMails) -1)
        name = list(RandomMails.keys())[mail]
        obj = list(RandomMails.values())[mail]
        Me.AddMail(name, obj)
    else :
        name = list(RandomMails.keys())[mailIndex]
        obj = list(RandomMails.values())[mailIndex]
        Me.AddMail(name, obj)

while Semester == 0 :

    AnnonceDate(5)

    Me.IsLate = False

    # Vérifie si le joueur a un talisman d'immunité.
    # Le talisman d'immunité permet de se débarrasser de la malchance aléatoire. Elle s'affecte sur la maladie, le retard et la fatigue.
    # Le talisman n'a aucun effet sur l'humeur des autres PNJ et donc ne permet pas de facilement gagner en confiance avec eux.
    hasImmune = Me.HasItem("Talisman d'immunité malchanceuse")

    #Le joueur a une chance sur 15 qu'on lui envoie un mail
    P = randint(0, 14)
    if P == 0 :
        MailReceive()
    
    if Me.IsSick :
        DayBeforeImNoLongerSick -= 1
        if DayBeforeImNoLongerSick <= 0 :
            Me.IsSick = False
            Say("Vous vous réveillez, et vous remarquez que vous allez beaucoup mieux maintenant.")
        else :
            Say(f"Rebien le bonjour ! Vous êtes encore malade, mais vous vous rassurez en vous disant qu'il reste {DayBeforeImNoLongerSick} jour{'s' if DayBeforeImNoLongerSick <= 1 else 's'}.")
            Ans = ForceAsk("Que voulez vous faire ?", ["Rester au lit", "Faire les courses"])
            if Ans == 0 :
                Say("Vous décidez de rester au lit.")
                # Déclenche une probabilité aléatoire de devoir écrire un mail pour annoncer à l'étabissement que vous êtes absent.
                P = randint(1, 7)
                if P <= 3 and Me.WasAbsent :
                    Say("Vous avez cependant reçu une notification de l'établissement annonçant que vous devez justifier votre absence.")
                    Ans = ForceAsk("Que souhaitez-vous faire ?", ["Ignorer", "Envoyer un mail."])
                    if Ans == 0 :
                        Say("Vous décidez de ne pas envoyer de mail.\nVous vous rendormez")
                    else :
                        Mail()
            else :
                Shop()
                    
    else :
        if not Date.Day == "Dimanche" :
            if not hasImmune :
                # Le joueur a une probabilité de 3,6% de tomber malade.
                P = randint(1, 30)
            else :
                P = 2
            if P == 1 :
                Me.IsSick = True
            else :
                Me.IsSick = False
            if Me.IsSick :
                DayBeforeImNoLongerSick = randint(1, 7)
                Say(f"Vous venez de vous réveiller, vous vous sentez faible et vous avez un mal de tête insupportable.\nVous appelez un docteur. Ce dernier vous informe que vous avez une fièvre et estime que vous en avez pour {DayBeforeImNoLongerSick} jour{'s' if DayBeforeImNoLongerSick <= 1 else 's'}.")
                Wait()
                Ans = ForceAsk("Que souhaitez vous faire ?", ["Rester au lit, probablement à regarder Netflix et manger Burger King.", "Rester à la maison mais travailler en visio conférence", "Aller tout de même à l'école"])
                if Ans == 0 :
                    Say("Vous ne faîtes absolument rien de la journée. Et ça c'est bien.")
                    Me.WasAbsent = True
                    Ans = ForceAsk("Souhaitez vous regarder votre inventaire ?", ["Oui", "Non"])
                    if Ans == 0 :
                        Me.ShowInventory()
                        Format.Line()
                        Wait()
                        Format.Line()
                        continue
                elif Ans == 1 :
                    Say("Vous appelez le chef d'établissement pour annoncer que vous n'êtes pas en forme pour assister à ses cours, etque vous souhaitez faire une visioconférence avec vos élèves.")
                    P = randint(0, 2)
                    if P == 0 :
                        Say("Bonne nouvelle, il a accepté.")
                        #Cours en visio conférence
                    else :
                        Say("Mauvaise nouvelle, il a refusé.")
                        Time.sleep(2)
                        Format.Line()
                        Ans = ForceAsk("Que souhaitez vous faire ?", ["Rester au lit, probablement à regarder Netflix et manger Burger King.", "Aller tout de même à l'école"])
                        if Ans == 0 :
                            Say("Vous ne faîtes absolument rien de la journée. Et ça c'est bien.")
                            Me.WasAbsent = True
                            Ans = ForceAsk("Souhaitez vous regarder votre inventaire ?", ["Oui", "Non"])
                            if Ans == 0 :
                                Me.ShowInventory()
                                Format.Line()
                                Wait()
                                Format.Line()
                                continue
                            else :
                                Say("Vous vous reveillez donc et decidez d'aller à l'école malgrès le mal de tête.")
            else :
                Say("Vous vous réveillez, vous allez très bien. Pas de trace de maladie quelquonque.")


            # Définie aléatoire le retard du joueur.
            # Si le joueur est malade et qu'il souhaite tout de même faire ses cours, il a 33% de chance d'être en retard.
            # Si dans le cas contraire, le joueur n'est pas malade, il a 7,1% de chance d'être en retard.

            
            if Me.IsSick :
                Me.IsLate = False if randint(0, 2) != 0 else True
            else :
                if not hasImmune :
                    Me.IsLate = False if randint(0, 15) != 0 else True
                else :
                    Me.IsLate = False
            if Me.IsLate :
                Me.TimeLate += 1
                Hours = f"{randint(9, 12)}:{randint(0, 59)}"
                Say(f"Cependant, vous remarquez qu'il est {Hours}.\nOui, espèce de débile, vous êtes en retard. Vous courez à toutes vitesses vers votre salle de bain puis vous reflechissez à un truc avant de partir...")
                if Me.TimeLate == 4 :
                    Say("Attention ! C'est la quatrième fois que vous êtes en retard ! Encore une fois et il se peut que vous soyez viré !")
                if Me.TimeLate == 5 :
                    Say("Vous avez été en retard 5 fois. Vous allez probablement passer un mauvais quart d'heure :(")
                Ans = ForceAsk(f"Voulez vous réellement aller en cours ? Il est quand même {Hours}...", ["Y aller", "Ne pas y aller"])
                
                if Ans == 1 :
                    Me.WasAbsent = True
                    Say("Vous décidez de rester chez vous.")
                    Ans = ForceAsk("Souhaitez-vous tout de même faire quelque chose ?", ["Non, ne rien faire", "Oui, faire les courses", "Oui, regarder mon inventaire"])
                    if Ans == 1 :
                        Shop()
                    elif Ans == 2 :   
                        Me.ShowInventory()
                        Format.Line()
                        Wait()
                        Format.Line()
                        continue
        else :
            Ans = ForceAsk("Il est dimanche !\nQue souhaitez vous faire en cette belle journée où vous ne travaillez pas ?", ["Faire des courses", "Voir mes mails", "Se promener", "Corriger des copies", "Ne rien faire"])
            if Ans == 0 :
                Shop()
            elif Ans == 1 :
                Mail()
        
