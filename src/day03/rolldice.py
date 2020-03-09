"""
掷骰子决定做什么事情

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""
from random import randint

face = randint(
    1
    ,
    1)
if face == 1:
    result = '唱首歌' + \
        '1'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(result)
print(999999999999999999999999999999999999*99999999999999999999999999999999999999)