l=[1,2,10,20,30,"tops",1.1,1,2,2.2,True,"python"]

print(l)
print(len(l))
l.append(100)
print(l)
# l.clear()
# print(l)
l1=l.copy()
print(l1)
l1.append(300)
print(l1)
print(l)
l2=l
l2.append(200)
print(l2)
print(l)
print(l.count(1))
l3=[101,102,103]
l.extend(l3)
print(l)
print(len(l))
print(l.index(10))
print(l.index(1,8))
l.insert(15,14)
print(l)
l.pop()
print(l)
l.pop(10)
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)