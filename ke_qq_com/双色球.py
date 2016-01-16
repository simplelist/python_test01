#coding:utf-8
import  urllib2,re,pickle
__author__ = 'Administrator'
rege=r'<td class="redBalls">[\s\S]+?<em>(\d.+?)</em><em>(\d.+?)</em><em>(\d.+?)</em><em>(\d.+?)</em><em>(\d.+?)</em><em>(\d.+?)</em>'
url="http://baidu.lecai.com/lottery/draw/list/50?agentId=5555"
#爬取并匹配所需数据,返回
def getNum(color):
    html=urllib2.urlopen(url).read()
    reg=re.compile(color)
    nums=re.findall(reg,html)
    return nums
reds=getNum(rege)
#将所有数据存在字符串中
all_reds=""
for redBall in reds:
    for ball in redBall:
        all_reds+= ball+" "
#统计红色球出现的频率
a=""
result=""
for i in range(1,34):#共有33个红色球
    if i<10:#如果小于10,前边补零
        a="0"+str(i)#将数字转为字符串
    else:
        a=str(i)
    result+=(str(a)+"\t"+ str(all_reds.count(a)))+"\n"#把结果收集到result中
print result#打印输出
#把结果保存到文件中
f=open("balls.result","w+")
pickle.dump(result,f)
f.close()