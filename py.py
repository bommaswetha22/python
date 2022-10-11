employee={
 "name": "tim",
 "age": 30,
"birthday" :"1990-03 -10",
 "job" : "devops engineer"}
employee.pop("age")
employee.update({"job":"software engineer"})
print(employee)
for x,y in employee.items():
  print(x,y)