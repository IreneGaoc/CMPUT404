import requests

print(requests.__version__)


r=requests.get("http://www.google.com")
s=requests.get("https://raw.githubusercontent.com/IreneGaoc/CMPUT404Lab1H05/master/main.py")
#print(r)

#print(r.text)
print(s.text)