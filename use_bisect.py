import bisect
# bisect 的函数如下：
# ['bisect', 'bisect_left', 'bisect_right', 'insort', 'insort_left', 'insort_right']
print([i for i in dir(bisect) if i.find("__")==-1])
