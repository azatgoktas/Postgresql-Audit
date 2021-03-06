from open_conf_file import open_conf_file
from color_print import print_red, print_green

#- Check that only local users have "trust" authentication in pg_hba.conf.
class check_trust_auth():
    print("Checking if any user have trust authentication except local users")

    is_trusted = False

    global lines
    conf = open_conf_file()
    lines = conf.lines
    
    for line in lines: #get line by line
        method = line[-6:].strip() #get last 6 character to check if it is trust or not
        if method == "trust":
            type = line[:5].strip() # is it local
            if type != "local" and type[:4] != "host":
                is_trusted = True


    if is_trusted:
        print_red("Error: There are some users have trust authentication in pg_hba.conf file")
    else:
        print_green("OK")
