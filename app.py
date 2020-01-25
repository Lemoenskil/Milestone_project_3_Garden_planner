import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId


app = Flask ("----name----")
app.config["MONGO_DBNAME"] = 'garden_planner'
app.config["MONGO_URI"] = 'mongodb+srv://CP3O:iYmkh8QOgi2fhu2y@lemoenskil-4vjdx.mongodb.net/garden_planner?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/plant_records')
def get_plant_record():
    plant_cards = mongo.db.plant_data.find().sort([('views', DESCENDING)]).limit(4)
    plants_carousel = mongo.db.plant_data.find().sort([('views', DESCENDING)]).limit(4)
    return render_template("plant_records.html", title="Home", plants = plant_cards, plants_carousel = plants_carousel)

    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            