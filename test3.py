""" 
    列表（List）:   有序，连续内存空间，可修改
    元组（tuple）:  有序，连续内存空间，不可修改 
    字典（dict）:   无序，不连续内存空间，可修改（key-value）  
    集合（set）: 
"""
list1 = list("Hello")
print(list1)
tuple = ('Python','java','c++','Javascript')
list2 = list(tuple)
print(list2)

dict1 = {'a': 100, 'b': 150, 'c': 200}
list3 = list(dict1)
print(list3)

range1 = range(1,20)
list4 = list(range1)
print(list4)

l = ["lisa", "python", "java"]
l.append("ruby")
l.append(["c#","javascript"])   #list append的时候，如果添加的是list或者tuple，则会当做一个元素添加到list里面，list允许直接添加数字
l.append(1)
l.extend("1")
l.extend(("c#","javascript"))   #list extend的时候，是把整个list或者tuple拆开追加到list里面，extend不允许直接数字
print(l)

l.insert(2,"This is the 2 position")
print(l)

del l[4]
print(l)

l.append("Go")
print(l)
l.extend(["R","Matlab","Verilog"])
l.pop(10)
print(l)

a = 14
print(str(14))