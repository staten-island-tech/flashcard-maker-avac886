
#REALx
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

        flashcards = [Flashcard(card['phrase'], card['answer']) for card in cards_data]

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