import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
import math
import re

app = Flask ("----name----")
app.config["MONGO_DBNAME"] = 'garden_planner'
app.config["MONGO_URI"] = 'mongodb+srv://CP3O:iYmkh8QOgi2fhu2y@lemoenskil-4vjdx.mongodb.net/garden_planner?retryWrites=true&w=majority'

plants_per_page = 6

mongo = PyMongo(app)

@app.route('/')
@app.route('/plant_records')
def get_plant_record():
    page_number = int(request.args.get('page', 1))
    plants_to_skip = (page_number - 1) * plants_per_page
    plant_count = mongo.db.plant_data.count_documents({})
    page_count = int(math.ceil(plant_count / plants_per_page))
    page_numbers = range(1, page_count + 1)
    plants_on_page = mongo.db.plant_data.find().skip(plants_to_skip).limit(plants_per_page)
    return render_template("plant_records.html", title="Home", plants=plants_on_page, page=page_number, pages=page_numbers, total=page_count)
    

@app.route('/view_plant/<plant_id>')
def view_plant(plant_id):
    """Shows full plant details"""
    mongo.db.plant_data.find_one(
        {'_id': ObjectId(plant_id)},
    )
    plant_db = mongo.db.plant_data.find_one_or_404({'_id': ObjectId(plant_id)})
    return render_template("view_plant.html", plant=plant_db)
    
@app.route('/add_plant')
def add_plant():
    return render_template("add_plant.html")
 
@app.route('/insert_plant', methods=['POST'])
def insert_plant():
    plants = mongo.db.plant_data
    plants.insert_one(convert_form_to_plant_data(request.form))
    return redirect(url_for('get_plant_record'))
    
@app.route('/update_plant/<plant_id>')
def update_plant(plant_id):
    plants =  mongo.db.plant_data.find_one({"_id": ObjectId(plant_id)})
    return render_template('update_plant.html', plant=plants)
                           
def convert_form_to_plant_data(form):
    value_sowing_under_glass = [ month for month in range(1, 13) if f"sowing-under-glass-{month}" in form ]
    value_outside_seeding = [ month for month in range(1, 13) if f"outside-seeding-{month}" in form ]
    value_harvest = [ month for month in range(1, 13) if f"harvest-{month}" in form ]
    return {
        'plant_name':form.get('plant_name'),
        'picture_link':form.get('picture_link'),
        'crop_group': form.get('crop_group'),
        'crop_family': form.get('crop_family'),
        'soil':form.get('soil'),
        'frost_tolerant':form.get('frost_tolerant'),
        'position':form.get('position'),
        'feeding':form.get('feeding'),        
        'companions':form.get('companions'),        
        'spacing':form.get('spacing'), 
        'Sow_and_Plant':form.get('Sow_and_Plant'), 
        'Harvesting':form.get('Harvesting'), 
        'Pests':form.get('Pests'), 
        'Note':form.get('Note'),
        'value_sowing_under_glass':value_sowing_under_glass,
        'value_outside_seeding':value_outside_seeding,
        'value_harvest':value_harvest,
    }
    
@app.route('/edit_plant/<plant_id>', methods=["POST"])
def edit_plant(plant_id):
    plants = mongo.db.plant_data
    plants.update( {'_id': ObjectId(plant_id)}, convert_form_to_plant_data(request.form))
    return redirect(url_for('get_plant_record'))
    
@app.route('/delete_plant/<plant_id>')
def delete_plant(plant_id):
    mongo.db.plant_data.remove({'_id': ObjectId(plant_id)})
    return redirect(url_for('get_plant_record'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            