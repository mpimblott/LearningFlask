
import os
from sqlalchemy import create_engine, MetaData, Table, Column, String

database_url = os.environ['DATABASE_URL']

print(database_url)

database = create_engine(database_url, echo=True)


def sql_test(db):
    # Create
    db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
    db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

    # Read
    result_set = db.execute("SELECT * FROM films")
    for r in result_set:
        print(r)

    # Update
    db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")

    # Delete
    db.execute("DELETE FROM films WHERE year='2016'")
    db.execute("DROP TABLE IF EXISTS FILMS")


def sql_expression_test(db):
    meta = MetaData(db)
    film_table = Table('films', meta,
                       Column('title', String),
                       Column('director', String),
                       Column('year', String))

    with db.connect() as conn:
        # Create
        film_table.create()
        insert_statement = film_table.insert().values(title="Doctor Strange", director="Scott Derrickson", year="2016")
        conn.execute(insert_statement)

        # Read
        select_statement = film_table.select()
        result_set = conn.execute(select_statement)
        for r in result_set:
            print(r)

        # Update
        update_statement = film_table.update().where(film_table.c.year == "2016").values(title="Some2016Film")
        conn.execute(update_statement)

        # Delete
        delete_statement = film_table.delete().where(film_table.c.year == "2016")
        conn.execute(delete_statement)

        # Drop statement
        film_table.drop()


sql_test(database)


sql_expression_test(database)
