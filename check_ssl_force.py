from open_conf_file import lines
from color_print import print_red, print_green

#Check that pg_hba.conf forces remote connections to use SSL

print("Checking if ssl is forced")
is_ssl_forced = True

for line in lines: #get line by line
    method = line[:7].strip() #get last 6 character to check if it is trust or not
    if method != "hostssl":
        is_ssl_forced = False

if is_ssl_forced :
    print_red("Error: SSL is not forced")
else:
    print_green("OK")
