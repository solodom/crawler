from urllib import request
import re
from bs4 import BeautifulSoup


def getcontent(url):
    # 模拟浏览器
    headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')
    opener=request.build_opener()
    opener.addheaders=[headers]
    # 安装全局opener
    request.install_opener(opener)
    # 爬取回的源代码是二进制代码，需要字符串化
    data=request.urlopen(url).read().decode('utf-8')
    # 设置beautifulsoup对象，参数为文件与解析器
    soup=BeautifulSoup(data,'html.parser')
    # return a list of h2 tags 
    usertag_list=soup.find_all('h2')
    user_list=[]
    # .string return the according tag's contents
    for user in usertag_list:
        # string属性只能返回单节点的字符串，如果内容中含有<br/>,需要用get_text()
        user_str=user.string
        # 去点字符串前后的‘\n’,strip返回新字符串，字符串不能更改，所有字符串方法都要返回新的字符串
        user_str=user_str.strip('\n')
        user_list.append(user_str)
    # return a list of span tags with class attribute being 'content'
    contenttag_list=soup.find_all('div',class_='content') 
    content_list=[]
    for content in contenttag_list:
        # 内容中含有<br/>,不能用string属性，需要用get_text()
        # 用.来获取子节点
        content_str=content.span.get_text()
        content_str=content_str.strip('\n')
        content_list.append(content_str)
    for i in range(1,len(user_list)+1):
        print('用户{}{}发表的内容是:\n{}'.format(str(i),user_list[i-1],content_list[i-1]))


base_url='https://www.qiushibaike.com/text/page/'
for i in range (1,3):
    url=base_url+str(i)
    print('第{}页：'.format(str(i)))
    getcontent(url)

    
