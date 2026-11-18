#1
# fruits ={'Apple', 'Banana', 'Orange', 'Mango', 'Grapes'}
# print(fruits)
# print(len(fruits))

#2
# numbers1 = [10, 20, 10, 30, 20, 40, 50, 30]
numbers ={10, 20, 10, 30, 20, 40, 50, 30}
print(set(numbers))

#3
colour = {"red", "blue", "green"}
colour.add("yellow")
print(colour)
colour.add("black")
print(colour)
colour.remove("blue")
print(colour)

#4
student1 = {"Python", "Java", "SQL", "HTML"}
student2 = {"Python", "C++", "SQL", "CSS"}
print(student1.intersection(student2))

#5
student1 = {"Python", "Java", "SQL", "HTML"}
student2 = {"Python", "C++", "SQL", "CSS"}
print(student1)
print(student2)

#6
student= {'name': 'Rahul','age': '20',
          'course':'python','city': 'Kochi'}
print('whole_dictionary')
print(student)

print(student['name'])
print(student['age'])
print(student['course'])

#7
employee = {"name":"Anu", "age": 25, "salary": 25000}
employee["department"]='IT'
print(employee)
employee["salary"]='30000'
print(employee)
employee["age"]='26'
print(employee)

#8
marks = { "Maths": 80, "Science": 75, "English": 90,
"Computer": 85}
marks.keys()
print(marks.keys())
print(marks.values())
print(sum(marks.values()))
sum_ =sum(marks.values())
avg = len(marks.values())
avg_stu = sum_/avg
print(avg_stu)

#9
student = {"name": "Arun", "age": 21, "course": "Python",
"marks": 85}
print(student['name'])
print(student['course'])

if(student['marks']>= 50):
    print("pass")
else:
    print("fail")

student["grade"]='A'
print(student)

for i in student.items():
    print(i)

#10
morning_batch = {"Anu", "Rahul", "Arun", "Meera"}
evening_batch = {"Rahul", "Meera", "John", "Priya"}


print(morning_batch.difference(evening_batch))
print(morning_batch.intersection(evening_batch))
print(morning_batch.difference(evening_batch))
print(evening_batch.difference(morning_batch))


