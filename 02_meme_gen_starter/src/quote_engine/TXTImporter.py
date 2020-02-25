'''
This file contains TXTImporter class which is realized from IngestorInterface
'''

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTImporter(IngestorInterface):
    file_exts = ['txt']

    '''
    parse method takes path of the file and checks if it is a txt file.
    If the file is of txt format then it is read and alist of quotes is
    returned.
    '''
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file')
        quotes = []
        file_ref = open(path, 'r')
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                line = line.split('-')
                quotes.append(QuoteModel(*line))
        file_ref.close()
        return quotes
