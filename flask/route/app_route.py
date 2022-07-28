from flask import Blueprint, render_template
NAME = 'first_route'
app_route = Blueprint(NAME, __name__)


@app_route.route('/')
def index():
    return render_template('index.html')