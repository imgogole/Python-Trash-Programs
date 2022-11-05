# EMC Learner
# Allows you to help someone learn their EMC class (yes I used it for MY EMC class so...)

from random import *
from difflib import SequenceMatcher
from json import *

from datetime import *

from random import *

Months = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre');

def IsBissextile(Year: int) :
    return Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0

def GetIndexMonth(Month: str) :
    for i in range(12) :
        if Months[i].lower() == Month.lower() :
            Index = i
    return Index

def GetParity(Month: str, Year: int):
    Index = GetIndexMonth(Month)
    if Index == 2 :
        return 1 if IsBissextile(Year) else 0
    elif Index < 7 :
        return (Index + 1) % 2
    else :
        return Index % 2

def RandomFrenchDatesAround(Date: str) :
    Day, Month, Year = tuple(Date.split())
    Year = int(Year)
    Day = int(Day)
    Year += randint(-5, 5)
    Index = GetIndexMonth(Month)
    Month = Months[(Index + randint(-2, 2)) % 12]
    Day += randint(-5, 5)
    Day %= 27 + GetParity(Month, Year)
    Day += 1
    return "%d %s %d" % (Day, Month.lower(), Year)

def RandomDefinition() :
    t = [
        "Régime politique dans lequel le peuple choisit ses réprésentants, on dit que le peuple est souverain.",
        "Système institutionel dans lequel la puissance publique est résumée au droit.",
        "Tous les citoyens exercent directement le pouvoir sans intermédiaire des représentants.",
        "Démocratie où les décisions sont prises par les représentants.",
        "Monarchie dans laquelle les pouvoirs sont soumis et limités par une constitution.",
        "Ensemble des individus qui se reconnaissent destin commun et partage une même culture.",
        "Vote des électeurs sur un seul candidat élu à la majorité relative au second tour.",
        "Mode de désignation par éléction qui attribue les sièges selon le nombre de voix obtenues par les différentes listes.",
        "Organisation dont les membres partagent des valeurs et des idées et mènent une action commune pour faire élire leurs représentants aux éléctions locales et nationales"
    ]
    return choice(t)

def RandomCountry(Size = 1) :
    countries = [
        "Royaume-Uni",
        "Canada",
        "Australie",
        "Polynésie",
        "Etat-Unis",
        "Inde",
        "Indonésie",
        "Groeland",
        "Norvège",
        "Suède",
        "Danemark",
        "Espagne",
        "Belgique",
        "Pays-Bas"
    ]
    shuffle(countries)
    return ", ".join(countries[:Size])

def RandomReg() :
    t = [
        "Monarchie parlementaire",
        "République autoritaire",
        "République démocratique",
        "Dictature",
        "République populaire"
    ]
    return choice(t)

def RandomYear(Year, Seuil = 15) :
    return str(int(Year) + randint(-Seuil, Seuil))

def IsAlmostSame(fstr, sstr, seuil = 0.8) :
    return SequenceMatcher(a = fstr, b = sstr).ratio() > seuil 

class Question :
    @staticmethod
    def Eval(String: str, Answer: str) :
        if not String.startswith("$") : return String
        Command = String[1:].split()[0]
        Value = Answer
        while Value == Answer :
            if Command == "randomDate" :
                Value = RandomFrenchDatesAround(Answer)
            if Command == "randomDef" :
                Value = RandomDefinition()
            if Command == "randomReg" :
                Value = RandomReg()
            if Command == "randomYear" :
                Value = RandomYear(Answer)
            if Command == "randomCountry" :
                Value = RandomCountry(int(String.split()[1]))
        return Value

    def __init__(self, _Question, ProbQCM = 50) :
        self.Question = _Question
        self.WrongAnwsers = []
        self.Anwser = ""
        self.ProbQCM = ProbQCM
    def SetWrongAnswers(self, Answer) :
        """
        Add multiple wrong answers for a question.
        """
        for Ans in Answer :
            self.WrongAnwsers.append(Ans)
    def SetAnswer(self, Answer) :
        """
        Add answer for a question.
        """
        self.Anwser = Answer
    def Start(self) :
        IsQCM = randint(0, 100) <= self.ProbQCM
        if IsQCM :
            PossibleAnswers = []
            WrongAnswers = self.WrongAnwsers.copy()
            shuffle(WrongAnswers)
            PossibleAnswers.extend(WrongAnswers[:3])
            PossibleAnswers.append(self.Anwser)
            shuffle(PossibleAnswers)
            IndexOfRightAnwser = -1
            for i in range(len(PossibleAnswers)) :
                if self.Anwser == PossibleAnswers[i] :
                    IndexOfRightAnwser = i + 1 
                    break
            print("===========================================================================")
            print(self.Question)
            print("===========================================================================")
            for i in range(0, 4) :
                print(f"{i + 1} - {PossibleAnswers[i]}")
            print("===========================================================================")
            UserAns = input(">>> Votre réponse : ").strip()
            try :
                if int(UserAns) == IndexOfRightAnwser :
                    print("===========================================================================")
                    print("Bonne réponse !")
                    return True
                else :
                    raise Exception()
            except :
                print("===========================================================================")
                print("Mauvaise réponse : " + PossibleAnswers[IndexOfRightAnwser - 1])
            return False
        else :
            print("===========================================================================")
            print(self.Question)
            print("===========================================================================")
            UserAns = input(">>> Votre réponse : ")
            if IsAlmostSame(UserAns.lower().strip(), self.Anwser.lower()) :
                print("Bonne réponse !")
                return True
            print("Mauvaise réponse : " + self.Anwser)
        

class Exam :
    def __init__(self, Difficulty = 10) :
        self.Questions = []
        self.Difficulty = Difficulty
    def Add(self, _Question: Question) :
        self.Questions.append(_Question)
    def Start(self) :
        Points = 0
        for _ in range(self.Difficulty) :
            a = choice(self.Questions)
            a = a.Start()
            if a : Points += 1

        print(f"Vous avez fait {Points} points sur {self.Difficulty}.")

QuestionsAnswers = {}
exam = Exam(50)

with open("EMCLearner.json", 'r', encoding='utf-8') as q :
    QuestionsAnswers = dict(loads(q.read()))

for _, Values in QuestionsAnswers.items() :
    q = Question(Values["Question"], int(Values["ProbQCM"]))
    q.SetAnswer(Values["Answer"])
    l = []
    while len(l) < 3 :
        l = list(set(map(lambda ans : Question.Eval(ans, Values["Answer"]), tuple(Values["WrongAnswers"]))))
    if Values["Answer"] in l : l.remove(Values["Answer"])
    q.SetWrongAnswers(l)

    exam.Add(q)

exam.Start()



