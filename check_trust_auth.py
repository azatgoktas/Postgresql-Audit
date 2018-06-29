from open_conf_file import lines

#- Check that only local users have "trust" authentication in pg_hba.conf.

for line in lines: #get line by line
    method = line[-6:].strip() #get last 6 character to check if it is trust or not
    if method == "trust":
        type = line[:5].strip() # is it local
        if type != "local" and type != "host":
            print("Error: There are some users have trust authentication in pg_hba.conf file")
