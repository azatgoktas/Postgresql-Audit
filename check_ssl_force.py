from open_conf_file import open_conf_file
from color_print import print_red, print_green

#Check that pg_hba.conf forces remote connections to use SSL
class check_ssl_force():

    print("Checking if ssl is forced")

    global lines
    is_ssl_forced = True
    conf = open_conf_file()
    lines = conf.lines

    for line in lines: #get line by line
        method = line[:7].strip() #get last 6 character to check if it is trust or not
        if method != "hostssl":
            is_ssl_forced = False

    if is_ssl_forced :
        print_red("Error: SSL is not forced")
    else:
        print_green("OK")
