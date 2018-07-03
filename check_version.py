import psycopg2
from connect import connect
from get_last_version import get_last_version #fetching version from website
from color_print import print_red, print_green

#- Check that you are running the latest release for your version of PostgreSQL.

class check_version():
    print("Checking postgres version.")

    global cur
    global version_number

    db = connect()
    cur = db.cur

    last_version = get_last_version()
    version_number = last_version.version_number

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
        print_red("Warning: Please update your postgresql. "+ version_number + " is avaliable.")
    else:
        print_green("OK")
