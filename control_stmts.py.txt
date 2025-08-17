#1
l=[3,4,5,63,7,88,2]
for i in l:
    if i%2==0:
        print(i)
        break

#2
password=input("enter the  original password : ")
count=1
while True:
    
    pswd=input("enter your password : ")
    if pswd== password :
        print("password is correct")
        break
    else:
        if count>2:
            print("account locked")
            break
        else:
            count+=1
            print("try again password")



#3

while True:
    ans_type=input("enter your inout here : ")
    if ans_type.lower() =="exit":
        break

#4
l2=[2,5,-1,6,-3,3,6,-2,5,33,-45,65,72,-87]
for i in l2:
    if i<0:
        continue
    print(i)

#5
input2="education"
for i in input2:
    if i  in "AEIOUaeiou":
        continue
    print(i)

print("question 6 answer")
#6
for i in range(1,51):
    if not(i%3==0 and i%5!=0):
        continue
    print(i)

## tasks on pass

#7
def process_data():
    pass
process_data()

#8
class User:
    pass
#9
for i in range(1,6):
    pass
#10
print("answer to 10 th :")
for i in range(51):
    if i==0:
        pass
    elif i%2!=0:
        continue
    else:
        print(i)

l=['hello','hi','meow','wait','cut','go','end','right'] 
for i in l:
    if len(i)>2:
        if i.lower()=='end':
            break
        elif i.lower()=='wait':
            pass 
        else: 
            print(i)
