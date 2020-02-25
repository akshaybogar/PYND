'''
This file contains DocxImporter class which is realized from IngestorInterface
'''

from .IngestorInterface import IngestorInterface
from docx import Document
from .QuoteModel import QuoteModel


class DocxImporter(IngestorInterface):
    file_exts = ['docx']

    '''
    parse method takes path of the file and checks if it is a docx file.
    If the file is of docx format then it is read using docx library and
    returns the list of quotes.
    '''
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file')
        quotes = []
        doc = Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                quotes.append(QuoteModel(*para.text.split('-')))
        return quotes
