import psycopg2
from connect import cur

#- Check that nobody except for superusers has any privileges on pg_catalog.pg_authid.
print("Checking privileges on pg_catalog.pg_authid.")

def get_privileges_on_pg_catalog(): #get users who have privileges on pg_catalog.pg_authid
    cur.execute("""SELECT grantee
                    FROM information_schema.role_table_grants
                    where table_schema = 'pg_catalog'
                    and table_name = 'pg_authid'
                    group by grantee
                    """)

def get_superusers():
    # cur.execute("""SELECT usename
    #                 from pg_user
    #                 where usesuper = true
    #             """)
    cur.execute("""SELECT *
                    FROM pg_catalog.pg_authid
                    where rolsuper = true
                    """)

try:
    get_privileges_on_pg_catalog()
    users_on_pg_catalog = cur.fetchall()
except psycopg2.Error as err:
    print("Error: Fetching privileges on pg_catalog failed ",err)

try:
    get_superusers()
    superusers = cur.fetchall()
except psycopg2.Error as err:
    print("Error: Fetching superusers failed",err)


superList = []
for super in superusers: #creating super user list.
    for superuser in super:
        superList.append(superuser)

for users in users_on_pg_catalog:
    for user in users:
        if user not in superList: # if that user not super user print an error.
             print("Critical Error: " + user + " has privileges on pg_catalog.pg_authid. "
             + user + " must be a superuser")
        else:
             print("OK")
