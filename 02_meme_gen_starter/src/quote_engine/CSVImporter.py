from .IngestorInterface import IngestorInterface
import pandas as pd
from .QuoteModel import QuoteModel

class CSVImporter(IngestorInterface):
    file_exts = [csv]

    def parse(cls, path):
        if not can_ingest(path):
            raise Exception('Cannot ingest this file')
        quotes = []
        df = pd.read_csv(path)

        for index, row in df.iterrows():
            quotes.append(QuoteModel(*row))
        return quotes
