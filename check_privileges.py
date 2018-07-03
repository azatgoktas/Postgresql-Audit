import psycopg2
from connect import connect

#- Check that only the DBA has SUPERUSER, CREATEDB oder CREATEROLE privileges.

class check_privileges():

    global cur

    db = connect()
    cur = db.cur

    def get_database_users_and_privileges():
        cur.execute("""SELECT grantee, privilege_type
                        FROM information_schema.role_table_grants
                        """)

    # dba = input("enter dba admin ")
    dba = "postgres"

    #Get database users and privileges
    try:
        get_database_users_and_privileges()
        users_and_privigiles = cur.fetchall()
    except psycopg2.Error as err:
        print("error fetching users")

    #check if regular db users have superuser createdb or createrole privileges
    for user_and_privigile in users_and_privigiles:
        privigile = user_and_privigile[1].lower()
        user = user_and_privigile[0].lower()
        if ("superuser" in privigile) or ("createdb" in privigile) or ("createrole" in privigile):
            if user != dba:
                print_red("Critical issue :" + user + " has " + privigile + " privigile which is not recommended")
            else:
                print_green("OK")
