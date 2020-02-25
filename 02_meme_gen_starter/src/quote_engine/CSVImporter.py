'''
This file contains CSVImporter class which is realized from IngestorInterface
'''

from .IngestorInterface import IngestorInterface
import pandas as pd
from .QuoteModel import QuoteModel


class CSVImporter(IngestorInterface):
    file_exts = ['csv']

    '''
    parse method takes path of the file and checks if it is a CSV file.
    If the file is of CSV format then it is read using pandas library and
    returns the list of quotes.
    '''
    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file')
        quotes = []
        df = pd.read_csv(path)

        for index, row in df.iterrows():
            quotes.append(QuoteModel(*row))
        return quotes
