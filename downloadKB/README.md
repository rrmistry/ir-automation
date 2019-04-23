# Scrape Wikipedia pages to build a knowledge base

The search starts with the initial page:

> `https://en.wikipedia.org/wiki/IFRS_17`

Followed by deep search with a maximum linked page depth limit of 2.

## Environment setup

Run the Visual Studio Code Task:

> `Environment: Create And Configure Environment`

**NOTE:** Support for MacOS and Linux may be required.

## Execution

Simply run the python command in this folder to start the Wikipedia Web-Scraping:

> `python download.py`

## Customization

To customize the root page, update any of the following constants in [download.py](download.py):

```
BASE_PATH = dir_path + "/dataset/"

BASE_PAGE = "IFRS_17"

DEPTH_LIMIT = 2
```

## Useful References

* **Most Useful**: Python Wikipedia Library:
 https://pypi.org/project/wikipedia/

* For python beautiful soup documentation:
 https://www.crummy.com/software/BeautifulSoup/bs4/doc/

* For python Multi-Threading:
 https://stackoverflow.com/questions/919897/how-to-find-a-thread-id-in-python