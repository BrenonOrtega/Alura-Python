import json
import config
import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/<int:poke_id>')
@app.route('/<string:poke_name>')
def hello(poke_id=1, poke_name=''):
    query = poke_id if poke_name == '' else poke_name
    response = requests.get(config.URL + str(query))
    data = json.loads(response.text)
    sprite_url = data['sprites']['front_default']

    return render_template('index.html', data=data, sprite_url=sprite_url)

if __name__ == "__main__":
    app.run(debug=True)
