class flashcard():
    def __init__(self, subject, phrase, answer):
        self.subject = subject
        self.phrase = phrase
        self.answer = answer
    def display(self):
        return f"{self.phrase}: {self.answer}"
    def dict(self):
        return {"subject": self.subject, "phrase": self.phrase, "answer": self.answer}

new_flashcard = flashcard