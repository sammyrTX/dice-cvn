from flask_wtf import FlaskForm

from wtforms import (IntegerField,
                     SubmitField,
                     )

from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired, InputRequired


class DiceHold(FlaskForm):
    dice_hold = IntegerField('Dice_to_Hold', validators=[DataRequired()])
    enter = SubmitField('Enter')
