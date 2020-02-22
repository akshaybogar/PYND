from .IngestorInterface import IngestorInterface
from docx import Document

class DocxImporter(IngestorInterface):
    file_exts = [docx]

    def parse(cls, path):
        if not can_ingest(path):
            raise Exception('Cannot ingest this file')
        quotes = []
        doc = Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                quotes.append(para.text)
        return quotes
