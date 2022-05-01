from flask import render_template, url_for
from . import main
from ..requests import get_sources, get_articles


@main.route('/')
def index():
    news_sources = get_sources()
    return render_template('index.html', news_sources = news_sources)

@main.route('/source/<id>')
def source(id):
    source = get_articles(id)
    return render_template('source.html', source = source)