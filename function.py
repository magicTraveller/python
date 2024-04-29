# -*- coding=utf-8 -*-

def data_of_square(side=2):# 计算周长和面积的函数 如果不输入参数就默认side=2 即默认参数   默认参数只能在必需参数的后面    def可以用来定义函数、变量和类
    if not isinstance(side, int) or not isinstance(side, float):   #由于py没有设定数据类型 如果是字符串内计算会出错 所以要先判断是哪种数据类型
        C = side *4
        S = side * side
        return C, S

zc, mj = data_of_square(16)#其实返回的是tuple但是可以分开接受



def average(*args,**kwargs):#可变参数args会被当成tuple  **kwargs可变关键字参数类似dict  求平均值
    sum = 0
    if len(args) == 0:#因为可能是空所以要加个判断
        return sum
    for item in args:
        sum += item
    avg = sum / len(args)
print(kwargs['names'],'三人的年龄分别是',kwargs.get('age'))#两种获取可变关键字参数的方法
    return avg

print('三人的平均分是',average(67,47,95,names = ['Alice', 'Bob', 'Candy'],age = [16, 15,17]))



#函数栈的大小不是无限 递归用的太多会栈溢出  大概递归10000就溢出了
