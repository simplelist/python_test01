#coding:utf-8
__author__ = 'Administrator'
import threading
import socket,re

routers=[]
lock=threading.Lock()

def search_routers():
    local_ips=socket.gethostbyname_ex(socket.gethostname())[2]
    all_threads=[]
    for ip in local_ips:
        for i in xrange(1,255):
            array=ip.split(".")
            array[3]=str(i)
            # print array
            new_ip='.'.join(array)#把内容转换成IP
            t=threading.Thread(target=check_ip,args=(new_ip,))
            t.start()
            all_threads.append(t)
    for t in all_threads:
        t.join()

def check_ip(new_ip):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    PORT=135
    result=s.connect_ex((new_ip,PORT))#跟主机地址的80端口建立链接
    s.close()#关闭链接
    if result==0:#
        lock.acquire()#获取锁
        print new_ip.ljust(15),'port %s is open'%PORT
        lock.release()#释放锁
def getTitle(self):
    page=self.getPage(1)
    pattern=re
print 'searching for routers ,please waiting....'
search_routers()


