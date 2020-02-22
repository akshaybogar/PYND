from .IngestorInterface import IngestorInterface
import os
import random
import subprocess

class PDFImporter(IngestorInterface):
    file_exts = [pdf]

    def parse(cls, path):
        if not can_ingest(path):
            raise Exception('Cannot ingest this file')

        tmp_file = '{}.txt'.format(random.randint(0, 100000))
        call = subprocess.call('pdftotext', path, tmp_file)
        quotes = []
        file_ref = open(tmp_file, 'r')
        for quote in file_ref.readlines():
            quote = line.strip('\n\r').strip()
            if len(line) > 0:
                quotes.append(line)

        file_ref.close()
        os.remove(file_ref)
        return quotes
