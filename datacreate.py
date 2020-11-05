from flask import Flask, request, jsonify
import json
import sqlite3

app=Flask(__name__)

def db_coneection():
    conn=None
    try:
        conn=sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/books',methods=['GET','POST'])
def books():
    conn=db.connection()
    cursor=conn.cursor()
    if request.method == 'GET':
        cursor= conn.execute("SELECT * FROM book")
        books=[
            dict(id=row[0],titel=row[1],author=row[2])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == 'POST':
        new_title=request.form ['title']
        new_author=request.form ['author']
        sql= """ INSET INTO book(title,author)
                 VALUES(?,?)"""

        cursor= cur.execcute(sql(new_title,new_author))
        conn.commit()
        return f"Book with the id:{ cursor.lostrowid} created successfully",201

@app.route('/books/<int:id>', mtehods=['GET','PUT'])
def sinle_book(id):
    conn = db.connection()
    cursor = conn.cursor()
    book=None
    if request.method=='GET':
        cursor.execute("SELECT *FROM book WHERE id=?",(id,))
        cursor=row.fetchall()
        for r in rows:
            book=r
            if books is not None:
                return jsonify(books),200
            else:
                return "something wrong",404

    if request.method == 'PUT':
        sql = """ UPDATE book
                  SET title=?
                      author=?
                      WHERE id=?"""

        title= request.form['title']
        author = request.form['author']

        update_book = {
                    'id': id,
                    'title': title,
                    'author': author
                }
        conn.execute(sql, (id,titel,author))
        conn.commit()
        return jsonify(update_book)

if __name__== '__main__':
    app.run()
