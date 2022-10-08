"""Ingestor class for parsing files.

Ingestor class realizes the IngestorInterface abstract base class
and encapsulates file specific ingestor classes. It selects the appropriate
ingestor for a given file, based on filetype.
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Subclass of IngestorInterface for parsing files."""

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method to verify file type and process data.

        :param path: a path to a file.
        :returns: a list of 'QuoteModel'.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
