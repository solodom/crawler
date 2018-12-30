from urllib import request


def use_proxy(proxy_adrr,url):
    """
    this function use a proxy to open a webpage

    args:
        proxy_adrr: string, proxy address
        url: string, url to open 

    return:
        data: the data of the webpage
    """
    # 设置一个ProxyHandler对象
    proxy=request.ProxyHandler({'http':proxy_adrr})
    # 建立一个含有ProxyHandler和HTTPHandler的opener
    own_opener=request.build_opener(proxy,request.HTTPHandler)
    # 安装全局opener
    request.install_opener(own_opener)
    data=request.urlopen(url).read().decode('utf-8')
    return data


proxy_adrr="183.47.40.35:8088"  # 找验证时间较短的代理ip，成功率比较高
url='http://www.baidu.com'
data=use_proxy(proxy_adrr,url)
print(len(data))