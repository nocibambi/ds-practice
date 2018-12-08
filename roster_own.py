import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    -- This is a composite primary key
    -- There can be multiple instances of the same foreign keys
    -- but their combinations need to be unique
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input("File to load:")
if not fname: fname = ("roster_data.json")

json_text = open(fname).read()
json_data = json.loads(json_text)

for item in json_data:
    user_name = item[0]
    course_code = item[1]
    role = item[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (user_name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (user_name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course_code,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course_code,))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

conn.commit()

conn.close()
