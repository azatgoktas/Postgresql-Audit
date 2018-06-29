import psycopg2
from connect import cur
from color_print import print_red, print_green

#- Check that no privileges on objects are granted to PUBLIC.
print("Checking privileges on granted to PUBLIC")

def get_public_privileges():
    cur.execute("""SELECT *
                    FROM information_schema.role_table_grants
					where grantee = 'PUBLIC'
                    """)

try:
    get_public_privileges()
    privileges = cur.fetchall()
except psycopg2.Error as err:
    public("Error: Fetching public privileges failed ",err)

if len(privileges) > 0 :
    print_red("Critical Error: there is some privileges are granted to PUBLIC")
    # print(Fore.RED + "Critical Error: there is some privileges are granted to PUBLIC")
    # print("Critical Error: there is some privileges are granted to PUBLIC")
else:
    print_green("Ok")
