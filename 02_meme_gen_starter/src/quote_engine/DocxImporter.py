from .IngestorInterface import IngestorInterface
from docx import Document
from .QuoteModel import QuoteModel

class DocxImporter(IngestorInterface):
    file_exts = ['docx']

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
