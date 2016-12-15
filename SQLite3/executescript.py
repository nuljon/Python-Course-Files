import sqlite3

with sqlite3.connect('test_database.db') as connection:
	c=connection.cursor()
	c.executescript("""
	DROP TABLE IF EXISTS People;
	CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
	INSERT INTO People VALUES('Ron', 'Obvious', 42);
	""")
