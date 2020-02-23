from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTImporter(IngestorInterface):
    file_exts = [txt]

    def parse(cls, path):
        if not can_ingest(path):
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
