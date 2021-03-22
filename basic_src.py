from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
# 请求获取HTML资源
html = urlopen("http://www.baidu.com/")
# 解析html
obj = bf(html.read(),'html.parser')
# 提取logo图片
logo_pic_info = obj.find_all('img',class_="index-logo-src")
# 提取logo图片的链接
logo_url = "https:"+logo_pic_info[0]['src']
# 打印链接
print(logo_url)