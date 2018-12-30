from urllib import request,parse

url='http://www.iqianyue.com/mypost/'

#Convert a mapping object or a sequence of two-element tuples, which may contain str or bytes objects, 
# to a percent-encoded ASCII text string. If the resultant string is to be used as a data for
# POST operation with the urlopen() function, then it should be encoded to bytes, otherwise it would
# result in a TypeError.
postdata=parse.urlencode({'name':'ceo@iqianyue.com','password':'aA123456'}).encode('utf-8')

# 构建带有postdata的Request 对象
reg=request.Request(url,postdata)

# 为Request添加浏览器模拟
reg.add_header( 'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')

data=request.urlopen(reg).read()
fh=open(r'D:\pythoncode\crawler\2.html','wb')
fh.write(data)
fh.close()

