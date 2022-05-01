from flask import render_template
from . import main
from ..requests import get_sources


@main.route('/')
def index():
    news_sources = get_sources()
    return render_template('index.html', news_sources = news_sources)