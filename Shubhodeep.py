#!/usr/bin/env python
# coding: utf-8

# ### Answer 1
# 

# In[1]:


for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        print(i,end=",")


# ### Answer 2

# In[103]:


n=int(input("Enter value::"))
val=1
for i in range(1,n+1):
    val=val*i
print(val)


# ### Answer 3

# In[ ]:


dict={}
n=int(input("Enter value::"))
for i in range(1,n+1):
    dict[i]=i*i
print(dict)


# ### Answer 4

# In[ ]:


l=list(map(int, input("Enter multiple value: ").split(",")))
print(l,tuple(l))


# ### Answer 5

# In[ ]:





# ### Answer 6

# In[ ]:


import math
l=list(map(int, input("Enter multiple value: ").split(",")))
for i in l:
    q=round(math.sqrt((2*50*i)/30))
    print(q,end=",")


# ### Answer 7

# In[ ]:


row=int(input("enter row::"))
col=int(input("enter row::"))
res=[[row*col for col in range(col)] for row in range(row)]
print(res)


# ### Answer 8

# In[ ]:


l=list(map(str,input("enter words::").split(",")))
print(sorted(l))


# ### Answer 9

# In[ ]:


string=input("enter string")
print(string.upper())


# ### Answer 10

# In[ ]:


l=list(map(str,input("enter words::").split(" ")))
l=set(l)
for i in l:
    print(i,end=" ")


# ### Answer 11

# In[ ]:


def binaryToDecimal(n):
    return int(n,2)

l=list(map(int,input("enter::").split(",")))
l1=[]
for i in l:
    l1.append(str(i))
res=[]
for i in l1:
    res.append(binaryToDecimal(i))
for i in res:
    if i%5==0:
        print(i)


# ### Answer 12

# In[ ]:


l=[]
for i in range(1000,3001):
    k=str(i)
    c=len(k)
    count=0
    for i in k:
        if int(i)%2==0:
            count+=1
    if count==c:
        l.append(k)
print(l)


# ### Answer 13

# In[ ]:


n=input("enter::")
l=[]
digit=0
letter=0
for i in n:
    if i.isalpha():
        letter+=1
    elif i.isnumeric():
        digit+=1
print("digit::",digit)
print("letter::",letter)


# ### Answer 14

# In[ ]:


n=input("enter::")
upper=0
lower=0
for i in n:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("upper::",upper)
print("lower::",lower)


# ### Answer 15

# In[ ]:


n=int(input("enter number"))
l=[]
for i in range(1,5):
    l.append(int(str(n)*i))
print(sum(l))


# ### Answer16

# In[ ]:


l=list(map(int,input("enter::").split(",")))
for i in l:
    if i%2!=0:
        print(i*i,end=" ")


# ### Answer 17

# In[ ]:


l=list(map(str,input("Enter D for deposit and W for withdrawl and amount").split()))
alp=[]
dig=[]
sum=0
for i in l:
    if i.isalpha():
        alp.append(i)
    else:
        dig.append(i)
for i,j in zip(alp,dig):
    if i =="D":
        sum+=int(j)
    else:
        sum-=int(j)
print(sum)
        


# ### Answer 18

# In[ ]:


import re
l=list(map(str,input("Enter passwords::").split(",")))
count=0
for i in l:
    if re.search(r'[a-zA-Z0-9]',i) and len(i)>6 and len(i)<12:
        if "@" in i or "$" in i or "#" in i:
            print(i)
        


# ### Answer 19

# In[ ]:


from operator import itemgetter
list=[]
while True:
    inp=input("enter name: age: score= ")
    if inp:
        list.append(tuple(inp.split(',')))
    else:
        break
print(sorted(list, key=itemgetter(0,1,2)))


# ### Answer 20

# In[ ]:





# ### Answer 21

# In[19]:


l=[]
n=4
dis=[]
dir=[]
for i in range(n):
    k=input()
    l.append(k)
    k1=k.split(" ")
    dir.append(k1[0])
    dis.append(int(k1[1]))
