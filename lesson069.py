import sys
li = []
print(sys.getsizeof(li))
li = ['a']
print(sys.getsizeof(li))

li = ['a', 'b', 'c', 'd']

print(li[2])
print(sys.getsizeof(li))
li.append('e')
print(li)
print(sys.getsizeof(li))
li.pop()
print(li)
li.pop()
print(li)
li.insert(0,'x')
print(li)
li.insert(2,'alien')
print(li)
