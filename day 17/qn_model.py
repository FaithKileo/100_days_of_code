class Question:
    
    def __repr__(self):
        return f"{self.text}"

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer 