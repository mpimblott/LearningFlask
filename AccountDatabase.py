import os
from sqlalchemy import create_engine, MetaData, Table, Column, String

database_url = os.environ['DATABASE_URL']

print(database_url)

database = create_engine(database_url, echo=True)


def add_user(db, username, password, joinDate, admin):
    db.execute("INSERT INTO users (id, username, password, joinDate, admin ) VALUES"
               " ('1', %s, %s, %s, %s)", (username, password, joinDate, int(admin)))


def create_users_table(db):
    # Create
    db.execute("CREATE TABLE IF NOT EXISTS users (id integer, username text, "
               "password text, joinDate date, admin integer)")
    db.execute("INSERT INTO users (id, username, password, joinDate, admin ) VALUES"
               " ('1', 'matthew', 'password', '2017-09-11', '1')")


def clear_users(db):
    db.execute("DELETE FROM users *")


def print_users(db):
    # Read
    result_set = db.execute("SELECT * FROM films")
    for r in result_set:
        print(r)

    # Update
    db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")

    # Delete
    db.execute("DELETE FROM films WHERE year='2016'")
    # db.execute("DROP TABLE IF EXISTS FILMS")


add_user(database, 'bob', 'mybestpassword', '2019-12-12', 1)
# clear_users(database)
# add_user(database, 'fred', '1234', '2017-09-11', 1)