m=max(dis[0],dis[1])
m0=min(dis[0],dis[1])
m1=max(dis[2],dis[3])
m2=min(dis[2],dis[3])
s=m+m1-m0-m2
print(s)


# ### Answer 22

# In[ ]:


n=input()
l=n.split()
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l2.append([i,l.count(i)])
l2=sorted(l2)
for i in l2:
    print(i)


# ### Answer 23

# In[20]:


import math
n=int(input())
print(math.sqrt(n))


# ### Answer 24

# In[23]:


print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


# ### Answer 25

# ### Answer 26

# In[27]:


def sum(a,b):
    return a+b
a,b=map(int,input().split())
print(sum(a,b))


# ### Answer 27

# In[29]:


def convert(n):
    print(str(n))
    print(type(str(n)))
n=int(input())
convert(n)


# ### Answer 28

# In[30]:


def sum(a,b):
    return int(a)+int(b)
a,b=map(str,input().split())
print(sum(a,b))


# ### Answer 29

# In[31]:


a,b=map(str,input().split())
print(a+b)


# ### Answer 30

# In[32]:


def compare(a,b):
    if len(a)>len(b):
        return a
    else:
        return b
    
a,b=map(str,input().split())
if len(a)==len(b):
    print(a,"\n",b)
else:
    print(compare(a,b))


# ### Answer 31

# In[35]:


dict={}

for i in range(1,21):
    dict[i]=i*i
print(dict)


# ### Answer 32

# In[40]:


import math
def ret():
    dict={}
    for i in range(1,21):
        dict[i]=math.sqrt(i)
    print(dict)
ret()


# ### Answer 33

# In[43]:


def ret(i):
    return i*i
l=[]
for i in range(1,21):
    l.append(ret(i))
print(l)


# ### Answer 34

# In[42]:


def ret(i):
    return i*i
count=0
for i in range(1,21):
    if count==5:
        break
    else:
        print(ret(i))
        count+=1


# ### Answer 35

# In[44]:


def ret(i):
    return i*i
count=0
for i in range(1,21):
    if count==5:
        break
    else:
        print(ret(i))
        count+=1


# ### Answer 36

# In[49]:


def ret(i):
    return i*i
count=0
l=[]
for i in range(1,21):
    l.append(ret(i))
print(l[5:])


# ### Answer 37

# In[50]:


def ret(i):
    return i*i
count=0
l=[]
for i in range(1,21):
    l.append(ret(i))
l1=tuple(l)
print(l1)


# ### Answer 38
# 

# In[51]:


def ret(i):
    return i*i
count=0
l=[]
for i in range(1,21):
    l.append(ret(i))
