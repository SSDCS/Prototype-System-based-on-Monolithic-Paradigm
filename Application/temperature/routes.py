"""
Temperature
"""
from flask import render_template
from Application.temperature import bp
from tests import consumers

#@bp.route('/')
#def show_temp():
#    return render_template('templates/temperature.html')
@bp.route('/temperature', methods=['GET', 'POST'])
def temperature1():
    return render_template('templates/temperature.html')
@bp.route('/temperature/<value>', methods=['GET', 'POST'])
def temperature2(value):
    return "Temperature is: "+value
