'''
This file contains an abstract class IngestorInterface and an abstractmethod
parse
'''
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    file_exts = []

    '''
    can_ingest method is takes file path and checks if the extension of the
    file can be ingested or not
    '''
    @classmethod
    def can_ingest(cls, path):
        file_ext = path.split('.')[-1]
        return file_ext in cls.file_exts

    '''
    parse is an abstractmethod which every class realizing IngestorInterface
    will override.
    '''
    @classmethod
    @abstractmethod
    def parse(cls, path):
        pass
