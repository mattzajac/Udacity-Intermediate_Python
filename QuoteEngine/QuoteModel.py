"""QuoteModel class to encapsulate the body and author."""


class QuoteModel():
    """A base class to generate a quote."""

    def __init__(self, body, author):
        """Create a new `QuoteModel`.

        :param body: A body of a quote.
        :param author: An author of a quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a string with a quote and an author."""
        return f'{self.body} - {self.author}'
