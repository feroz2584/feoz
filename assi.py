#part1 
#1
l =["Feroz", "Rahul", "Aman", "Ravi", "Kiran","Arjun", "Suresh", "Vijay", "Priya", "Neha"]
l.append("Anil")
l.insert(0, "Karthik")
l.remove("Rahul")
print(l)

#2
numbers=[12, 5, 8, 21, 5, 30, 8, 15]
max=numbers[0]
min=numbers[0]
total = 0
for i in numbers:
    if i > max:
        max = i
    if i < min:
        min= i
    total=total+i
average=total/len(numbers)
print("Maximum:", max)
print("Minimum:", min)
print("Total:", total)
print("Average:", average)

#3
numbers=[10, 20, 10, 30, 40, 20, 50]
u=[]
for i in numbers:
    if i not in u:
        u.append(i)
print(u)
#4
numbers = [10, 15, 22, 31, 44, 57, 60, 73]
even=[]
odd=[]
for i in numbers:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)
print("Even count:", len(even))
print("Odd numbers:", odd)
print("Odd count:", len(odd))
#5
marks = [78, 45, 92, 66, 35, 88, 55]
marks.sort()
print("Ascending:", marks)
marks.reverse()
print("Descending:", marks)
print("Top 3 marks:", marks[:3])

#sets - part 2
python_students={"rahul", "aman", "kiran", "neha", "priya"}
sql_students={"arjun", "suresh", "vijay", "neha", "priya"}
print(python_students & sql_students)
# 2
python_students={"rahul", "aman", "kiran", "neha", "priya"}
sql_students={"arjun", "suresh", "vijay", "neha", "priya"}
print(python_students-sql_students)
print(sql_students-python_students )

list=[10,20,30,20,10,40,50]
u=set(list)
print(u)
print(len(u))

s1={10,20,30,40,50}
s2={30,40,50,60,70}
print("union:",s1.union(s2))
print("Interesection:",s1.intersection(s2))
print("difference",s1.difference(s2))
print("symmetric Difference:",s1.symmetric_difference(s2))

emp_id={101,102,103,104,105}
user=int(input("enter id:"))
if user in emp_id:
    print("Employee ID found")
else:
    print("Employee ID not found")
    
#dictionaries - part 3
students={'name':'john','age':25,'course':'python','marks':86}
students['city']='hyd'
students['marks']=90
print(students.keys())



employees = { "Feroz": 45000, "Rahul": 55000, "Aman": 35000, "Ravi": 60000}
highest = 0
lowest =99999
for name, salary in employees.items():
    if salary > highest:
        highest = salary
        high_name = name
    if salary < lowest:
        lowest = salary
        lowest_name = name
print("Highest:", high_name, highest)
print("Lowest:", lowest_name, lowest)


sales = { "Monday": 12000,"Tuesday": 15000,"Wednesday": 9000,"Thursday": 18000,"Friday": 14000}
total = 0
highest = 0
for day, amount in sales.items():
    total = total + amount
    if amount > highest:
        highest = amount
        high_day = day
average = total / len(sales)
print("Total:", total)
print("Average:", average)
print("Highest day:", high_day)

names = ["Asha", "Ravi", "John"]
marks = [85, 72, 91]
student = {}
for i in range(len(names)):
    student[names[i]] = marks[i]
print(student)

salary = {"IT": [45000, 55000, 60000], "HR": [40000, 48000], "Sales": [35000, 50000, 65000]}
for department, salaries in salary.items():
    total = 0
    for s in salaries:
        total = total + s
    average = total / len(salaries)
    print(department)
    print("Total:", total)
    print("Average:", average)