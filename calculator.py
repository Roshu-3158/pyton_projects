print("***** Calculator *****")
a = int(input("Enter the first number : "))
b = int(input("Enter the second number :"))

print("Which operation you wants to perform : ")
print("1)Addition")
print("2)Substraction")
print("3)Multiplication")
print("4)Divison")
c =int(input("Select one operation :"))

if(c==1):
    print("The addition is : ",a+b)
elif(c==2):
    print("The substraction is : ",a-b)
elif(c==3):
    print("The multiplication is : ",a*b)
elif(c==4):
    print("The divison is : ",a/b)
