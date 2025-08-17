# 1. Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. Print even numbers from 1 to 10
i = 2
while i <= 10:
    print(i)
    i += 2

# 3. Print the sum of numbers from 1 to 10
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum =", total)

# 4. Print each digit of a number
num = 123
while num > 0:
    digit = num % 10
    print(digit)
    num //= 10

# 5. Print numbers from 10 down to 1
i = 10
while i >= 1:
    print(i)
    i -= 1


# 6. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 7. Print each character in "banana"
for ch in "banana":
    print(ch)

# 8. Print squares of numbers from 1 to 5
for i in range(1, 6):
    print(i * i)

# 9. Print even numbers in list
nums = [2, 5, 8, 9, 10]
for n in nums:
    if n % 2 == 0:
        print(n)

# 10. Print numbers from 1 to 20 divisible by 3
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

# 11. Star pattern
for i in range(1, 4):
    print("*" * i)

# 12. Number pattern 123 repeated 3 times
for i in range(3):
    print("123")

# 13. Triangle number pattern
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 14. Multiplication table of 2
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)

# 15. Print each character of two words
words = ["hi", "ok"]
for w in words:
    for ch in w:
        print(ch)


# 16. Print numbers 1–10 with Even/Odd
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")

# 17. Ask 5 numbers and print even ones
for i in range(5):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        print(num, "is even")

# 18. Ask until negative number
while True:
    num = int(input("Enter number: "))
    if num < 0:
        break
    print("You entered:", num)

# 19. Print vowels in a word
word = "education"
for ch in word:
    if ch in "aeiouAEIOU":
        print(ch)

# 20. Count vowels in a word
word = "education"
count = 0
for ch in word:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels =", count)


# 21. Print "Hello" 5 times
for i in range(5):
    print("Hello")

# 22. Ask favorite color 3 times
for i in range(3):
    color = input("Enter your favorite color: ")
    print("You like", color)

# 23. Print pattern
for i in range(1, 4):
    print(chr(64 + i) * i)

# 24. Count 'a' in "banana"
word = "banana"
count = 0
for ch in word:
    if ch == "a":
        count += 1
print("Count of 'a' =", count)

# 25. Print 1–10 with Small/Big
for i in range(1, 11):
    if i < 5:
        print(i, "Small")
    else:
        print(i, "Big")
