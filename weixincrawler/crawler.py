from urllib import request
import urllib.error
import time
from bs4 import BeautifulSoup
import re

def get_data(url):
    try:
        proxy_addr='125.123.140.200:9999'
        #设置含有ProxyHandler和HTTPHandler的opener
        proxy=request.ProxyHandler({'http':proxy_addr})
        opener=request.build_opener(proxy,request.HTTPHandler)
        # 模拟浏览器
        headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')
        opener.addheaders=[headers]
        #将opener设置为全局opener
        request.install_opener(opener)
        data=request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,'reason'):
            print(e.reason)    
        time.sleep(10)
    except Exception as e:
        print('exception:'+str(e))
        time.sleep(1)


def get_urls(url):
    try:
        data=get_data(url)
        # beautifulsoup object
        soup=BeautifulSoup(data,'html.parser')
        # <h3> node
        url_list=soup.find_all('h3')
        urls=[]
        for content in url_list:
            # son node <a> of <h3>,and get the 'href' atrribute
            url=content.a['href']
            urls.append(url)
        return urls
    except urllib.error.URLError as e:
        if hasattr(e,'reason'):
            print(e.reason)    
        time.sleep(10)
    except Exception as e:
        print('exception:'+str(e))
        time.sleep(1)


def local_store(url,i,j):
    try:
        print('爬取第{}页的第{}篇文章'.format(i,j))
        html_data=get_data(url)
        soup=BeautifulSoup(html_data,'html.parser')
        # title name
        title_name=soup.find('h2').string.strip()
        #去除title中的\/?<>"符号
        #re.sub(pattern,substr,string)
        title_name=re.sub('<>"\?\\\/\|:\*',' ',title_name)
        local_file=open('D:/pythoncode/crawler/weixincrawler/'+title_name+'.html','wb')
        local_file.write(html_data.encode('utf-8'))
    except AttributeError as e:
        original_urltool=soup.find_all('div',class_='original_panel_tool')
        original_url=original_urltool.a['href']
        original_data=get_data(original_url)
        soup=BeautifulSoup(original_data,'html.parser')
        # title name
        title_name=soup.find('h2').string.strip()
        #去除title中的\/?<>"符号
        #re.sub(pattern,substr,string)
        title_name=re.sub('<>"\?\\\/\|:\*',' ',title_name)
        local_file=open('D:/pythoncode/crawler/weixincrawler/'+title_name+'.html','wb')
        local_file.write(html_data.encode('utf-8'))
    except urllib.error.URLError as e:
        if hasattr(e,'reason'):
            print(e.reason)    
        time.sleep(10)
    except Exception as e:
        print('exception:'+str(e))
        time.sleep(1)
    


page_num=int(input('please input the number of pages you want to crawl:'))
try:
    for i in range (1,page_num+1):
        key='物联网'
        # make the string suitable for http addrress
        key_code=request.quote(key)
        url='https://weixin.sogou.com/weixin?type=2&query='+key_code+'&page='+str(i)
        urls=get_urls(url)
        j=1
        for url in urls:
            local_store(url,i,j)
            j+=1
except urllib.error.URLError as e:
    if hasattr(e,'reason'):
        print(e.reason)    
    time.sleep(10)
except Exception as e:
    print('exception:'+str(e))
    time.sleep(1)