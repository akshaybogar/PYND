from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    file_exts = []

    @classmethod
    def can_ingest(cls, path):
        file_ext = path.split('.')[-1]
        return file_ext in cls.file_exts

    @classmethod
    @abstractmethod
    def parse(cls, path):
        pass
        
