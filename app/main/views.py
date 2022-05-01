from flask import render_template
from . import main
from ..requests import get_sources


@main.route('/')
def index():
    get_sources()
    return render_template('index.html')