# -*- coding: utf-8 -*-
#随机猜数字小游戏

import random #导入random随机模块
secret = random.randint(1, 99)    #设定一个secret变量，值为从1-99随机的一个数。 
guess = 0
tries = 0
print "哈哈哈! 我是恐怖海盗罗伯茨，我有一个秘密!"
print "这个数字是1到99。我会让你尝试6次。 "

#可以猜6次
while guess != secret and tries < 6:                
    guess = input("你猜这个数字是? ")  
    if guess < secret:
        print "低啦,再高点儿!"
    elif guess > secret:
        print "高啦,再低点儿!"

    tries = tries + 1            # 猜的次数递增              

#最终显示结果
if guess == secret:                           \
    print "wo~ 你猜到了！你猜到了我的私密!"
else:
    print "次数用尽! 希望你下次能猜得更准，兄弟!"
    print "这次的私密数其实为：", secret
