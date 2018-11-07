import requests
import sys

url = sys.argv[1]
initial = "'"

print "Testing "+ url
first = requests.post(url+initial)

if "mysql" in first.text.lower():
    print "[+] Injectable MySQL detected"
elif "native client" in first.text.lower():
    print "[+] Injectable MSSQL detected"
elif "syntax error" in first.text.lower():
    print "[+] Injectable PostGRES detected"
elif "ORA" in first.text.lower():
    print "[+] Injectable Oracle detected"
else:
    print "[-] Not Injectable "
