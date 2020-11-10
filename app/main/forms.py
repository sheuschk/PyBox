from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField


class CreateLobby(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Create')


class RegisterUser(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    code = StringField('Lobby Code', validators=[DataRequired()])
    submit = SubmitField('Join')


class StartGame(FlaskForm):
    start = SubmitField('Start')
