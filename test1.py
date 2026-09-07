
#print 1 to 10
for i in range(1,11):
    print(i)
##even  numbers
for i in range(1,21):
    if i%2==0:
        print(i)
#sum of 1 to n
n=int(input("enter number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#multiplication table
n=int(input("enter number"))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i=i+1

#count vowels in a string
s="programming"
v=0
for i in s:
    if i in "aeiou":
        v=v+1
print(v)

#print squares
for i in range (1,11):
    print(i*i)

#divisible by 3 and 5
for i in range(1,51):
    if i %3==0 and  i % 5==0:
        print(i)
#sum of a list
n=[4,8,15,16,23,42]
sum=0
for i in n:
    sum =sum+i
print(sum)
#find the largest number in a list
n=[4,6,16,8,12]
l=0
for i in n:
    if i>l:
        l=i
print(l)

#reverse a string
s="hello"
s1=""
for  char in s:
    s1=char+s1
print(s1)

#10 to 1
i=10
while i>0:
    print(i)
    i-=1

# 1 to 10
i=0
while i<=10:
    print(i)
    i+=1

#count digits in a number
s=int(input("enter a number"))
c=0
while s>0:
    r=s%10
    c+=1
    s=s//10
print(c)

#reverse of a number
s=int(input("enter a number"))
rev=0
t=s
while s>0:
    r=s%10
    rev=rev*10+r
    s=s//10
print(rev)
#password retry
i=0
while i<3:
    password=input("enter a password: ")
    if password=="python123":
        print("Access Granted")
    else:
        print("Access Denied")
    i+=1
print("you have exceeded the limit of login attempts")
#multiples of 3
i = 3
while i<=30:
    print(i)
    i=i+3
#factorial of a number
n =int(input("Enter a number: "))
fact=1
i=1
while i<= n:
    fact=fact * i
    i=i + 1
print(fact)
#sum until zero
sum=0
n=int(input("enter a number"))
while n!=0:
    sum=sum+n
    n=int(input("enter a number"))
print(sum)

#secreet number
s=7
n=int(input("enter the number: "))
while n!=s:
    print("Try again")
    n= int(input("Guess the number: "))
print("Correct")
    
