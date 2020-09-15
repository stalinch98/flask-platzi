import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="platzi_flask",
    user="postgres",
    password="Unapologetic98"
)

cur = con.cursor()


def get_user(username):
    rows = []
    data = ()

    try:
        cur.execute("select * from users where username = '{}'".format(username))
        rows = cur.fetchall()
        for row in rows:
            data = row
    except:
        print("Error: unable to fetch data")

    cur.close()
    con.close()
    return data


def get_alls(username):
    rows = []
    all = ""
    try:
        cur.execute("select description from alls where username = '{}'".format(username))
        rows = cur.fetchall()
        for row in rows:
            all = row[0]

    except:
        print("Error: unable to fetch data")

    cur.close()
    con.close()
    return all
