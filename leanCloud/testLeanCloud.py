#coding:utf-8
import leancloud
from leancloud import Object
from gevent import monkey
from leancloud import Query
monkey.patch_all()
leancloud.init('9mDg7pW6a3OeJdtafnUvz5a5-gzGzoHsz', 'ca2bfiU3krn4j5WxeS3UEfYC')


class GameScore(Object):
    def is_cheated(self):
        # 可以像正常 Python 类一样定义方法
        return self.get('cheatMode')

    @property
    def score(self):
        # 可以使用property装饰器，方便获取属性
        return self.get('score')

    @score.setter
    def score(self, value):
        # 同样的，可以给对象的score增加setter
        return self.set('score', value)

'''
game_score = GameScore()
game_score.set('score', 222)  # or game_score.score = 42
game_score.set('cheatMode', True)
game_score.set('playerName', 'wwwww2w')
game_score.save()
'''
query = Query(GameScore)
game_score = query.get('569f7c667db2a200521e063a')
game_score.increment('score', 1)
game_score.save()

print game_score.get('playerName')