"""CSV parser."""

from typing import List
import pandas
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class to parse CSV files and return quotes."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV files and return list of 'QuoteModel'."""
        if not cls.can_ingest(path):
            raise Exception('Unsupported file. Cannot ingest.')

        quotes = []

        try:
            df = pandas.read_csv(path, header=0)
        except FileNotFoundError:
            print(f"File {path} not found!")

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
