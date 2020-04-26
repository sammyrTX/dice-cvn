from flask_wtf import FlaskForm

from wtforms import (IntegerField,
                     SubmitField,
                     BooleanField,
                     SelectField,
                     )

from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired, InputRequired


class DiceHold(FlaskForm):
    dice_hold = IntegerField('Dice_to_Hold', validators=[DataRequired()])
    enter = SubmitField('Enter')


class DiceHoldWeb(FlaskForm):
    die1 = BooleanField('--- One ---')
    die2 = BooleanField('--- Two ---')
    die3 = BooleanField('--- Three ---')
    die4 = BooleanField('--- Four ---')
    die5 = BooleanField('--- Five ---')
    roll_dice = SubmitField('Roll Dice')


class RollTwo(FlaskForm):
    die2 = SelectField(u'Die No. 2', choices=[('die2', '-- 2 --'),
                                              ('die3', '-- 3 --')])
    roll_dice = SubmitField('Roll Dice 2')
