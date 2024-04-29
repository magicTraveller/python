
#在开头加这个可以避免 SyntaxError: Non-ASCII character '\xe7' in file ..   这个错误
# -*- coding=utf-8 -*-


#有序容器：列表list[]、元组tuple()
#无序容器：字典dict{}（所以在需要有序的dict时要用Ordereddict）、集合set{}和list的不同是元素不重复 所以set通常被用于当dict的key

#a = (1) 会被识别为数字1 就像改变计算优先级一样
a=(1,)#所以这样才被识别为一个元组，tuple可以转变成list 而且tuple里list里的元素可以改，但是tuple内元素不可变所以代码更安全,能用tuple代替list就尽量用tuple,比如作为字典中的键key
newA1=list(a+(2,'ds',1,))#但是可以创建新的tuple
newA=list(newA1)#tuple转换list


#newA.count(1)统计1的出现次数 newA.index('ds')ds第一次出现的索引不存在时会报错   newA.sort()  从小到大排序   len()可以得到元素数量
#另外元组的存储空间要比列表的少16字节访问和处理速度快    dict的查找速度快 

#s1.issubset(s2)判断s2是s1的子集   issuperset判断的是超集  isdisjoint是判断是否有重合元素


L = ["Bob",75, 'Alice', 92,'Tom',59,'Mary',68, True]#计算平均值
sum = 0.0
i=0
for x in L:  #通过for循环访问列表每一个元素的方式，我们称为迭代
    i = i + 1
    if i % 2 == 0:
        continue #continue继续循环 break跳出
    sum = sum + x
print(sum/4);
# 或者
i=0
while i<7:
	i+=1
	if i % 2 != 0:
        	continue #continue继续循环 break跳出
	sum+=L[i]
print(sum / 4)
#没有缩进会报错 混用空格和tab也报错



names = ['Alice', 'Bob', 'David', 'Ellena']
names.append("Fried")#append()将元素添加到list的尾部   集合set用的是add()   update()可以批量添加    names.remove('Bob') 不存在的会报错   discard()不会报错
names.insert(2, 'Candy')#插到第三位
names.pop(-6)#负数是倒序从-1开始   没有索引就删最后一个    dict也可以用pop
print(names)




d = {
    'Alice': 45,
    'Bob': 60,
    'Candy': 75,
    'key': 'value',
}
#调用的dict的key不存在时   会报错 所以使用自带的get更安全
if 'Alice' in d:#还可以这样先判断是否存在这个key   items()会返回包含key和value的所有的元素   如： for key, value in d.items()   类似的还有values()和keys()函数   clear()可以清空

