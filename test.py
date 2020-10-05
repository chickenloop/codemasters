import hashlib
import sys
import requests

r = requests.get("http://index.hu")
print(r)

print (sys.version)
print (sys.executable)

test=hashlib.new("sha256","this string is hashed".encode())
print(test.hexdigest())