def sum1(a,b):
    c=a+b
    return c
a=0
b=0
list =[]
for i in range(100):
    list.append(i+1)
for i in list:
    if i%3==0:
        a=a+i
    if i%7==0:
        b=b+i
print(list)
print(a)
print(b)
print(sum1(a,b))


