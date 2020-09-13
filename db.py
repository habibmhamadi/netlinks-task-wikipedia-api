import sqlite3 as lite

class DB():
    con = None
    def __init__(self):
        if self.con is None:
            try:
                self.con = lite.connect('articles.db')
                cur = self.con.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS articles
                    (id INTEGER PRIMARY KEY,title TEXT,desc TEXT);''')
                self.con.commit()
            except lite.Error:
                print(lite.Error)

    def insert(self,title,desc):
        try:
            data = (title,desc)
            cur = self.con.cursor()
            cur.execute('INSERT INTO articles(title,desc) values (?,?)',data)
            self.con.commit()
            print('Article added successfully')
        except lite.Error:
            print(lite.Error)

    def showAll(self,order='id',limit=10):
        try:
            cur = self.con.cursor()
            data = (order,limit)
            cur.execute('SELECT * FROM articles ORDER BY ? LIMIT ?',data)
            records = cur.fetchall()
            return records
        except lite.Error:
            print(lite.Error)
            return None

    def where(self,value,order='title',limit=5):
        try:
            cur = self.con.cursor()
            cur.execute('SELECT * FROM articles where title like ? ORDER BY ? LIMIT ?',('%'+str(value)+'%',order,limit))
            records = cur.fetchall()
            return records
        except lite.Error:
            print(lite.Error)
            return None

    def show(self,id):
        try:
            cur = self.con.cursor()
            data = (id,)
            cur.execute('SELECT * FROM articles WHERE ID = ?',data)
            records = cur.fetchone()
            return records
        except lite.Error:
            print(lite.Error)

    def delete(self,id):
        try:
            cur = self.con.cursor()
            data = (id,)
            cur.execute('DELETE FROM articles WHERE ID = ?',data)
            self.con.commit()
        except lite.Error:
            print(lite.Error)

            


