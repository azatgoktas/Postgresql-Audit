import psycopg2
from connect import connect
from color_print import print_red, print_green

#get users who have grant option

class show_grantees():
    print("Checking users who have grant option")
    global cur

    db = connect()
    cur = db.cur

    def get_grantees(): #get users who have privileges on pg_catalog.pg_authid
        cur.execute("""SELECT grantee
                        FROM information_schema.role_table_grants
                        where is_grantable = 'YES'
                        group by grantee
                        """)

    try:
        get_grantees()
        grantees = cur.fetchall()
    except psycopg2.Error as err:
        print("Error: Fetching privileges on pg_catalog failed ",err)

    users = ""
    for grantee in grantees:
        for user in grantee:
            users += user + " "

    print(users + " have grant option. Revoke if it is unnecessary")
