"""TXT parser."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Class to parse TXT files and return quotes."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse TXT files and return list of 'QuoteModel'."""
        if not cls.can_ingest(path):
            raise Exception('Unsupported file. Cannot ingest.')

        quotes = []

        try:
            with open(path, 'r', encoding='utf-8') as f:
                for quote in f.readlines():
                    quote = quote.replace('"', "").strip('\n\r').strip()

                    if len(quote) > 0:
                        parsed = quote.split(' - ')
                        new_quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(new_quote)

            return quotes

        except FileNotFoundError:
            print(f"File {path} not found!")
