import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/postgres')
engine
connection = engine.connect()

# sel = connection.execute("""SELECT * FROM film;
# """).fetchone()
# sel = connection.execute("""SELECT title FROM film;
# """).fetchmany(10)
sel = connection.execute("""SELECT first_name, last_name FROM actor;
""").fetchmany(10)
pprint(sel)
