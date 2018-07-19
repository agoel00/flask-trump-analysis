from flask import Flask, render_template, request
import requests
from textblob import TextBlob
import json

app = Flask(__name__)

@app.route('/random', methods=['POST'])
def random():
    response = requests.get('https://api.tronalddump.io/random/quote')

    response_text = json.loads(response.text)

    quote = response_text['value']
    source = response_text['_embedded']['source'][0]['url']

    blob = TextBlob(quote)

    sentiment = blob.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    return render_template('random.html', quote=quote, source=source, polarity=polarity, subjectivity=subjectivity)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
