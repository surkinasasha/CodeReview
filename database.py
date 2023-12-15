import sqlite3
from my_parser import sum_articles
from config import DATABASE
articles = sum_articles()
def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    sql ="CREATE TABLE articles (title TEXT, link TEXT, date TEXT)"
    cursor.execute(sql)
    conn.close()
def clear_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    sql = "DELETE FROM articles"
    cursor.execute(sql)
    conn.commit()
    conn.close()
def fill_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO articles VALUES (?, ?, ?)", articles)
    conn.commit()
    conn.close()
