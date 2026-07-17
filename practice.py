#a= input("enter 1st movie name:")
#b= input("enter 2nd movie name:")
#c= input("enter 3rd movie name:")
#movies=[a,b,c]
#print(movies)

"""movies=[]
movies.append(input("enter 1st movie name:"))
movies.append(input("enter 2nd movie name:"))
movies.append(input("enter 3rd movie name:"))
print(movies)"""

"""list=[1,2,3,1]
ch=list.copy()
ch.reverse()
if(ch==list):
    print("palindrome no")
else:
    print("non palindrome no")"""    

#tup=("c","d","a","a","b","a")
#print(tup.count("a"))

#list=["c","d","a","a","b","a"]
#list.sort()
#print(list)

#meaning={}
#meaning.update({"table":["a piece of furniture","lists of facts and fig"],"cat":"an animal"})
#print(meaning)

#subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
#print("the no. of classroom required is",len(subject))

"""dict={}
a=int(input("enter marks"))
dict.update({"chem":a})

b=int(input("enter marks"))
dict.update({"phy":b})

c=int(input("enter marks"))
dict.update({"maths":c})

print(dict)"""

"""i=1
while i<=100:
    print(i)
    i += 1"""

"""i=100
while i>=1:
    print(i)
    i -= 1"""

"""n=int(input("enter a no."))
i=1
while i<=10:
    print(n*i)
    i +=1"""

#list=[1,4,9,16,25,36,49,64,81,100]
#idx=0
#while idx<len(list):
    #print(list[idx])
    #idx +=1

"""tup=(1,4,9,16,25,36,49,64,81,100)
x=64
idx=0
while idx<len(tup):
    if(tup[idx]==x):
        print("found at index",idx)
    idx +=1"""

"""list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
 print(el)"""

"""list=[1,4,9,16,25,36,49,64,81,100,36]
x= 36
idx= 0
for el in list:
    if(el==x):
        print(idx)
    idx += 1"""

#for el in range(1,101):
    #print(el)  


#for el in range(100,0,-1):
    #print(el)

#n=int(input("enter no:"))
#for el in range(1,11):
   # print(n*el) 

"""n= 5
sum=0
for i in range(1,n+1):
    sum += i
 
print(sum)"""   


"""n= 5
fac=1
for i in range(1,n+1):
    fac *= i
 
print(fac)"""

"""def even_odd(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")


even_odd(9)"""

"""with open("practice.txt","w") as f:
    f.write("Hi Everyone\nwe are learning File I/O\nusing Java.\nI like Programming in Java")
f.close()"""

"""with open("practice.txt","r") as f:
    data=f.read()

new_data  = data.replace ("Java","Python")
print(new_data) 

f=open("practice.txt","w")
f.write(new_data)"""

"""def find_word():
    word="mlearning"
    with open("practice.txt","r") as f:
        data=f.read()
        if(word in data):
            print("found")
        else:
            print("not found") 

find_word()"""


"""fruites=["Mango","lichi","apple","banana","guava"]
flowers=["sunflower","rose","marigold","daisy"]
def list_len(list):
    print(len(list))

list_len(fruites)
list_len(flowers)"""    
   
"""def find_fact(n):
    fac=1
    for i in range(1,n+1):
        fac *= i
        print(fac)

find_fact(5)"""      


"""def converter_inr(n):
    inr_val = n*83
    print(inr_val)

converter_inr(2)"""


class student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hi",self.name,"your avg marks is",sum/3)   

s1 = student("moumi",[99,98,97])
s1.get_avg()             

