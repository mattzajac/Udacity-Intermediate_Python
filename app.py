"""Meme Generator Flask App.

This app generates random memes but also allows you to provide
your own picture and quotes for your own memes.
"""

import random
import os
import requests
from flask import Flask, render_template, request

from QuoteEngine import Ingestor,
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, file) for file
            in os.listdir(images_path) if file.endswith(".jpg")]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    img = requests.get(request.form['image_url'])
    body = request.form['body']
    author = request.form['author']

    try:
        tmp_file = f'tmp/{random.randint(0, 1000)}.jpg'
        open(tmp_file, 'wb').write(img.content)
    except:
        print('Unsupported file. Cannot load image.')
    else:
        path = meme.make_meme(tmp_file, body, author)
        os.remove(tmp_file)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

