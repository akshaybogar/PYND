import random
import os
import requests
import shutil
import urllib.request
from flask import Flask, render_template, abort, request
from quote_engine import Ingestor
from meme_engine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   #'./_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    print(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url = request.form.get('image_url')
    quote = request.form.get('body')
    author = request.form.get('author')
    response = requests.get(img_url, stream=True)
    temp_file = './_data/photos/temp/img.jpg'
    with open(temp_file, 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)
    del response
    path = meme.make_meme(temp_file, quote, author)
    os.remove(temp_file)
    return render_template('meme.html', path=path)

if __name__ == "__main__":
    app.run(debug=True, port=4999)
