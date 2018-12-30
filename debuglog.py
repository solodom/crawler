#  在程序运行的过程中边运行边打印日志


from urllib import request
# 使用HTTPHandler()和HTTPSHandler() 将debuglevel 设置为1
httphd=request.HTTPHandler(debuglevel=1)
httpshd=request.HTTPSHandler(debuglevel=1)
own_opener=request.build_opener(httphd,httpshd)
request.install_opener(own_opener)
data=request.urlopen('http://edu.51cto.com')
