print(1)
print("Hello World!")

a=1
b="Hello World"
print(a,b)

print("Duan""Yixuan")
print("Duan","Yixuan")

print("www","baidu","com",sep=".")

num=19
print(num)

str="Duan YiYuan"
print(str)

list = [1,2,'a']
print(list)

tuple = (1,2,"a")
print(tuple)

dict = {"a":1, 'b':2}
print(dict)

s="Duan Yixuan"
x=len(s)
print("The length of %s is %d" % (s,x)) #与C语言区别在于，Python中格式控制符和换行说明符用%分分隔，C语言用逗号

PI=3.1415926
print("%10.3f" % PI)
print("PI=%*.3f" % (3,PI))
print("PI=%+ 10.3f" % PI)
""" 
    print格式归纳：
    %s 字符串采用str()的显示
    %r 字符串(repr())的显示
    %c 单个字符
    %b 二进制整数
    %d 十进制整数
    %i 十进制整数
    %o 八进制整数
    %x 十六进制整数
    %e 指数（基底写e）
    %E 指数（基底写E）
    %f,%F 浮点数
    %g 指数(e)或浮点数(根据显示长度)
    %G 指数(E)或浮点数(根据显示长度)
    %% 字符%    
"""
for x in range(0,5):
    print(x)
