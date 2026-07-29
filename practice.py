#3fav movie using list

#a= input("enter 1st movie name:")
#b= input("enter 2nd movie name:")
#c= input("enter 3rd movie name:")
#movies=[a,b,c]
#print(movies)

#3fav movies using append function in list

"""movies=[]
movies.append(input("enter 1st movie name:"))
movies.append(input("enter 2nd movie name:"))
movies.append(input("enter 3rd movie name:"))
print(movies)"""

#palindrome no

"""list=[1,2,3,1]
ch=list.copy()
ch.reverse()
if(ch==list):
    print("palindrome no")
else:
    print("non palindrome no")"""    

#count grade A student

#tup=("c","d","a","a","b","a")
#print(tup.count("a"))

#sort from A to D

#list=["c","d","a","a","b","a"]
#list.sort()
#print(list)

#store following word meaning

#meaning={}
#meaning.update({"table":["a piece of furniture","lists of facts and fig"],"cat":"an animal"})
#print(meaning)

#COUNT NO OF CLASSROOM REQUIRED FOR EACH SUBJECT

#subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
#print("the no. of classroom required is",len(subject))

#ENTER MARKS OF 3 SUBJECT IN DICT

"""dict={}
a=int(input("enter marks"))
dict.update({"chem":a})

b=int(input("enter marks"))
dict.update({"phy":b})

c=int(input("enter marks"))
dict.update({"maths":c})

print(dict)"""

#WHILE LOOP:-
#PRINT NO FROM 1 TO 100

"""i=1
while i<=100:
    print(i)
    i += 1"""

#PRINT NO FROM 100 TO 1

"""i=100
while i>=1:
    print(i)
    i -= 1"""

#MULTIPLICATION OF NO. n

"""n=int(input("enter a no."))
i=1
while i<=10:
    print(n*i)
    i +=1"""

#PRINT THE GIVEN LIST USING WHILE LOOP

#list=[1,4,9,16,25,36,49,64,81,100]
#idx=0
#while idx<len(list):
    #print(list[idx])
    #idx +=1

#SEARCH FOR A NO. n IN A TUPLE

"""tup=(1,4,9,16,25,36,49,64,81,100)
x=64
idx=0
while idx<len(tup):
    if(tup[idx]==x):
        print("found at index",idx)
    idx +=1"""

#FOR LOOP:-
#PRINT THE ELEMENT USING FOR LOOP

"""list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
 print(el)"""

#SEARCH FOR A NO n 

"""list=[1,4,9,16,25,36,49,64,81,100,36]
x= 36
idx= 0
for el in list:
    if(el==x):
        print(idx)
    idx += 1"""

#PRINT 1 TO 100

#for el in range(1,101):
    #print(el)  

#PRINT FROM 100 TO 1

#for el in range(100,0,-1):
    #print(el)

#MULTIPLE OF N

#n=int(input("enter no:"))
#for el in range(1,11):
   # print(n*el) 

#SUM OF FIRST n NO.

"""n= 5
sum=0
for i in range(1,n+1):
    sum += i
 
print(sum)"""   

#FACTORIAL OF FIRST n NO.

"""n= 5
fac=1
for i in range(1,n+1):
    fac *= i
 
print(fac)"""

#FUNCTIONS:-
#EVEN ODD USING FUNCTIONS

"""def even_odd(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")


even_odd(9)"""

#LENGTH OF A LIST UDING FUNCTION

"""fruites=["Mango","lichi","apple","banana","guava"]
flowers=["sunflower","rose","marigold","daisy"]
def list_len(list):
    print(len(list))

list_len(fruites)
list_len(flowers)"""    

#FACTORIAL USING FUNCTION
#  
"""def find_fact(n):
    fac=1
    for i in range(1,n+1):
        fac *= i
        print(fac)

find_fact(5)"""      

#CONVERT USD TO INR

"""def converter_inr(n):
    inr_val = n*83
    print(inr_val)

converter_inr(2)"""

#FILE I/0:-
#CREATE A NEW FILE
"""with open("practice.txt","w") as f:
    f.write("Hi Everyone\nwe are learning File I/O\nusing Java.\nI like Programming in Java")
f.close()

with open("practice.txt","r") as f:
    data=f.read()"""

#REPLACE JAVA WITH PYTHON

"""new_data  = data.replace ("Java","Python")
print(new_data) 

f=open("practice.txt","w")
f.write(new_data)"""

#SEARCH IF WORD "LEARNING"EXIST OR NOT

"""def find_word():
    word="mlearning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(word in data):
            print("found")
        else:
            print("not found") 

find_word()"""

#OOPs:-
# STUDENT NAME AND MARKS OF 3 SUBJECT AND FIND THE AVERAGE

#class student:
    #def __init__(self,name,marks):
        #self.name= name
        #self.marks = marks

    #def get_avg(self):
        #sum = 0
        #for i in self.marks:
           # sum += i
       # print("hi",self.name,"your avg marks is",sum/3)   

#s1 = student("moumi",[99,98,97])
#s1.get_avg()

#BANKING SYSTEM

"""class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    
    def debit(self,amount):
        self.balance -= amount
        print("rs", amount , "is debited from your account")
        print("the total amount is ", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("rs", amount , "is credited from your account")
        print("the total amount is ", self.get_balance()) 

    def get_balance(self):
        return self.balance       

acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(2000)"""

#finding area and perimeter of a circle using oops

"""class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*self.radius**2
    
    def perimeter(self):
        return 2*(22/7)*self.radius
    

cir1=Circle(14)
print(cir1.area())
print(cir1.perimeter())"""

#INHERITANCE

"""class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showdetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("Salary =", self.salary)

class engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT",75000)

emp1=engineer("moumi",23)
emp1.showdetails()"""

#using a dunder function __gt__()

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price > ord2.price


ord1=Order("brownie",150)
ord2=Order("cake",70)   

print(ord1>ord2)
        

