# -*- coding: utf-8 -*-
# 获取网页上的内容

import urllib2 #导入urllib2网络爬虫库
# file = urllib2.urlopen('http://helloworldbook.com/data/message.txt')
file = urllib2.urlopen('https://www.qq.com')
message = file.read() 
print message
