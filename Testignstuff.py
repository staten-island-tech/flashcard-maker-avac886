""""
import json

class flashcard():
    def __init__(self, phrase, answer):
        self.phrase = phrase
        self.answer = answer
    def display(self):
        return f"{self.phrase}: {self.answer}"
    def dict(self):
        return {"phrase": self.phrase, "answer": self.answer}


cards = []
new_phrase = input("Enter an English phrase/word: ")
new_answer = input("Enter the Russian translation of that phrase/word: ")
new_flashcard = flashcard(new_phrase, new_answer)

try:
    with open("flashcards.json", "r") as file:
        cards_data = json.load(file)
except FileNotFoundError:
    cards_data = []
cards_data.append(new_flashcard.dict()) # dict not to_dict dummy
with open("cards.json", "w") as file:
    json.dump(cards_data, file, indent=4)

for card in cards_data:
    print(new_flashcard.display())
"""
""" while True:
    cards = []
    new_phrase = input("Enter an English phrase/word: ")
    new_answer = input("Enter the Russian translation of that phrase/word: ")
    new_flashcard = flashcard(new_phrase, new_answer)
    cards.append(new_flashcard)

    cards_data = [flashcard.dict() for flashcard in cards]
    with open('flashcards.json', 'w', encoding='utf-8') as json_file:
        json.dump(cards_data, json_file, ensure_ascii=False, indent=4)
    try:
        with open("flashcards.json", "r") as file:
            cards_data = json.load(file)
    except FileNotFoundError:
            cards_data = []
    print(cards_data) """


#attempt 1
""" while True:
    cards = []
    new_phrase = input("Enter an English phrase/word: ")
    new_answer = input("Enter the Russian translation of that phrase/word: ")
    new_flashcard = flashcard(new_phrase, new_answer)
    cards.append(new_flashcard)

    cards_data = [flashcard.dict() for flashcard in cards]
    with open('flashcards.json', 'w', encoding='utf-8') as json_file:
        json.dump(cards_data, json_file, ensure_ascii=False, indent=4)
    try:
        with open("flashcards.json", "r") as file:
            cards_data = json.load(file)
    except FileNotFoundError:
            cards_data = []
    print(cards_data) """

""" import json

class flashcard():
    def __init__(self, phrase, answer):
        self.phrase = phrase
        self.answer = answer
    def display(self):
        return f"{self.phrase}: {self.answer}"
    def dict(self):
        return {"phrase": self.phrase, "answer": self.answer}

for i in range(2):
    cards = []

    cards_data = [new_flashcard.dict() for new_flashcard in cards]
    with open("cards.json", "w") as file:
        json.dump(cards_data, file, indent=4)

    new_phrase = input("Enter an English phrase/word: ")
    new_answer = input("Enter the Russian translation of that phrase/word: ")
    new_flashcard = flashcard(new_phrase, new_answer)

    try:
        with open("flashcards.json", "r") as file:
            cards_data = json.load(file)
    except FileNotFoundError:
        cards_data = []
    cards_data.append(new_flashcard.dict()) # dict not to_dict dummy
    with open("cards.json", "w") as file:
        json.dump(cards_data, file, indent=4)
 """

''''
import json

class Flashcard:
    def __init__(self, phrase, answer):
        self.phrase = phrase
        self.answer = answer
    
    def display_phrase(self):
        print(self.phrase)

    def display_answer(self):
        print(self.answer)
    
    def to_dict(self):
        return {"phrase": self.phrase, "answer": self.answer}


try:
    with open("flashcards.json", "r") as file:
        cards_data = json.load(file)
except FileNotFoundError:
    cards_data = []

for i in range(2): 
    new_phrase = input("Enter an English phrase/word: ")
    new_answer = input("Enter the Russian translation of that phrase/word: ")
    
    new_flashcard = Flashcard(new_phrase, new_answer)
    
    cards_data.append(new_flashcard.to_dict())

with open("flashcards.json", "w") as file:
    json.dump(cards_data, file, indent=4)

streak = 0
score = 0

for card in cards_data:
    print(card['phrase'])
    guess = input("Enter translation: ")
    if card['answer'] == guess:
        print("correct")
        score = score + 1
        streak = streak + 1
        if streak > 0:
            score = score + 1
        print(score)
        print(streak)
    else:
        print("incorrect")
        print(card['answer'])
        streak = 0
        print(score)
        print(streak)
'''''

#TESR
while True:
    import json

    position = input("Yo are you a teacher or student?")

    class Flashcard:
        def __init__(self, phrase, answer):
            self.phrase = phrase
            self.answer = answer
        
        def display_phrase(self):
            print(self.phrase)

        def display_answer(self):
            print(self.answer)
        
        def to_dict(self):
            return {"phrase": self.phrase, "answer": self.answer}

    try:
        with open("flashcards.json", "r") as file:
            cards_data = json.load(file)
    except FileNotFoundError:
        cards_data = []

    if position == "teacher":
        amount = int(input("What is the absurd amount of defintions you want to torture your kids with? "))
        for i in range(amount): 
            new_phrase = input("Enter an English phrase/word: ")
            new_answer = input("Enter the Russian translation of that phrase/word: ")
            
            new_flashcard = Flashcard(new_phrase, new_answer)
            
            cards_data.append(new_flashcard.to_dict())

    with open("flashcards.json", "w") as file:
        json.dump(cards_data, file, indent=4)

    if position == "student":

        streak = 0
        score = 0

        #The error you're seeing — that "display_phrase" does not exist — happens because you're calling display_phrase() on a dictionary, 
        # not a Flashcard object.

        flashcards = [Flashcard(card['phrase'], card['answer']) for card in cards_data] #make flashcards in flashcards JSON applicable to the class functions

        for card in flashcards:
            print(f"Phrase: {card.display_phrase()}")
            guess = input("Enter translation: ")
            if card.display_phrase == guess:
                print("correct")
                score = score + 1
                streak = streak + 1
                if streak > 0:
                    score = score + 1
                print(f"Your current score is {score}")
                print(f"Your current streak is {streak}")
            else:
                print("incorrect")
                card.display_answer()
                streak = 0
                print(f"Your current score is {score}")
                print(f"Womp womp you lost your streak. It is now {streak}. Bring it back up loser.")