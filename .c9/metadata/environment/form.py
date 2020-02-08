{"filter":false,"title":"form.py","tooltip":"/form.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":47,"column":19},"action":"insert","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField","from wtforms.validators import DataRequired, Length, EqualTo, Email","","","class LoginForm(FlaskForm):","    username = StringField('Username', validators=[DataRequired()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember_me = BooleanField('Remember Me')","    submit = SubmitField('Sign In')","","","class RegisterForm(FlaskForm):","    username = StringField('Username', validators=[DataRequired(),","                                                   Length(min=4, max=20)])","    password = PasswordField('Password',","                             validators=[DataRequired(),","                                         EqualTo('password2', message='Passwords must match')])","    password2 = PasswordField('Repeat Password')","    email = StringField('Email Address', validators=[Length(min=6, max=35), Email()])","    remember_me = BooleanField('Remember Me')","    submit = SubmitField('Register')","","","class CreateRecipeForm(FlaskForm):","    title = StringField('Title', validators=[DataRequired()])","    short_description = TextAreaField('Short Description', validators=[DataRequired()])","    ingredients = TextAreaField('Ingredients (one per line please)', validators=[DataRequired()])","    method = TextAreaField('Instructions', validators=[DataRequired()])","    tags = StringField('Tags (separate by comma please)', validators=[DataRequired()])","    image = StringField('Image Link (full path)', validators=[DataRequired()])","    submit = SubmitField('Add Recipe')","","","class EditRecipeForm(FlaskForm):","    title = StringField('Title', validators=[DataRequired()])","    short_description = TextAreaField('Short Description', validators=[DataRequired()])","    ingredients = TextAreaField('Ingredients (one per line please)', validators=[DataRequired()])","    method = TextAreaField('Instructions', validators=[DataRequired()])","    tags = StringField('Tags (separate by comma please)', validators=[DataRequired()])","    image = StringField('Image Link (full path)', validators=[DataRequired()])","    submit = SubmitField('Update Recipe')","","","class ConfirmDelete(FlaskForm):","    title = StringField('Title', validators=[DataRequired()])","    submit = SubmitField('Delete this Recipe')","© 2020 GitHub, Inc."],"id":1}],[{"start":{"row":47,"column":18},"end":{"row":47,"column":19},"action":"remove","lines":["."],"id":2},{"start":{"row":47,"column":17},"end":{"row":47,"column":18},"action":"remove","lines":["c"]},{"start":{"row":47,"column":16},"end":{"row":47,"column":17},"action":"remove","lines":["n"]},{"start":{"row":47,"column":15},"end":{"row":47,"column":16},"action":"remove","lines":["I"]},{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"remove","lines":[" "]},{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"remove","lines":[","]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"remove","lines":["b"]},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"remove","lines":["u"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"remove","lines":["H"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"remove","lines":["t"]}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"remove","lines":["i"],"id":3},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"remove","lines":["G"]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"remove","lines":[" "]},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"remove","lines":["0"]},{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"remove","lines":["2"]},{"start":{"row":47,"column":3},"end":{"row":47,"column":4},"action":"remove","lines":["0"]},{"start":{"row":47,"column":2},"end":{"row":47,"column":3},"action":"remove","lines":["2"]},{"start":{"row":47,"column":1},"end":{"row":47,"column":2},"action":"remove","lines":[" "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":1},"action":"remove","lines":["©"]},{"start":{"row":46,"column":46},"end":{"row":47,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":22,"column":0},"end":{"row":46,"column":46},"action":"remove","lines":["","","class CreateRecipeForm(FlaskForm):","    title = StringField('Title', validators=[DataRequired()])","    short_description = TextAreaField('Short Description', validators=[DataRequired()])","    ingredients = TextAreaField('Ingredients (one per line please)', validators=[DataRequired()])","    method = TextAreaField('Instructions', validators=[DataRequired()])","    tags = StringField('Tags (separate by comma please)', validators=[DataRequired()])","    image = StringField('Image Link (full path)', validators=[DataRequired()])","    submit = SubmitField('Add Recipe')","","","class EditRecipeForm(FlaskForm):","    title = StringField('Title', validators=[DataRequired()])","    short_description = TextAreaField('Short Description', validators=[DataRequired()])","    ingredients = TextAreaField('Ingredients (one per line please)', validators=[DataRequired()])","    method = TextAreaField('Instructions', validators=[DataRequired()])","    tags = StringField('Tags (separate by comma please)', validators=[DataRequired()])","    image = StringField('Image Link (full path)', validators=[DataRequired()])","    submit = SubmitField('Update Recipe')","","","class ConfirmDelete(FlaskForm):","    title = StringField('Title', validators=[DataRequired()])","    submit = SubmitField('Delete this Recipe')"],"id":4}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":22,"column":0},"end":{"row":22,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1581014615731,"hash":"e22e4b41915d6e2fd827198585aa2148a654b1ed"}