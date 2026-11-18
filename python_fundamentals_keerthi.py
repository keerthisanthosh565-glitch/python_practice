#1
name = ('keerthi')
age = 22
height = 5.4
enrolled = True
subject= ['english', 'maths', 'malayalam',]
DOB = (28,9,2002)
skills = {"excel","python"}
student = {"name":"keerthi","age":"24","course":"data science"}


print(type(name)) 
print(type(age))
print(type(height))
print(type(enrolled))
print(type(subject))
print(type(DOB))
print(type(skills))
print(type(student))

#2
python = 80
maths = 70
science = 60

total = python + maths + science
print("total:", total)

average = total/3
print("average:", average)  # average

print("highest mark:", max(python , maths , science))
print("lowest mark:",min(python , maths , science))

print(python>40)
print(maths>40)
print(science>40)
print("************************")
#3
subject = {'python':15,'maths':45,'science':10}
total =subject['python'] +subject['maths'] + subject['science']
print("subject:" , total)

if (total >= 90) :
     print("grade:A")
     print('eligible for certificate')
     
elif(total >= 75):
   print("grade:B")
   print('eligible for certificate')
   
elif(total >= 60):
    print("grade:C")
    print('eligible for certificate')

elif(total >= 40):
    print("grade:D")

else:
   print("grade:fail")

for num in subject ["python"]>=25,subject["maths"]>=25,subject["science"]>=25:
    print('subject passed',num)



#4
subject_mark = [45, 38, 72, 90, 55]
total= 0
pass_coun=0
fail_cou=0

for i in subject_mark:
    print('mrks',i)
    total = total+i
    if i >=40:
       # print('pass')
        pass_coun=pass_coun+1
    else:
       # print('fail') 
        fail_cou=fail_cou+1  

print("total:", total)
print('pass_count',pass_coun)
print('fail_count',fail_cou)
print('******************************')

#5

num =1
while(num < 50):
  print(num)
  num = num +1


num = 1
while(num < 50): # odd number from 1 to 50
    print(num)
    num = num +2

num = 2
sum = 0
while num <= 50:
    sum = sum + num
    num = num + 2
print(sum)

num = 1
sum = 0
while num <= 50:
    sum = sum + num
    num = num + 2
print(sum)

#6
skills ={"python", "excel","SQl"}
skills.add("java")
print(skills)
skills.remove("excel")
print(skills)
print("python",skills)
print(skills)

#7
student = {"name":"keerthi","age": 20,
           "course":"data science","total mark": 380,
            "average mark":76,"grade": "B","certificate eligibility": True }
print(student)
