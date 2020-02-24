from .IngestorInterface import IngestorInterface
import os
import random
import subprocess
from .QuoteModel import QuoteModel

class PDFImporter(IngestorInterface):
    file_exts = ['pdf']

    @classmethod
    def parse(cls, path):
        if not can_ingest(cls, path):
            raise Exception('Cannot ingest this file')

        tmp_file = '{}.txt'.format(random.randint(0, 100000))
        call = subprocess.call('pdftotext', path, tmp_file)
        quotes = []
        file_ref = open(tmp_file, 'r')
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                line = line.split('-')
                quotes.append(QuoteModel(*line))

        file_ref.close()
        os.remove(file_ref)
        return quotes
