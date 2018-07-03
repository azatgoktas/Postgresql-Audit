import configparser
import sys
from pathlib import Path

class open_conf_file():
    #root directory
    path = Path(sys.executable)
    root_or_drive = path.root or path.drive #get root directory
    configFilePath =  root_or_drive + 'usr/local/var/postgres/pg_hba.conf' #reading pg_hba.conf file
    with open(configFilePath,'r') as conf: #safe way
        file = conf.readlines()
    lines = []
    for line in file:
        if line[0] != '#' and line[0] != "\n":
            lines.append(line)
            
