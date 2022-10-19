num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")
count=0
result = 0
if ch == '+':
    result = num1 + num2
    count=+1
elif ch == '-':
    result = num1 - num2
    count = +1
elif ch == '*':
    result = num1 * num2
    count = +1
elif ch == '/':
    result = num1 / num2
    count = +1
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)

next_calc=input("do you want to continue?(continue/exit):")
if next_calc=="exit":
    print(count)
    "break"

#Enter which operation would you like to perform?
#Enter any of these char for specific operation +,-,*,/: -
#21 - 34 : -13
#do you want to continue?(continue/exit):exit
#1








