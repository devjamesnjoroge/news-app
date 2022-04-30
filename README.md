# NEWS APP
## By `devjamesnjoroge`
---
## BRIEF ABOUT

### This is a basic flask application running on python 3 that uses the [NEWS API](https://newsapi.org/) to display various news articles.

## USER STORIES

- A user can see various news sources on the homepage of the application.

- A user can select a news source and see all news articles from the selected news source in the application.

- A user can see the image, description and the time a news article was created.

- A user can click on an article and read the full article on the source website.

## REQUIREMENTS

- A PC running on any OS with terminal

- A code editor. *Recommended VSCODE*

- python3 is installed in the terminal

- knowledge on the CLI

## USAGE
**First clone this repo**
```
git clone https://github.com/devjamesnjoroge/news-app.git
```

**Launch virtual environment**
```
python -m venv virtual

source virtual/bin/activate
```

**Install all the app dependencies**
```
pip install -r requirements.txt 
```
**To run website**
```
python3 manage.py server
```

## DATE

**30 APRIL 2022**

## FOLDER STRUCTURE

| app | tests | config.py | manage.py | start.sh|
|-----| :---: | :-------: | :-------: | ------: |
|main | `models_test.py`| `os.environ` variables|running app| hiding secret keys|
|static|
| templates|
| `__init__.py`|
|`models.py`|
|`requests.py`|


## LICENSE

[MIT LICENSE](LICENSE)

[Go back to the top](#)
