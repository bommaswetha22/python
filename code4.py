my_list = [6,8,0,5,8,7,9,10]
even_nums = [num for num in my_list if num % 2 == 0]
print("even numbers in list are:",even_nums)

#lower and upper string count
string = input("Enter string:")
count1 = 0
count2 = 0
for i in string:
    if (i.islower()):
        count1 = count1+3
    elif (i.isupper()):
        count2 = count2+3
print("The no.of lower characters is:")
print(count1)
print("The no.of upper characters is:")
print(count2)

#Youngest employee
def get_age(employee):
    return employee.get('age')
employee = [{ "name" : "Tina",
              "age" : "40",
              "DoB" : "1990-03-10",
              "job": "Devops Engineer",
              "address":{"city":"New york","country":"USA"}},
            { "name" : "Tim",
              "age" : "35",
              "DoB" : "1985-02-21",
              "job": "Devoloper",
              "address":{"city":"Sydney","country":"Australia"}}]
employee.sort(key=get_age)
print(employee[0]['name'],'\n', employee[0]['age'])