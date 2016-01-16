#coding:utf-8
__author__ = 'Administrator'

import urllib2
import re

class Baiduieba:
    def __init__(self,baseUrl,SeeLZ):
        self.baseURL=baseUrl
        self.seeLZ='?see_lz='+str(SeeLZ)

    def getPage(self,pageNum):
        try:
            url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError,e:
            if(hasattr(e,'reason')):
                print u"链接百度贴吧失败,原因"+e.reason
                return  None

baseURL='http://tieba.baidu.com/p/4305478882'
bdtb=Baiduieba(baseURL,1)
bdtb.getPage(1)

