from urllib import request
from urllib import error
"""
try:
    request.urlopen('http://abs.csdn.net')
except error.URLError as e:
    # print(e.code) URLerror 没有code
    print(e.reason)
"""

try:
    request.urlopen('http://abs.csdn.net')
except error.HTTPError as e:
    print(e.code) 
    print(e.reason)