#coding:utf-8
import  urllib2,re,pickle
__author__ = 'Administrator'
rege=r'<td class="redBalls">[\s\S]+?<em>(\d.+?)</em><em>(\d.+?)</em><em>(\d.+?)</em><em>(\d.+?)</em><em>(\d.+?)</em><em>(\d.+?)</em>'
url="http://baidu.lecai.com/lottery/draw/list/50?agentId=5555"
def getNum(color):
    html=urllib2.urlopen(url).read()
    reg=re.compile(color)
    nums=re.findall(reg,html)
    return nums
reds=getNum(rege)
all_reds=""
for redBall in reds:
    for ball in redBall:
        all_reds+= ball+" "
a=""
result=""
for i in range(1,37):
    if i<10:
        a="0"+str(i)
    else:
        a=str(i)
    result+=(str(a)+"\t"+ str(all_reds.count(a)))+"\n"
print result
f=open("balls.result","w+")
pickle.dump(result,f)
f.close()