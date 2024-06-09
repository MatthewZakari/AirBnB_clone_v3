#!/usr/bin/python3

'''API Status'''
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/status', strict_slashes=False)
def return_status():
    '''Returns the API status.'''
    return jsonify(status='OK')


@app.route('/stats', strict_slashes=False)
def get_stats():
    '''Returns statistics about the number of stored objects.'''
    stats = {
        'states': storage.count(State),
        'users': storage.count(User),
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
    }
    return jsonify(stats)


if __name__ == '__main__':
    app.run()

