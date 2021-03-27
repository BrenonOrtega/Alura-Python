import config
import requests
from collections import namedtuple
from operator import itemgetter
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/<int:poke_id>')
@app.route('/<string:poke_name>')
def hello(poke_id=1, poke_name=''):
    query = str(poke_id) if poke_name == '' else poke_name
    data = requests.get(config.POKEMON_URL + query)
    pokemon = get_obj("pokemon", data.json())
    sprite_url = pokemon.sprites['front_default']
    return render_template('index.html', data=pokemon, sprite_url=sprite_url)

get_obj = lambda classe, object: namedtuple(classe, object.keys())(*object.values())

if __name__ == "__main__":
    app.run(debug=True)
