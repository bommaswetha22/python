employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

num=int(input("enter num:"))
for i in range(num):
    print(employees[i]['name'])
    print(employees[i]['job'])
    print(employees[i]['address']['city'])
    print("\n")

print(employees[1]['address']['country'])

#Tina
#DevOps Engineer
#New York


#Tim
#Developer
#Sydney


#Australia
