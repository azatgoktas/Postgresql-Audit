import psycopg2
from connect import cur
from get_last_version import version_number #fetching version from website

#- Check that you are running the latest release for your version of PostgreSQL.
print("Checking postgres version.")

def get_last_version_of_postgres():
    cur.execute("select version()")

try :
    get_last_version_of_postgres()
    versionArr = cur.fetchall()
except psycopg2.Error as err:
    print("Error: Fetching last version")

versionStr = ""
for versionA in version_number:
    for versionText in versionA:
        versionStr += str(versionText)

if versionStr != version_number:
    print("Warning: Please update your postgresql. "+ version_number + " is avaliable.")
)
