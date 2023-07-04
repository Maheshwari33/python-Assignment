import mathopr as m


# Create an instance of MathOperations
class Invalidinput(Exception):
    def _init_(self,message):
        super()._init_(message)  
try:
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
except ValueError as error:
    raise Invalidinput("the provided values are invalid")  from error
opr=m.MathOperations


# Call member functions
print("Choose from below: ")
print("1) Addition\n2) Subtraction\n3) Trignometric")
n=int(input("Enter your choice: "))

if n==1:
    add = opr.add()
    print("Addition:", add)
    

elif n==2:
    sub = opr.subtract()
    print("Subtraction:", sub)
    

elif n==3:
    print("Choose from below: ")
    print("1) Sine\n2) Cosine ")
    if n==1:
        print("Sine: ",opr.sincalculate())
    if n==2:
        print("Cosine: ",)
    else:  
        print("Wrong Choice")

else:
    print("Invalid Choice")

    
# mul = opr.multiply()
# div = opr.divide()
# sqr = opr.square_root()

# print("Addition: ",add)
# print("subtraction: ",sub)
# print("Multiplication:", mul)
# print("Division:", div)
# print("Square Root:", sqr)