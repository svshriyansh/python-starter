a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    large = a
else:
    large = b
    
if c > large:
    large = c
print("Largestof {},{} and {} is: {}".format(a, b, c, large))