>>> a = 10
>>> print(a)
10
>>> str=''
>>> str='hello world'
>>> print(str)
hello world
>>> l=[]
>>> l.append(0)
>>> print  
<built-in function print>
>>> print(l)
[0]
>>> l.append(1) 
>>> l.append(2) 
>>> l.append(3) 
>>> print(l)
[0, 1, 2, 3]
>>> l.pop()
3
>>> print(l)
[0, 1, 2]
>>> pop(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> l.pop(1)
1
>>> l.insert(1,2) 
>>> l
[0, 2, 2]
>>> l.insert(1,3) 
>>> l
[0, 3, 2, 2]
>>> l.remove()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.remove() takes exactly one argument (0 given)
>>> l.remove(2)
>>> l
[0, 3, 2]
>>>
