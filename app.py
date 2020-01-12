import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask ("----name----")
app.config["MONGO_DBNAME"] = 'garden_planner'
app.config["MONGO_URI"] = 'mongodb+srv://CP3O:iYmkh8QOgi2fhu2y@lemoenskil-4vjdx.mongodb.net/garden_planner?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_plant_record')
def get_plant_record():
    return render_template("plant_records.html", plant_data=mongo.db.plant_data.find())
    
@app.route('/')
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            