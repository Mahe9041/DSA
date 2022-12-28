>>> str="svec"
>>> str
'svec'
>>> l=[]
>>> l.append(str)
>>> l
['svec']
>>> l.pop()
'svec'
>>> for i in range (len(str)):
...     l.append(str[i])
...
>>> l
['s', 'v', 'e', 'c']
>>> for i in range (len(str)):
...     l.pop()
...
'c'
'e'
'v'
's'