class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        if '"' in self.body:
            return '{} - {}'.format(self.body, self.author)
        return '"{}" - {}'.format(self.body, self.author)
