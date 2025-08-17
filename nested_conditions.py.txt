#1
bottles=int(input())
customer_type=input("regular or non regular")
bill=int(input("enter the bill amount: "))
if bottles >=2:
    if customer_type == "regular":
        bill= bill-((15/100)*bill)
        print("bill is ", bill)
    else:
        bill= bill-((5/100)*bill)
        print("bill is ", bill)
else:
    print("bill is ", bill)

#fuel check
fuel_level=int(input("enter fuel level"))
vehicle_type=input("enter vehivle type car or bike")
vehicle_type.lower()
if fuel_level <= 25:
    if vehicle_type == "car":
        print("Refuel soon at a petrol station")
    elif vehicle_type ==" bile":
        print("Refuel at nearest ppump")
else:
    print("check vehicle type")

#3
grade=int(input())
income= int(input("income in lakhs  enter only number"))

if grade>85:
    if income<3:
        print("elgible for scholarship")
    elif income>=3 and income<=6:
        print("elgible for half scholorship")
    else:
        print("not elgible for scholorship")


# 4 Shopping Cart Offer

cart_value = int(input("Enter the total cart value: "))
payment_method = input("Enter the payment method: ")
if cart_value > 1000:
    if payment_method == "card":
        discount = (10/100) * cart_value
        print("Discount: ", discount)
    elif payment_method == "UP!":
        discount = (15/100) * cart_value
        print("Discount: ", discount)
else:
    print("No discount")

#5

age = int(input("Enter your age: "))
vaccinated = input("Are you vaccinated? (yes/no): ")
vaccinated.lower()
if age >= 18:
    if vaccinated == "yes":
        print("Allowed to dine in")
    elif vaccinated == "no":
        print("Takeaway only")
else:
    print("You must be at least 18 to dine here.")


#6

age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))
if age >= 14 and age <= 18:
    if height > 160:
        print("Eligible for tryouts")
    else:
        print("Not eligible (too short)")
else:
    print("Not eligible (age out of range)")


#part B
# 1
light_color = input("Enter the light color: ")
if light_color == "green":
    print("Go")
else:
    print("Stop")

# 2. 
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult Ticket")
else:
    print("Child Ticket")

# 3
amount_spent = int(input("Enter the amount spent: "))
if amount_spent >= 500:
    print("You get a free gift!")
else:
    print("No gift")
#4
location = input("Enter your location: ")
if location == "local":
    delivery_fee = 20
else:
    delivery_fee = 50
    print("Delivery fee is: ", delivery_fee)

# 5
temperature = int(input("Enter your temperature: "))
if temperature >= 100:
    print("High Fever")
else:
    print("Normal")


#6

units = int(input("Enter the units consumed: "))
if units < 100:
    print("Free")
elif 100 <= units <= 300:
    if "residential" == input("Is it residential? "):
        print("Rs5 per unit")
    else:
        print("Rs8 per unit")
else:
    print("Rs10 per unit flat")







