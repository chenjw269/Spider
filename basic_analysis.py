from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
# 请求获取html资源
html = urlopen("http://www.baidu.com/")
# 解析html
obj = bf(html.read(),'html.parser')
# 从标签head、title里提取标题
title = obj.head.title
print(title)