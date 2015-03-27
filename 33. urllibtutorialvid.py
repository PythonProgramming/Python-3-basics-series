
import urllib.request
import urllib.parse

#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())
'''
url = 'http://pythonprogramming.net'
values = {'s':'basic',
          'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))


try:
    url = 'https://www.google.com/search?q=test'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))

















