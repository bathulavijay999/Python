# task1.
a=6
b=4
print("before swaping",a,b)
temp=a
a=b
b=temp
print("after swaping",a,b)

#task2
# c=input()
# d=int(input())
# e=float(input())
# print("type is ",type(c))
# print("type is ",type(d))
# print("type is ",type(e))
 
 #3
f=23
g=6
print("addtion",f+g)
print("subtraction",f-g)
print("multiplication",f*g)
print("division",f/g)
print("floar division",f//g)
print("remainder",f%g)
print("double multiplie",f**g)

#4
# salary=15000
# hike=15
# new_sal=(hike/100*15000)+salary
# print(new_sal)

# #5
# # r=int(input())
# # area=(3.14159*(r**2))
# # print("area of circle is",area)
# # perimeter=2*3.14159*r
# # print("perimeter of circle",perimeter)

# #6
# input1="A"
# print(ord(input1))

# #7
# # num=int(input())
# # if num%2==0:
# #     print("even")
# # else:
# #     print("odd")

# #8
# i=6
# j=9
# print(i,j)
# i+=4
# print(i)
# i-=2
# print(i)
# i*=j
# print(i)
# i//=j
# print(i)
# i%=j
# print(i)

# #9
# a=5
# b=7
# print(a and b)
# print(a or b)
# print(not a)

# #10
# a=17
# b=5
# print(a<<b)
# print(a>>b)

#11
a=12
b=5
print(a&b)
print(a|b)
print(a^b)
print(~a)


#12 convert str to int
a="123"
b=int(a)
print(type(b))
print(b)
print()

#float to str
a=123
b=float(a)
print(b)
print(type(b))
print()
 
 #int to bool
a=123
b=bool(a)
print(b)
print(type(b))

#13
tem_c=33
tem_f=(tem_c*9/5)+32
print("temperature in fahrenheit",tem_f)

#14
l=22
m=11
print("remainder",l%m)
print("quotient",l//m)

#15
str1=("vijayendar reddy")
print("all upper =",str1.upper)
print("all lower =",str1.lower)
print("length of the string is",len(str1))
print("vijayendar" in str1)

#16
input1=143
sum=0
while input1>0:
    dig=input1%10
    sum=sum+dig
    input1=input1//10
print(sum)

#17
list1=[2,3,4,5,6]
list2=[2,3,4,5,6]
print(list1==list2)
print(list1 is list2)
#18
age=int(input("enter the age"))
months=ge*12
days=age*365
print("age in months",months)
print("age in days",days)
#19
x=10+3.5
y="age"+str(30)
z=True+False+2
print("type of x is",type(x))
print("type of y is",type(y))
print("type of z is",type(z))

#20
n=5
print("n<<1 is",n<<1)
print("n>>2",n>>2)