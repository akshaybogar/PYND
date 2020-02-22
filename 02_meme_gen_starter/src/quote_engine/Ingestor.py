from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .TXTImporter import TXTImporter
from .PDFImporter import PDFImporter
from .DocxImporter import DocxImporter

class Ingestor(IngestorInterface):
    importers = [CSVImporter, TXTImporter, PDFImporter, DocxImporter]
    @classmethod
    def parse(cls, path):
        for importer in importers:
            if importer.can_ingest(path):
                return importer.parse(path)
