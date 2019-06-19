import psycopg2
import sys

con = None
fout = None

try:
    con = psycopg2.connect(database='postgres',
                           user='postgres',
                           password='test')
    cur = con.cursor()
    cur.execute("SELECT NAME,ID FROM players WHERE CLUB IN %s;",
                (tuple(['Chelsea']), ))
    cur.fetchall()
    con.commit()

except psycopg2.DatabaseError as e:

    if con:
        con.rollback()

    print(f'Error {e}')
    sys.exit(1)
except IOError as e:

    if con:
        con.rollback()

    print(f'Error {e}')
    sys.exit(1)

finally:
    if con:
        con.close()
