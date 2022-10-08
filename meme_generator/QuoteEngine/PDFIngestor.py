"""PDF parser."""

from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse PDF files and return quotes."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF files and return list of 'QuoteModel'."""
        if not cls.can_ingest(path):
            raise Exception('Unsupported file. Cannot ingest.')

        tmp = f'./tmp/{random.randint(0,1000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        try:
            f = open(tmp, "r", encoding='utf-8-sig')
        except FileNotFoundError:
            print(f"File {path} not found!")

        quotes = []

        for quote in f.readlines():
            quote = quote.strip('\n\r').strip()
            if len(quote) > 0:
                parsed = quote.replace('"', "").split(' - ')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        f.close()
        os.remove(tmp)
        return quotes
