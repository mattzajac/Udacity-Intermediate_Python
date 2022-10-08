"""Meme Generator.

This script allows to load an image, manipulate it and add
a quote body and a quote author. It returns the path to
newly created meme.
"""

import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """MemeEngine class to generate memes.

    Attributes:
    font_type: font type
    font_fill: font color
    """

    font_type = './_data/font/arial.ttf'
    font_fill = 'white'

    def __init__(self, output_path):
        """Create instance of class.

        Parameters:
        output_path: a path to save a file
        """
        self.output_path = output_path

    def make_meme(self, img_path, body, author, width=500) -> str:
        """Create a meme with a quote and author.

        Parameters:
        img_path: image path
        body: quote text
        author: quote author
        width: width to be resized to (default=500px)

        Returns:
        meme path string
        """
        with Image.open(img_path) as img:
            if width is not None:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height))

            if body and author:
                quote = f'{body}\n- {author}'
                font_size = int(height/20)
                x, y = 10, random.randint(font_size, height-font_size)

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(font=self.font_type, size=font_size)
                draw.text((x, y), quote, font=font, fill=self.font_fill)

            out_path = f'{self.output_path}/{random.randint(0, 100)}.jpeg'
            img.save(out_path)

        return out_path
