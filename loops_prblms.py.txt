# for i in range(51):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i)

#1
# while True:
#     n=int(input())
#     if n%11==0:
#         print("divisible by 11, Thank you")
#         break
#     else:
#         print("enter again number")
# #2
# str1=input()
# count=0
# for i in str1:
#     if i in "AEIOUaeiou":
#         count+=1
# print(count)

#3
num=100
while num>=2:
    print(num)
    num-=2

#4
# while True:
#     pswd=input()
#     if pswd=='admin123':
#         break
#     else:
#         print(" enter again: ")

#5
# num2=int(input())
# for i in range(1,11):
#     print(num2, "*", i,"=" ,i*num2)

#6
# l=list(map(int,input().split()))
# for i in l:
#     if i>0:
#         print(i)
#7
# num3=int(input())
# print((num3 * (num3+1))//2)
#8
print("prime numbers are")
for num in range(1, 51):   
    if num < 2:            
        continue
    
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break
    
    if not is_prime:
        continue   
    
    print(num)

#9
sum=0
while True:
    usr_num=int(input("enter a  no:"))
    if usr_num==0:
        print(sum)
        break
    else:
        sum+=usr_num
