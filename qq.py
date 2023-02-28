import re
from http import client
import calendar
file = "folder1/folder2/file.ext"
regex = re.compile('\w+xt')

s = regex.findall(file)
s = "".join(s)
print(s)

connection = client.HTTPSConnection("www.google.com")
connection.request("GET", "/")
response = connection.getresponse()
print(response.status, response.reason)
connection.close()

print(dir(calendar))


calendar.prmonth(2027,2)
calendar.prmonth(1995,6)

calendar.prcal(2023)
