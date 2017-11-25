from foursquareRestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "1Y1KAGWNJNG0S12YVN3N41MY4OMO5HFL53FVODL0OVPMUWU0"
foursquare_client_secret = "OMFFIFDWF0NUL4CFKXXN3FEV2135TO2JRP2IHEZJILH2QKU4"
google_api_key = "AIzaSyBNhD3eLr4Lg2GA5H88ESn0xg1e6oaoA6Q"

engine = create_engine('sqlite:///restaruants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@app.route('/restaurants', methods=['GET', 'POST'])
def all_restaurants_handler():
    if request.method == 'GET':
        restaurants = session.query(Restaurant).all()
        return jsonify(restaurants=[i.serialize for i in restaurants])

    elif request.method == 'POST':
        location = request.args.get('location', '')
        mealType = request.args.get('mealType', '')
        restaurant_info = findARestaurant(mealType, location)
        if restaurant_info != "No Restaurants Found":
            restaurant = Restaurant(restaurant_name=unicode(restaurant_info['name']),
                                    restaurant_address=unicode(restaurant_info['address']),
                                    restaurant_image=restaurant_info['image'])
            session.add(restaurant)
            session.commit()
            return jsonify(restaurant=restaurant.serialize)
        else:
            return jsonify({"error": "No Restaurants Found for %s in %s" % (mealType, location)})


@app.route('/restaurants/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def restaurant_handler(id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    if request.method == 'GET':
        return jsonify(restaurant=restaurant.serialize)
    elif request.method == 'PUT':
        address = request.args.get('address')
        image = request.args.get('image')
        name = request.args.get('name')
        if address:
            restaurant.restaurant_address = address
        if image:
            restaurant.restaurant_image = image
        if name:
            restaurant.restaurant_name = name
        session.commit()
        return jsonify(restaurant=restaurant.serialize)

    elif request.method == 'DELETE':
        session.delete(restaurant)
        session.commit()
        return "Restaurant Deleted"


if __name__ == '__main__':
    app.debug = True
app.run(host='0.0.0.0', port=5000)