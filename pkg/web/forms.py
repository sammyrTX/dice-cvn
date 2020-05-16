from flask_wtf import FlaskForm

from wtforms import (IntegerField,
                     SubmitField,
                     BooleanField,
                     TextField,
                     )

# from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired


class DiceHold(FlaskForm):
    """Dice to be held. (Not in use)"""
    dice_hold = IntegerField('Dice_to_Hold', validators=[DataRequired()])
    enter = SubmitField('Enter')


class DiceHoldWeb(FlaskForm):
    """Track which dice are being kept"""
    die1 = BooleanField('--- One ---')
    die2 = BooleanField('--- Two ---')
    die3 = BooleanField('--- Three ---')
    die4 = BooleanField('--- Four ---')
    die5 = BooleanField('--- Five ---')
    roll_dice = SubmitField('Roll Dice')


class CategorySelect(FlaskForm):
    """Display available scoring categories"""
    category_selection = TextField('Category')
    select = SubmitField('Select')
