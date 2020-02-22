from .IngestorInterface import IngestorInterface

class TXTImporter(IngestorInterface):
    file_exts = [txt]

    def parse(cls, path):
        if not can_ingest(path):
            raise Exception('Cannot ingest this file')
        quotes = []
        file_ref = open(path)
        for quote in file_ref.readlines():
            quote = line.strip('\n\r').strip()
            if len(quote) > 0:
                quotes.append(quote)
        return quotes
