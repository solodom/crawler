import re
from urllib import request,error


def crawl(url,page):
    """
    this function craw the images given the url and the page of the web

    args:
        page: int , the number of webpage you want to craw
        url； the start url of the webpage
    """
    # craw the source code of the webpage
    html_source=request.urlopen(url).read()
    # change the code to string
    html_sourcestr=str(html_source)
    # 选取要爬取得代码段
    pattern1='<div id="plist".+? <div class="page clearfix">'
    result1=re.compile(pattern1).findall(html_sourcestr)
    paragraph=result1[0]
    fh=open(r'D:\pythoncode\crawler\jingdongpic\image\1.txt','w')
    fh.write(paragraph)
    fh.close()
    # 在代码段中选取要爬取的图片链接,正则表达式中（）代表提取匹配字符
    pattern2='<img width="220" height="220" data-img="1" (.+?)>'
    imagelist=re.compile(pattern2).findall(paragraph)
    image_url_list=[]
    for image in imagelist:
        # find() 没找到返回-1
        if image.find('src')==-1:
            image_url=image.lstrip('data-lazy-img="').rstrip('"')
        else:
            image_url=image.lstrip('src="').rstrip('"')
        image_url_list.append(image_url)
    fh1=open(r'D:\pythoncode\crawler\jingdongpic\image\2.txt','w')
    for image in image_url_list:
        fh1.write(image+'\n')
    fh1.close()
    x=1
    for image in image_url_list:
        image_file='D:/pythoncode/crawler/jingdongpic/image/'+str(page)+str(x)+'.jpg'
        image_url='http:'+image
        try:
            request.urlretrieve(image_url,filename=image_file)
        except error.URLError as e :
            if hasattr(e,'code'):
                print(e.code)
                x+=1
            elif hasattr(e,'reason'):
                print(e.reason)
                x+=1
        x+=1
    print('there are {} pictures in page {}'.format(x-1,i))


for i in range (1,3):
    url='https://list.jd.com/list.html?cat=9987,653,655&page='+str(i)
    crawl(url,i)