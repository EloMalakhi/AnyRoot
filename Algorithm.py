
a = "\u2588"
x = 0

print("\nThis algorithm computes this expression")
print("           Z / Y")
print(f"{a}       {a} ")
print(f"  {a}   {a}  ")
print(f"    {a}   ")
print(f"  {a}   {a} ")
print(f"{a}       {a}")

x = float(input("What is the value of x?\n"))
while x <= 0:
    print("Sorry, x must be larger than 0\n")
    x = float(input("What is the value of x?\n"))

    

print("\n\n\n\n")
z = float(input("What is the value of Z?\n"))

while z != int(z):
    print("Sorry, the value of Z must be an integer\n")
    z = float(input("What is the value of Z?\n"))


print("\n\n\n\n")
y = float(input("What is the value of Y?\n"))

while y != int(y):
    print("Sorry, the value of Y must be an integer\n")
    y = float(input("What is the value of Y?\n"))

print("\n\n\n\n")
print("the algorithm is the following power series algorithm\n\n")
print("A^Z* (1 + c1*P + c2*P^2 + c3*P^3 + ...)")
print("A is a guess that speeds up the algorithm")
print("changing the value of A changes the value of P which will influence the speed of the algorithm.")
print("As P is closer to 0, the less steps it will take for the algorithm to compute the expression.\n")
print("P = (x - A^Y) / (A^Y)\n")
print("c_n = 1 if n = 0")
print("c_n = c_n-1 * (Z + Y*(1-n))/(n*Y)\n\n")
print("if y equals z then c1 will be 1 and c2 and upward will be zero")
print("which will result in the expression being A^Z*(1 + (x-A^Y)/A^Y)")
print("which is the same as x")

print("\n\n\n\n\n")
A = float(input("What is the value of A?\n"))
P = (x - A**y)/(A**y)

while abs(P) >= 1:
    print("Sorry, the absolute value of P must be smaller than 1\n")
    print("Enter a different value for A")
    A = float(input("What is the value of A?\n"))
    P = (x - A**y)/(A**y)

print("\n\n\n\n\n")
print("When you have your precision acquired type in any key to quit")

Rs = ""
cn = 1
power = 1
result = 1
n = 0
while Rs == "":
    n += 1
    power *= P
    cn = cn * (z + y*(1-n))/(n*y)
    result += cn*power
    print(result)
    Rs = input()
print(f"Expression = {result*(A**z)}")