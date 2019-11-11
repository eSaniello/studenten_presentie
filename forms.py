from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateTimeField


class UpdatePresentieForm(FlaskForm):
    student = SelectField('student')
    vak = StringField('vak')
    presentie = StringField('presentie')
    blok = StringField('blok')
    datum = DateTimeField('datum')
    submit = SubmitField('Bewerken')
