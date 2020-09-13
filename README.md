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

## Modules Used

**urlib3**  for http request
**sqlite3**  for storing offline data
**json**  for parsing json data
**re**  regular expression for removing html tags
**shutil**  for taking backup
**os**  for making directory
**XlsxWriter**  for creating and reading excel files