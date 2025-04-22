while True:
    import json

    mode = input("Yo are you a teacher or student?")

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

    if mode == "teacher":
        amount = int(input("What is the absurd amount of defintions you want to torture your kids with? "))
        for i in range(amount): 
            new_phrase = input("Enter an English phrase/word: ")
            new_answer = input("Enter the Russian translation of that phrase/word: ")
            
            new_flashcard = Flashcard(new_phrase, new_answer)
            
            cards_data.append(new_flashcard.to_dict())

    with open("flashcards.json", "w") as file:
        json.dump(cards_data, file, indent=4)

    if mode == "student":

        streak = 0
        points = 0
        total_correct = 0

        flashcards = [Flashcard(card['phrase'], card['answer']) for card in cards_data]

        for card in flashcards:
            print("Phrase:")
            card.display_phrase()
            guess = input("Enter translation:")
            if card.answer == guess:
                print("correct")
                streak = streak + 1
                points = points + 1
                total_correct = total_correct + 1
                if streak > 1:
                    points = points + 1
            else:
                streak = 0
                print(f"Incorrect. Womp womp you lost your streak. It is now {streak}. Bring it back up loser.")
            print(f"You got {total_correct} phrases correct")
            print(f"Your current score is {points}")
            print(f"Your current streak is {streak}")