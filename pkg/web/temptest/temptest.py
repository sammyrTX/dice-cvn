from flask import Blueprint, render_template

temptest_bp = Blueprint('temptest_bp',
                        __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='assets',
                        )


@temptest_bp.route('/')
def test01():
    name = 'MunroLive'
    return render_template('temptest/test01.html', name=name)
