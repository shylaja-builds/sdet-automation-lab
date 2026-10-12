# Print string
print("Hi! I am Prateek!")

# 4 arithmetic operations
num1 = 55
num2 = 34

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print(f"Add: {add}\nSub: {sub}\nMul: {mul}\nDiv: {div}")

# Area and Perimeter of Rectangle
length = 37
breadth = 10.5

perimeter = 2*(length + breadth)
area = length * breadth

print(f"Perimeter {perimeter}\nArea {area}")

# Divisibility
num1 = 35
num2 = 7

if num1%num2 == 0:
    print(f"Number {num1} is divisible by number {num2}")
else:
    print(f"Number {num1} is not divisible by number {num2}")
#display quotient and remainder
num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))

remainder = num1%num2 
div = num1/num2
#remainder = quotient - div

print(f"The quotient is {div}\nThe remainder is {remainder}")
# Area of trianhle
height = int(input("Enter height: ")) 
base = int(input("Enter base: ")) 

Area = 0.5 * height * base
print("Area of the triangle is",Area)
#Simple Interest
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time(in years): "))

SimpInt = (principal * rate * time) /100
print(f"The simple interest for a principal amount of {principal} rupees, a rate of {rate}% and a time of {time} years is {SimpInt} rupees")

#Finding the square and cube
num = (int(input("Enter the number here: ")))

square = num * num
cube = num * num * num
print (f"The square of the number is {square} and the cube of the number is {cube}")

#Checking the eligibility to vote
age = (int(input("Enter your age here: ")))
if age >= 18:
    print("you can vote :D")
else:
    print("Go away")