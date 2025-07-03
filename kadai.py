import re

def url_host(url):
    result = re.fullmatch(r"https?://([^\s]+)")
    return result.group({1})


print( url_host('https://www.iniad.org/en/access') )