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

def get_articles(id):

    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_sources(sources_list):
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if id:
            sources_object = Sources(id, name, description, url, category, language, country)
            sources_results.append(sources_object)

    return sources_results

def process_articles(articles_list):
    articles_results = []
    for source_item in articles_list:
        author = source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        urlToImage = source_item.get('urlToImage')
        publishedAt = source_item.get('publishedAt')
        content = source_item.get('content')
        if urlToImage:
            articles_object = Articles(author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(articles_object)

    return articles_results


        