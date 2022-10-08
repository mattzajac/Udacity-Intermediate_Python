"""IngestorInterface abstract base class to provide a schema for parsers."""

from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """Abstract base class parsing quotes from different file formats."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Verify if a passed file can be parsed.

        :param path: a path to a file.
        :returns: bool
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse files and return list of 'QuoteModel'."""
        pass
