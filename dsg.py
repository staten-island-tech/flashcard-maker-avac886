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