#Write a program that uses built-in functions to find the largest and smallest among three numbers.

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

maximum=max(num1,num2,num3)
minimum=min(num1,num2,num3)

print('The largest number is ',maximum)
print('The smallest is  ',minimum)