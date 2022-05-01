import os

class Config:

    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?country=us&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
