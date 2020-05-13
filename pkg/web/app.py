"""framework for web app version of dice-cvn game"""

from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   )

from . forms import (DiceHold,
                     DiceHoldWeb,
                     )

from .. diceroll.dice import (die_roll,
                              dice_png,
                              )

from .. gameprocessing.play_game import (start_game,
                                         game_status,
                                         )
from .. scorekeeping.scorepad import Scorepad_


from .. web.webgame.webgame import webgame_bp
from .. web.temptest.temptest import temptest_bp  # Test only - Remove

# Remove after HTML complete
from .. scorekeeping.scoredisplay import show_current_score


app = Flask(__name__)

app.config['SECRET_KEY'] = 'toASMuE59soIk7*9jA*F'

app.register_blueprint(webgame_bp, url_prefix='/webgame')
app.register_blueprint(temptest_bp, url_prefix='/temptest')  # Test only - Remove


@app.route('/')
def index():
    """Index page for webgame"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
