import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="platzi_flask",
    user="postgres",
    password="Unapologetic98"
)

cur = con.cursor()


def get_users():
    cur.execute("select * from users")
    rows = cur.fetchall()
    cur.close()
    con.close()

    return rows


def get_alls(username):
    cur.execute("select description from alls where username = '{}'".format(username))
    rows = cur.fetchall()
    cur.close()
    con.close()

    return rows
