class Question:
    # Using __init__ so the function runs buy itself
    def __init__(self, prompt, answer, serving_size, item):
        self.prompt = prompt
        self.answer = answer
        self.serving_size = serving_size
        self.item = item
