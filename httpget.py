# 利用get请求获取相应网页，并以html形式存储
from urllib import request
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd='
keyword='你好'
# 利用request.quote对中文进行编码
keyword_code=request.quote(keyword)
url_all=url+keyword_code
# 设置Request对象
reg=request.Request(url_all)
# 通过Request get内容，urlopen返回file-like object
data=request.urlopen(reg).read()
fhandle=open(r'D:/pythoncode/crawler/1.html','wb')
fhandle.write(data)
fhandle.close()