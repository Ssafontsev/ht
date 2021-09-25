import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/hometask')
engine
connection = engine.connect()

# sel = connection.execute("""SELECT album_name, year FROM album
# WHERE year = 2018;
# """).fetchall()
# sel = connection.execute("""SELECT title, time FROM track
# WHERE time = (SELECT MAX(time) FROM track);
# """).fetchall()
# sel = connection.execute("""SELECT title, time FROM track
# WHERE time >= 3.5;
# """).fetchall()
# sel = connection.execute("""SELECT title FROM collection
# WHERE year >= 2018 and year <= 2020;
# """).fetchall()
# sel = connection.execute("""SELECT name FROM artist
# WHERE name NOT LIKE ('%% %%');
# """).fetchall()
# sel = connection.execute("""SELECT title FROM track
# WHERE title iLIKE ('%%my%%');
# """).fetchall()

pprint(sel)
