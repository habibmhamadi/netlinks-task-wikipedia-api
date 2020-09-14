# Wikipedia API

This is a python3 command line program for fetching random articles from [Wikipedia](https://wikipedia.com)

## Features
    
- Fetch article online
- Save article to local sqlite database
- Fetch article from local Database
- Read article
- Delete article
- Search article
- Backup database
- Creates excel sheet for articles


## required dependency

install *xlsxwriter* modul for python3

```
pip3 install xlsxwriter
```

## Usage

```python
from wiki import WikiApp

#Create a new object of WikiApp and call start() method
app = Wiki()
app.start()
```

## Contribution

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository.

