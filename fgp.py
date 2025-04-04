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


