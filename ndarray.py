# _*_ coding=utf-8 _*


import numpy as np

"""ndarray创建与使用"""
# array()将列表转化为数组，可选择显示指定dtype
a = np.array([1,2,3])
print(a, type(a))

# arange() range的numpy版本，支持浮点数,size 数组的个数
b = np.arange(0,5,0.5) # 步长0.5
print(b, 'length:',b.size)

# linspace() 类似arange，第三个参数为数组长度
c = np.linspace(0,1,3)
print(c,'type:',c.dtype)

# zeros() 根据指定形状和dtype创建全0数组
d = np.zeros(10,dtype='int')
d1 = np.zeros(10)
print(d,d1)

# ones() 根据指定的形状和dtype创建全1数组
e = np.ones(5,dtype='int')
print(e)

# empty() 根据指定的形状和dtype创建全空数组（随机值）
f = np.empty(20)
print(f)

# eye() 根据指定边长和dtype创建单位矩阵
g = np.eye(5)   # 对角线全为1
print(g)
