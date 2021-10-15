import bisect
# bisect 的函数如下：
# ['bisect', 'bisect_left', 'bisect_right', 'insort', 'insort_left', 'insort_right']
[print(i) for i in dir(bisect) if i.find("__")==-1]
a = [1,2,3,5,7,9,20,44,55,60]
# bisect 与 bisect_right 的用法相同
# 作用: 查找该数值将会插入的位置并返回，而不会插入。如果x存在a中则返回x右边的位置
print(bisect.bisect_right(a,3))
print(bisect.bisect_right(a,4))
print("--------------")
# bisect_left 作用：
# 查找该数值将会插入的位置并返回，而不会插入。如果x存在在a中则返回x左边的位置
print(bisect.bisect_left(a,3))
print(bisect.bisect_left(a,4))
print("--------------")


# insort 与 insort_right 的用法相同
# 作用：在列表a中插入元素x，并在排序后保持排序。如果x已经在a中，把它插入右x的右边。
bisect.insort(a,3.0)
print(a)
bisect.insort(a,4)
print(a)
print("--------------")

# insort_left 作用：
# 在列表a中插入元素x，并在排序后保持排序。如果x已经在a中，把它插入右x的左边。
bisect.insort_left(a,2.0)
print(a)
bisect.insort_left(a,8)
print(a)