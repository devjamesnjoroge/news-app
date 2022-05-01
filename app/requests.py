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


def get_sources():
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    
    return sources_results
