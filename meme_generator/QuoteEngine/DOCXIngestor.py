"""DOCX parser."""

from typing import List
from docx import Document
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Class to parse DOCX files and return quotes."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse DOCX files and return list of 'QuoteModel'."""
        if not cls.can_ingest(path):
            raise Exception('Unsupported file. Cannot ingest.')

        quotes = []

        try:
            doc = Document(path)
        except FileNotFoundError:
            print(f"File {path} not found!")

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.replace('"', "").split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
