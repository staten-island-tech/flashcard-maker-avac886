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

#REAL

import json

class Flashcard:
    def __init__(self, phrase, answer):
        self.phrase = phrase
        self.answer = answer
    
    def display_phrase(self):
        print(self.phrase)

    def display_answer(self):
        print(self.answer)
    
    def dict(self):
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
    
    cards_data.append(new_flashcard.dict())

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
        streak = 0
        print(score)
        print(streak)