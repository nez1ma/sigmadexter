import uuid

class Book:
    def __init__(self, author: str, title: str):
        self.author = author
        self.title = title
        self.id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.title} — {self.author} (ID: {self.id})"
