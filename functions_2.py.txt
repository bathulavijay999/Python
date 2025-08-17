# 1. 
def cube(n):
    return n ** 3
print(cube(3)) 

#2
def average(a, b):
    return (a + b) / 2
print(average(10, 20)) 

# 3.
def square_and_sqrt(n):
    return n ** 2, n ** 0.5 
  
print(square_and_sqrt(16)) 

# 4. 
def is_odd(n):
    return n % 2 != 0

print(is_odd(7)) 

# 5. 
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_digits(1234))  

# 6. 
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())  

# 7. 
def power(base, exponent=2):
    return base ** exponent
print(power(5)) 

# 8. 
def total_bill(item="Sandwich", quantity=1, price=50):
    return f"{item} total price = {quantity * price}"
print(total_bill("Burger", 2, 80))


# 9. Employee info
def employee_info(name, age=30, department="HR"):
    return f"Name: {name}, Age: {age}, Department: {department}"
print(employee_info("Akash"))


# 10. 
def circle_area(radius=1):
    return 3.14 * radius * radius
print(circle_area(3)) 


# 11. 
def sum_of_evens(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total
print(sum_of_evens(10)) 

# 12. 
def largest_in_list(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(largest_in_list([2, 8, 4, 15, 9])) 

# 13.
def min_max(numbers):
    return min(numbers), max(numbers)
print(min_max([3, 7, 1, 9, 4]))


#14.
def student_summary(name, marks):
    total = sum(marks)
    average = total / len(marks)
    return f"Name: {name}, Total Marks: {total}, Average: {average:.2f}"

print(student_summary("Akash", [85, 90, 78, 92]))


#15.
def calculate(num1, num2, operator="+"):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero not allowed"
    else:
        return "Invalid operator"
print(calculate(10, 5))      


print(calculate(10, 5, "-")) 


print(calculate(10, 5, "*")) 


print(calculate(10, 5, "/")) 