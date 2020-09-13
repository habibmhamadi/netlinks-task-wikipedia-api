from urllib3 import PoolManager
from json import loads
from re import fullmatch, sub
from shutil import copy
from os import path, mkdir
from db import DB
import xlsxwriter as xl


http = PoolManager()
con = DB()


def getData():
    '''Get random article from Wikipedia'''
    result = http.request('GET','https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=extracts&rvprop=content&grnlimit=1')
    data = loads(result.data)
    pages = data['query']['pages']

    for i in pages.values():
        desc = i['extract']
        desc = sub('<.+?>',' ',desc,len(desc))
        return {'title':i['title'],'desc':desc}


def show_web_articles():
    '''Shows fetched articles to user'''
    while True:
        article = getData()
        print('\n',article['title'])
        x = input('\nEnter r to read this article, n to show next article or else to go to main menu: ')
        if x=='r':
            print('\n',article['desc'])
            y = input('\nEnter n to show next, s to save to DB or else go to main menu: ')
            if y=='n': continue
            elif y=='s' : save_to_db(article['title'],article['desc'])
            else: break
        elif x =='n': continue
        else: break


def show_db_articles():
    '''Shows menu for local DB articles'''
    while True:
        x = input('\nEnter 1 to show articles 2 to search articles or else to go to main menu: ')
        if x=='1': list_db_articles()
        elif x=='2':
            y = input('Enter artcle title: ')
            list_db_articles(y)
        else: break


def save_to_db(title,desc):
    '''Saves an article to local DB'''
    con.insert(title,desc)


def list_db_articles(prefix=None):
    '''Shows saved articles from local DB'''
    while True:
        data = con.where(prefix) if prefix!=None else con.showAll()
        if data!=None:
            for i in data:
                print(str(i[0])+'    '+i[1])
            if len(data)>0:
                x = input('\nEnter article id to show or else to go back: ')
                if fullmatch('[0-9]',x):
                    print('\n')
                    l = con.show(x)
                    if l!=None:
                        print('\n'+str(l))
                        y = input('\nEnter d to delete or else to go back: ')
                        if y=='d': con.delete(x)
                        else: break
                else: break
            else: print('\nNo records found!\n'); break
        else: print('\nNo records found!\n'); break


def get_backup():
    try:
        if path.isfile('articles.db'):
            if not path.isdir('backup'):
                mkdir('backup')
            copy('articles.db','backup/articles.db')
            print('\nBackup successfull')
        else: print('Error, DB file not found')
    except Exception as e:
        print(e)


def write_to_excel():
    if not path.isdir('excel'):
        mkdir('excel')
    wk = xl.Workbook('articles.xlsx')
    ws = wk.add_worksheet()
    ws.set_column('B:B',20)
    ws.set_column('C:C',40)
    bold = wk.add_format({'bold': True})
    ws.write('A1','ID',bold)
    ws.write('B1','TITLE',bold)
    ws.write('C1','DESCRIPTION',bold)
    data = con.showAll()
    j = 0
    for i in data:
        ws.write(j+1,0,i[0])
        ws.write(j+1,1,i[1])
        ws.write(j+1,2,i[2])
        j = j + 1
    wk.close()
    print('\nExcel file created!')


while True:
    a = input('\nEnter 1 for local DB\nEnter 2 for random articles from the WEB\nEnter 3 to backup local DB\nEnter 4 to create Excel sheet\nEnter q to quit: ')
    if a=='1': show_db_articles()
    elif a=='2': show_web_articles()
    elif a=='3': get_backup()
    elif a=='4': write_to_excel()
    elif a=='q': print('\nbye!'); break
    else: print('\nInvalid input')
