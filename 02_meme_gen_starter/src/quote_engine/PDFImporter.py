'''
This file contains PDFImporter class which is realized from IngestorInterface
'''

from .IngestorInterface import IngestorInterface
import os
import random
import subprocess
from .QuoteModel import QuoteModel


class PDFImporter(IngestorInterface):
    file_exts = ['pdf']

    '''
    parse method takes path of the file and checks if it is a pdf file.
    If the file is of pdf format then it is read through subprocess  using
    pdftotext and the method returns the list of quotes.
    '''
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file')

        tmp_file = '{}.txt'.format(random.randint(0, 100000))
        call = subprocess.call(['pdftotext', path, tmp_file])
        quotes = []
        file_ref = open(tmp_file, 'r')
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                line = line.split('-')
                quotes.append(QuoteModel(*line))

        file_ref.close()
        os.remove(tmp_file)
        return quotes
