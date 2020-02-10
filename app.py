import os
from flask import Flask, render_template, redirect, abort, request, url_for, session, flash
from flask_pymongo import PyMongo
from form import LoginForm, RegisterForm
from bson.objectid import ObjectId
import math
import re
import bcrypt



app = Flask ("----name----")
app.config["MONGO_DBNAME"] = 'garden_planner'
app.config["MONGO_URI"] = 'mongodb+srv://CP3O:iYmkh8QOgi2fhu2y@lemoenskil-4vjdx.mongodb.net/garden_planner?retryWrites=true&w=majority'

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.environ.get('SECRET_KEY') or 'y6rdh777y685hf67gk9786j65g9h*&^^*(^'

plants_per_page = 6

mongo = PyMongo(app)

@app.route('/')
@app.route('/plant_records')
def get_plant_record():
    page_number = int(request.args.get('page', 1))
    plants_to_skip = (page_number - 1) * plants_per_page
    plant_count = mongo.db.plant_data.count({})
    page_count = int(math.ceil(plant_count / plants_per_page))
    page_numbers = range(1, page_count + 1)
    plants_on_page = mongo.db.plant_data.find().skip(plants_to_skip).limit(plants_per_page)
    return render_template("plant_records.html", title="Home", plants=plants_on_page, page=page_number, pages=page_numbers, total=page_count)

@app.route('/register', methods=['GET', 'POST'])
def register_new_user():
    """Registers a new user"""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        all_existing_users = mongo.db.user_data
        found_user = all_existing_users.find_one({
            'name': request.form['username']
        })

        if found_user:
            flash(f"Username `{request.form['username']}` is already taken. Please try a different username.")
        else:
            # Convert password to hash to prevent password leakage should we get hacked 
            hashed_password = bcrypt.hashpw(
                request.form['password'].encode('utf-8'),
                bcrypt.gensalt()
            )
            all_existing_users.insert_one({
                'name': request.form['username'],
                'password': hashed_password,
                'email': request.form['email']
            })
            # User successfully registered, so treat the user as logged in.
            session['username'] = request.form['username']
            return redirect(url_for('get_plant_record'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user in"""
    if session.get('logged_in') is True:
        return redirect(url_for('get_plant_record', title="Sign In"))

    form = LoginForm()

    if form.validate_on_submit():
        all_existing_users = mongo.db.user_data
        found_user = all_existing_users.find_one({
            'name': request.form['username']
        })

        if found_user:
            password_matches = bcrypt.checkpw(
                request.form['password'].encode('utf-8'),
                found_user['password']
            )
            if password_matches:
                # Successful log-in: Store and redirect
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('get_plant_record', title="Sign In", form=form))
            flash('Invalid username / password combination')
    return render_template("login.html", title="Sign In", form=form)

@app.route('/logout')
def logout():
    """Logs the user out"""
    session.clear()
    return redirect(url_for('get_plant_record'))


@app.route('/list_plant') 
def list_plant():
    return render_template("list_plant.html", plants=mongo.db.plant_data.find())

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
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("add_plant.html")
 
@app.route('/insert_plant', methods=['POST'])
def insert_plant():
    if 'username' not in session:
        abort(401)
    plants = mongo.db.plant_data
    plants.insert_one(convert_form_to_plant_data(request.form))
    return redirect(url_for('get_plant_record'))
    
@app.route('/update_plant/<plant_id>')
def update_plant(plant_id):
    if 'username' not in session:
        return redirect(url_for('login'))
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
    print("whapsie")
    if 'username' not in session:
        abort(401)
    plants = mongo.db.plant_data
    plants.update( {'_id': ObjectId(plant_id)}, convert_form_to_plant_data(request.form))
    return redirect(url_for('get_plant_record'))
    
@app.route('/delete_plant/<plant_id>')
def delete_plant(plant_id):
    print("oopsie")
    if 'username' not in session:
        abort(401)
    mongo.db.plant_data.remove({'_id': ObjectId(plant_id)})
    return redirect(url_for('get_plant_record'))

@app.route('/search')
def search():
    """Provides logic for search bar"""
    query_A = request.args['query'].strip()
    regx = re.compile(f".*{query_A}.*", re.IGNORECASE)
    query = {'$regex': regx }
    results = mongo.db.plant_data.find({
        '$or': [
            {'plant_name': query},
            {'Note': query},
            {'crop_group': query},
        ]
    })
    return render_template('search_results.html', query=query_A, results=results)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            