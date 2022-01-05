import sqlite3
from contextlib import closing

# NOTE: delete aquarium.db if it already exists, before running this

connection = sqlite3.connect('aquarium.db')
# passing ':memory:' instead results in database in memory only

# create a table example
cursor = connection.cursor()
cursor.execute('CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)')

# insert examples
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

# select example - all
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

# select example - one
target_fish_name = 'Jamie'
rows = cursor.execute(
    "SELECT name, species, tank_number FROM fish WHERE name = ?",
    (target_fish_name,),
).fetchall()
print(rows)

# update example
new_tank_number = 2
moved_fish_name = 'Sammy'
cursor.execute(
    "UPDATE fish SET tank_number = ? WHERE name = ?",
    (new_tank_number, moved_fish_name, )
)
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

# delete example
released_fish_name = 'Sammy'
cursor.execute(
    "DELETE FROM fish WHERE name = ?",
    (released_fish_name, )
)
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

# show how many rows were affected
print(connection.total_changes)

# closing the cursor and the connection
with closing(connection):
    with closing(cursor):
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)
