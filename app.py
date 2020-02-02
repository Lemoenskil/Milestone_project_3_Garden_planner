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
    plant_cards = mongo.db.plant_data.find().sort([('views', DESCENDING)]).limit(6)
    return render_template("plant_records.html", title="Home", plants=plant_cards)


@app.route('/view_plant/<plant_id>')
def view_plant(plant_id):
    """Shows full plant details"""
    mongo.db.plant_data.find_one(
        {'_id': ObjectId(plant_id)},
    )
    plant_db = mongo.db.plant_data.find_one_or_404({'_id': ObjectId(plant_id)})
    return render_template("view_plant.html", plant=plant_db)
    
@app.route('/update_plant/<plant_id>')
def update_plant(plant_id):
    plants =  mongo.db.plant_data.find_one({"_id": ObjectId(plant_id)})
    return render_template('update_plant.html', plant=plants)
                           
                           
@app.route('/edit_plant/<plant_id>', methods=["POST"])
def edit_plant(plant_id):
    plants = mongo.db.plant_data
    plants.update( {'_id': ObjectId(plant_id)},
    {
        'plant_name':request.form.get('plant_name'),
        'picture_link':request.form.get('picture_link'),
        'crop_group': request.form.get('crop_group'),
        'crop_family': request.form.get('crop_family'),
        'soil':request.form.get('soil'),
        'frost_tolerant':request.form.get('frost_tolerant'),
        'feeding':request.form.get('feeding'),        
        'companions':request.form.get('companions'),        
        'spacing':request.form.get('spacing'), 
        'Sow_and_Plant':request.form.get('Sow_and_Plant'), 
        'Harvesting':request.form.get('Harvesting'), 
        'Pests':request.form.get('Pests'), 
        'Note':request.form.get('Note'), 
    })
    return redirect(url_for('view_plant'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            