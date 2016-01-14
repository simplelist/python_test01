#coding:utf-8
import  cookielib,urllib2
filename='cookie.txt'
cookie=cookielib.MozillaCookieJar(filename)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
request=urllib2.Request("http://www.baidu.com")
response=opener.open(request)
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
cookie.save(ignore_discard=True,ignore_expires=True)