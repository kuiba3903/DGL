from sortedcontainers import SortedDict,SortedList,SortedSet
import sortedcontainers
[print(i) for i in dir(sortedcontainers) if i.find("__")==-1]
s = SortedList([1,2,3])
# 添加元素
s.add(3)
s.add(7)
s.add(23)
print(s)
print("-------------")
s = SortedList([1,2,3])
# 删除元素，如果不存在，不报错
s.discard(7)
print(s)
# 删除元素，如果不存在，会报错
# s.remove(24)
# print(s)
print("-------------")
# pop(index):删除并返回索引处的值
print(s.pop(1))
print(s)
print("-------------")
# bisect_left(value): 返回索引值
print(s.bisect_left(1))
print("-------------")
# count(value):统计出现的次数
print(s.count(3))

print("-------------")
s.add(3)
# index(value): 返回第一个值处的索引
print(s.index(3))
print("-------------")
"""
    SortedDict:有序字典
"""
# setdefault(key,value): 添加键值对
sd = SortedDict()
sd.setdefault('a', 1)
sd.setdefault('b', 10)
sd.setdefault('b', 12)
print(sd)
print("-------------")
# pop(key,default): 弹出key对应的value,如果没有则返回default,如果没有给default则报错;
print(sd.pop('b'))
print(sd.pop('k',0))# 返回默认值
# 报错
# print(sd.pop('z'))
print("-------------")