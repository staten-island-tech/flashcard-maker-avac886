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
print(new_flashcard.display())
cards_data = [card.to_dict() for card in cards]
with open("cards.json", "w") as file:
    json.dump(cards_data, file, indent=4)
    

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



