#what are conditional statements
#Conditional statements are used to execute different blocks of code based on a condition or set of conditions.
#They are used to make decisions in a program.


#There are three types of conditional statements in Python: if, elif, and else.
#The if statement is used to execute a block of code if a condition is true.
#The elif statement is used to check another condition if the first condition is false.
#The else statement is used to execute a block of code if all conditions are false.

m=int(input("enter amount of money you have  "))
if m>=100:
    print("buy coffee")
elif m<100 and m>=50:
    print("buy tea")
else:
    print("Drink water")

########

age=20
if age>=18:
    print("you can vote!")
else:
    print("you are too young to vote")

###########

marks =75
if marks >=90:
    print("grade A")
elif marks >=75:
    print("Grade B")
elif marks >=60:
    print("Grade C")
else:
    print("fail")




# number sign positive or negative
num=int(input("enter a number "))
if num>0:
    print("number is positive")
else:
    print("number is negative")


## nested if 
age=20
citizen =True
if age>=18:
    if citizen:
        print("elgible to vote")
    else:
        print("not a citizen even elgible to vote so cant vote" )
else:
    print("you are too young to vote")

# challenges

#1 check a number divisible by both 3 and 5
num=int(input())
if num%3==0 and num%5==0:
    print("divisible by both 3 & 5")
else:
    print("not divisible by both 3 & 5")

x=int(input("enter value of x "))
y=int(input("enter value of y"))



##2
if x>y:
    print("x is greater than y")
else:
    print("y is greater than x")

#3
marks =75
if marks >=90:
    print("grade A")
elif marks >=75 and marks<90:
    print("Grade B")
elif marks >=60 and marks <75:
    print("Grade C")
else:
    print("fail")


#4 

# to check even or odd of an number
num=int(input("enter a number "))   
if num%2==0:
    print("number is even")
else:
    print("number is odd")

#5
age=int(input("enter thr age here : "))
if age<=20:
    print("Adult")
elif age>=13 and age<=19:
    print("Teen")
else:
    print("Child")
