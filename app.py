from flask import Flask, render_template, url_for
import sqlite3
from database import create_database, clear_database, fill_database
from my_parser import today
from config import DATABASE
import schedule
import time

def update():
    clear_database()
    fill_database()
if __name__ == "__app.py__":
    try:
        schedule.every().hour.do(update) 
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as ex: 
        print(ex)
        time.sleep(2)
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
if __name__ == '__main__':
    create_database()
    fill_database()
    app.run(debug=True)

