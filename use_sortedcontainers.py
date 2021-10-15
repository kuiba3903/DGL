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
# 删除元素，如果不存在，不报错
s.discard(7)
print(s)
s.discard(24)
print(s)
# 删除元素，如果不存在，会报错
# s.remove(24)
# print(s)
print("-------------")
# pop(index):删除并返回索引处的值,默认是-1即最后一个元素
print(s.pop())
print(s)
print(s.pop(1))
print(s)
print("-------------")
# bisect_left(value): 元素存在，返回索引值，不存在返回插入位置的索引;
print(s.bisect_left(1))
print(s.bisect_left(4))
print("-------------")
# count(value):统计出现的次数
print(s.count(3))
print(s.count(10))

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
sd.setdefault('c', 1)
sd.setdefault('d', 10)
sd.setdefault('e', 12)
sd['b']=100
print(sd)
print("-------------")
# pop(key,default): 弹出key对应的value,如果没有则返回default,如果没有给default则报错;
print(sd.pop('b'))
print(sd.pop('k',0))# 返回默认值
# 报错
# print(sd.pop('z'))
print(sd)
print("-------------")
# popitem(index=-1) 从排序的字典里删除并返回索引对,index默认是-1,即字典里最后一个
print(sd.popitem())
print(sd)
print("-------------")
# get 返回字典里key对应的value,否则返回默认值None,default值可以指定
print(sd.get('a',0))
print(sd.get('b'))
print(sd.get('b',0))
print("-------------")
# peekitem(index=-1):返回排序字典index处的索引对，不修改字典
print(sd.peekitem())
print(sd)
print("-------------")

"""
有序不重复集合：SortedSet
"""
ss = SortedSet()
# add(value):添加元素
ss.add(1)
ss.add(2)
ss.add(3)
ss.add(4)
ss.add(3)
print(ss)
print("-------------")
# discard(value):删除元素，不存在不报错
ss.discard(3)
print(ss)
ss.discard(9)
print(ss)
print("-------------")
# pop(index=-1):删除index处的值并返回,默认是最后一个
print(ss.pop(1))
print(ss)
