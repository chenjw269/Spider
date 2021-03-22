from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
# 请求获取HTML资源
html = urlopen("http://www.baidu.com/")
# 解析html
obj = bf(html.read(),'html.parser')
# 使用find_all函数获取所有图片
pic_info = obj.find_all('img')
for i in pic_info:
    print(i)