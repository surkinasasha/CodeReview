from flask import Flask, render_template, url_for
import sqlite3
from database import create_database, clear_database, fill_database
import threading
from my_parser import today
from config import DATABASE
def update():
    threading.Timer(60.0, update).start()
    clear_database()
    fill_database()
#update()
def get_db():
     conn = sqlite3.connect(DATABASE)
     cursor = conn.cursor()
     sql="SELECT * FROM articles"
     cursor.execute(sql)
     res = cursor.fetchall()
     if len(res) == 0:
        return [("Статей нет", "", today())]
     else:
        return res
     conn.close()
app = Flask(__name__)
@app.route('/')
def index():
    articles = get_db()
    return render_template("index.html", articles = articles)

if __name__ == "__main__":
     app.run(debug=True)
 