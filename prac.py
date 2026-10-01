"""
text = "PYTHONPROGRAMMING"
print(text[0:6])
print(text[-7:])
print(text[0::2])
print(text[1::3])
print(text[::-1])
print(text[::-2])

name="Feroz"
age=25
height=5.8
print(name, age,height)

a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

data = "PYTHONPROGRAMMING"
print(data[6:-4])

text = "  python programming  "
sp=text.strip()
print(text.strip())
print(sp.upper())
print(sp.replace("python","java"))

word = "PROGRAMMING"
print(len(word))
print(word[0])
print(word[-1])
print(word[::-1])


text = "python programming"
print(text.title())
print(text.upper())
print(text.lower())
print(text.count("p"))

data = "PYTHONPROGRAMMING"
print(data[0:6].upper())
print(data[6:-4].upper())

n = [10, 20, 30, 40, 50]
print(n[0])
print(n[-1])
print(n[::-1])
print(n[1:4])


n= [10, 20, 30]
n.append(40)
print(n)
n.insert(0,5)
print(n)
n.remove(20)
print(n)
n.sort(reverse=True)
print(n)
"""
"""
n = [10, 20, 10, 30, 10, 40]
print(n.count(10))
print(n.index(30))
n.append(50)
print(n)
n.pop()
print(n)

n=[5,2,8,1,9,3]
print(max(n))
print(min(n))
n.sort()
print(n)
n.sort(reverse=True)
print(n)

a = [10, 20, 30]
b = [40, 50, 60]
a.extend(b)
print(a)

t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-1])
print(t[1:4])
print(t[::-1])

numbers=(10,20,30)
print(numbers)
a,b,c=numbers
print(a,b,c)
"""
"""
t = (10, 20, 10, 30, 10, 40)
print(t.count(10))
print(t.index(30))

t = (10, 20, 30, 40, 50)
tuple=(50,40,30,20,10)
print(tuple)

n = [10, 20, 10, 30, 20, 40, 30]
print(set(n))

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b))
print(a.intersection(b))

print(a.difference(b))

print(b.difference(a))


print(a.difference(b))



s = {10, 20, 30}
s.add(40)
print(s)
s.add(50,60)
print(s)
"""
# Perfect Number

num = int(input("Enter a number: "))

total = 0
i = 1

while i < num:
    if num % i == 0:
        total = total + i
    i = i + 1

if total == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")



