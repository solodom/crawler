from urllib import request
import re


def getlink(url):
    # 模拟浏览器
    headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')
    opener=request.build_opener()
    opener.addheaders=[headers]
    # 将opener安装为全局
    request.install_opener(opener)
    file=request.urlopen(url)
    data=str(file.read())
    # 建立链接正则表达式
    pattern='(https?://[^\s)";]+\.(\w|/)*)'
    link=re.compile(pattern).findall(data)
    # 去掉重复元素
    link_list=list(set(link))
    return link_list


url='https://blog.csdn.net/'
link_list=getlink(url)
for link in link_list:
    print(link[0])