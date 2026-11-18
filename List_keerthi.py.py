#1
students = ['krishnapriya','grace','keerthi','jayalakshmi','anjali']
print('student')
students.insert(2,'anjali')
students.append('darshana')
print('2',students)

#2
list1 = ["Rice", "Sugar", "Milk"]
list2 = ["Bread", "Eggs", "Butter"]
list1 .extend(list2)
print(list1)
print(list2[len(list2)-1])

#3
numbers = [10, 20, 10, 30, 40, 10, 20, 50]
print("the no of times '8' appear in the number= ",numbers .count('8'))

#4
list1 = [1,2,3,4,5,6,7,8,9,10]
list1 .reverse()
print(list1)

#5
marks = [78, 45, 92, 56, 88, 34, 67]
marks .sort()  
print(marks)

marks.sort(reverse= True)
print(marks)

#6
fruits = ["Apple", "Banana", "Mango", "Orange"]
print('fruits')
fruits.insert(3,'grape')
print('3',fruits)

#7
subjects = ["English", "Maths", "Science", "Computer", "History"]
subjects .pop()
print(subjects)

#8
colours = ["Red", "Blue", "Green", "Yellow", "Blue"]
colours .remove("Green")
print('green',colours)

#9
list1 = ['python', 'java', 'c','javascript','c++']
list1.clear()
print(list1)

#10
students = ["Anu", "Rahul", "Meera", "Arun", "Diya"]
students .append("kiran")
print(students)

students .extend(["sneha","vijay"])
print(students)

students.insert(2,"ravi")
print(students)

print("the no of times 'anu' appear in the student= ",students .count('anu'))

students.sort()  
print(students)  

students.remove("Rahul")
print(students)

students.pop()
print(students)

students .reverse()
print(students)










