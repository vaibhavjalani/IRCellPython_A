import addone
import subsone
import mult

a=int(input("Enter First Number "))
b=int(input("Enter Second Number: "))
print("What You Want to do ?")
print("add")
print("substract")
print("multiply")
op=input()
if op=="add":
    addone.add(a,b)
elif op=="substract":
    subsone.subs(a,b)
elif op=="multiply":
    mult.multiply(a,b)