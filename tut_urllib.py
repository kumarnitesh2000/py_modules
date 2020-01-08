import urllib3,urllib
import urllib.error
from http.cookiejar import CookieJar
from urllib.request import urlopen,build_opener,HTTPCookieProcessor

'''https://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search'''

'''
response=urlopen('https://codeloop.org/')
print(response.status)
print(response.read()[:50])
try:
    urlopen("https://codeloop.org/page")
except urllib.error.HTTPError as e:
    print(e.url,e.reason,e.code)
response="https://codeloop.org/"
print(response.getheaders())

'''





'''
print(response.status)
print(response.getheaders(),"URL : ",response.url)
cookie_jar=CookieJar()
opener=build_opener(HTTPCookieProcessor(cookie_jar))
opener.open("https://google.com")
print(len(cookie_jar))

cookies=list(cookie_jar)
print(cookies)
'''

#provide : basic authentications , cookies , proxies provided by handlers and openers objects

import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    print("done")
    pass


'''
In the case of HTTP,
there are two extra things that
Request objects allow you to do:
 First, you can pass data to be sent to the server.
Second, you can pass extra information (“metadata”) about the data or the about request itself, to the server - this information is sent as HTTP “headers”.

'''

#DATA PART COME BRO --------------------
#The encoding is done using a function from the urllib.parse library. from bytes to ascii characters



import urllib.parse



