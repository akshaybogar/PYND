'''
This file contains QuoteModel class which defines the template for a quote.
'''

class QuoteModel():
    '''
    __init__ method takes body and author as inputs and initialzes quote object.
    '''
    def __init__(self, body, author):
        self.body = body
        self.author = author

    '''
    __repr__ is magic function which is used to represent the quote in the
     form of string.
    '''
    def __repr__(self):
        if '"' in self.body:
            return '{} - {}'.format(self.body, self.author)
        return '"{}" - {}'.format(self.body, self.author)
