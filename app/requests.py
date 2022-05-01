import urllib.request, json
from .models import Sources, Articles

# Getting api key
api_key = None

# Getting the base_urls
sources_url = None
articles_url = None

def configure_request(app):
    global api_key, sources_url, articles_url

    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_API_SOURCE_URL']
    articles_url = app.config['NEWS_API_ARTICLES_URL']