l1=tuple(l)
l=len(l1)
print(l1[:l//2])
print(l1[l//2:])


# ### Answer 39

# In[53]:


l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
print(tuple(l1))


# ### Answer 40
# 

# In[54]:


n=input()
if n=="Yes" or n=="YES" or n=="yes":
    print(n)
else:
    print("no")


# ### Answer 41
# 

# In[55]:


l= [1,2,3,4,5,6,7,8,9,10]
res=map(lambda x:x*x,l)
print(list(res))


# ### Answer 42
# 

# In[56]:


l= [1,2,3,4,5,6,7,8,9,10]
res=map(lambda x:x*x,l)
res1=filter(lambda x: x % 2 == 0, res)
print(list(res1))


# ### Answer 43
# 

# In[58]:


l= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
res1=filter(lambda x: x % 2 == 0, l)
print(list(res1))


# ### Answer 44
# 

# In[62]:


import math
l= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
res1=map(lambda x: math.sqrt(x), l)
print(list(res1))


# ### Answer 45
# 

# In[67]:


class America:
    def __init__(self,nationality):
        self.nationality=nationality
    @staticmethod
    def printNationality(nationality):
        return nationality
america=America("India")
print(america.printNationality("India"))
        


# ### Answer 46
# 
# 

# In[68]:


class America:
    def __init__(self,nationality):
        self.nationality=nationality
    @staticmethod
    def printNationality(nationality):
        return nationality
class NewYork(America):
    def __init__(self):
        America.__init__(self)
america=America("India")
print(america.printNationality("India"))


# ### Answer 47
# 

# In[72]:


class Circle:
    def __init__(self,radius):
        self.radius=radius
    def printarea(self,radius):
        return radius*radius
circle=Circle(20)
print(circle.printarea(20))


# ### Answer 48
# 

# In[73]:


class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def printarea(self,breadth,length):
        return length*breadth
rectangle=Rectangle(20,30)
print(rectangle.printarea(20,30))


# ### Answer 49
# 

# In[77]:


class Shape:
    def __init__(self,side):
        self.side=side
    def printarea(self,side):
        return side*side
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def printarea(self,side):
        return side*side
square=Square(30)
print(square.printarea(30))


# ### Answer 50

# In[99]:


a=[1,2]
try:
    print(a[2])
    raise RuntimeError
except RuntimeError:
    print("not possible")


# ### Answer 51
# 

# In[93]:


try:
    r=5/0
    print(r)
except:
    print("not possible")


# ### Answer 52

# ### Answer 53
# 

# In[101]:


n=input()
name=""
for i in n:
    if i!="@":
        name+=i
    else:
        break
print(name)


# ### Answer 54

# In[109]:


n=input()
name=""
x=n.split("@")
x1=x[1].split(".")
name=x1[0]   
    
    
print(name)


# ### Answer 55

# In[130]:


n=input("enter::")
l=[]
digit=0

for i in n:
    if i.isnumeric():
        l.append(i)
print(l)


# ### Answer 56

# In[132]:


print(u'Hello, world!')


# ### Answer 57

# In[136]:


s="hey you"
s.encode("UTF-8")


# ### Answer 58

# In[137]:


s="hey you"
s.encode("UTF-8")


# ### Answer 59

# In[139]:


num = int(input("Enter a number: "))
newnum = 0

for each in range(1,num+1):
    newnum = newnum+(each/(each+1))

print(round(newnum,2))


# ### Answer 60

# In[1]:


def fun(n):
    if n==0:
        return 0
    else:
        return fun(n-1)+100
n=int(input())
print(fun(n))


# ### Answer 61

# In[4]:


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(7))


# ### Answer 62

# In[5]:


def f(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1) + f(n-2)

no = int(input("Enter input: "))
for i in range(no+1):
    print(f(i),end=',')


# ### Answer 63

# In[6]:


no=int(input("enter a number"))
for i in range(no+1):
    if(i%2==0):
        print(i,end=',')


# ### Answer 64

# In[25]:


no=int(input("enter a number"))
for i in range(no+1):
    if(i%5==0 and i%7==0):
        print(i,end=',')


# ### Answer 65

# In[ ]:


l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    assert(i%2==0)


# ### Answer 66

# In[2]:


exp=input()
print(eval(exp))


# ### Answer 67

# In[6]:


l=[1,2,3,4,5,6,7,8,9]
if 2 in l:
    print("found")


# ### Answer 68

# In[10]:


import random
n = float(random.randint(10,100))
print(n)


# ### Answer 69

# In[8]:


import random
n = random.randint(5,95)
print(n)


# ### Answer 70

# In[11]:


l=[2,4,6,8,10]
print(random.choice(l))


# ### Answer 71

# In[12]:


l=[]
for i in range(10,151):
    if i%5==0 and i%7==0:
        l.append(i)
print(random.choice(l))


# ### Answer 72

# In[19]:


from random import sample
l = [] 
for i in range(100,201):
    if i%2==0:
        l.append(i)
print(sample(l,5))


# ### Answer 73

# In[20]:


from random import sample
l = [] 
for i in range(100,201):
    if i%2==0:
        l.append(i)
print(sample(l,5))


# ### Answer 74
# 

# In[21]:


from random import sample
l=[]
for i in range(1,1000):
    if i%5==0 and i%7==0:
        l.append(i)
print(sample(l,5))


# ### Answer 75
