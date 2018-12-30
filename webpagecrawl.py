from urllib import request


url=input('URL:')
file_name=input('Filename:')
page_file=request.urlretrieve(url,filename=file_name)