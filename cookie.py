from urllib import request, parse
from http import cookiejar


url='http://bbs.chinaunix.net/member.php?mod=logging&action=login&action=login&loginsubmit=yes&loginhash=L768q'
# encode the post data
postdata=parse.urlencode({
    'username':'weisuen',
    'password':'aA123456'
}).encode('utf-8')

# request object
req=request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')
# 创建cookiejar对象
cjar=cookiejar.CookieJar()
# 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
opener=request.build_opener(request.HTTPCookieProcessor(cjar))
# 全局安装opener
request.install_opener(opener)
file=opener.open(req)
data=file.read()
hf=open(r'D:\pythoncode\crawler\cookie1.html','wb')
hf.write(data)
hf.close()
url2='http://bbs.chinaunix.net'
data2=request.urlopen(url2).read()
hf2=open(r'D:\pythoncode\crawler\cookie2.html','wb')
hf2.write(data2)
hf.close()
