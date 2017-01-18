import requests
import webbrowser
import json
import urllib.request
import urllib.parse
import re

token = "Bearer " + input("OAuth Token: ") #BQDWxOubOFzx8fjeDi9E3Npt_fd9GiGXVgdiC3tS9LWHgajM3dRe2w3DjVVtjv0ZgHZAKt6zw2cD9PEBcLf-TFxtpOnb89THvPNMH-gbAO9Ho_8eSchxzO7JdaQ1Rg6eLBmzGIPjUp-5NM9Umpk62uKuAwPw7kSB0fb_B1uYdR4YkztfMsW5_OwXJukHyN0Cp2ztHR5V4_-5oFlHuTfPmyDcKZK8yreVwFUZuYB_VMPe_4pNhmu3PwlcePsKel9irRRsw41ly0mk1FcL3XFFHHXMHBHblYEu7hSccB8sqecdVZD9-w7PdcYS"

headers = {
        'Accept': 'application/json',
        'Authorization': token}
params = {
        'country': 'BR',
        'limit': '6',
        'offset' : '1'
        }

r = requests.get('https://api.spotify.com/v1/browse/new-releases', headers=headers, params = params)
print_json = r.json()

albums_name = []

for i in range(6):
    a = print_json['albums']['items'][i]['name']
    albums_name.append(a)

def youtube(s):
    query_string = urllib.parse.urlencode({"search_query" : s})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return("http://www.youtube.com/watch?v=" + search_results[0])

for i in albums_name:
    webbrowser.open(youtube(i))
