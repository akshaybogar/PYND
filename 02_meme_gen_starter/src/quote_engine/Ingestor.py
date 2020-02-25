'''
This file consists Ingestor class definition
'''

from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .TXTImporter import TXTImporter
from .PDFImporter import PDFImporter
from .DocxImporter import DocxImporter


class Ingestor(IngestorInterface):
    importers = [CSVImporter, TXTImporter, PDFImporter, DocxImporter]

    '''
    parse method defined.
    Description : Takes path of a file and calls the right importer from the
    list created above to read data from the file.
    '''
    @classmethod
    def parse(cls, path):
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
