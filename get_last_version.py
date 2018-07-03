# We need to check last version of postgres
#There is no api that we can get the last release version number
#we need to go official website than cut version text
#this module may not work when website updated

import urllib.request

class get_last_version():

    request = urllib.request.urlopen("https://www.postgresql.org")
    content = request.read() #all html code

    below_latest_relase = content.decode().split("<h2>Latest Releases</h2>",1)
    above_notes = below_latest_relase[1].split("Notes</a></li>",1)

    after_li_tag = above_notes[0].split("""<li class=""><b>""",1)
    before_b_tag = after_li_tag[1].split("</b>",1)


    version_number = before_b_tag[0] #version number
