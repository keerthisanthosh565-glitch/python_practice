#************************************************#
#*************SET*******************************#

#declare a set
# method 1
set1= {}

#method 2
set2 = {12,55,88,2026,True,'BSNL',2026,2026.0,'2026'}  # dic {} ith set alla dict  ahn
#method 3
set3 = set()

print(type(set1)) # strng allowed ahn'2026'.
print(type(set2)) # duplicate undel delete avum.
print(type(set3))  # index onm pattila.(list,tuple onum pattula)

print(set2)   # multiple data accept aavum (hetroginous ahn)# repeated value not consider set il

#****************************************************
#*****************************************************
#               FUNCTIONS

roll = {1,2,3,4,5,6}
roll_odd ={1,3,5}
roll_even ={2,4,6}
random ={1,5,9,4}

random.add(2026) # value vre set ilk add aakan
print(random)

print(random.difference(roll_odd)) # randathil und il und bt roll  illa
print(roll_odd.difference(random)) # roll il und randathil illa

print(roll.issuperset(roll_odd)) # roll t superset ahno roll odd nn.
print(roll.issubset(roll_odd))   # roll t subset ahno roll odd nn.
print(roll.issuperset(random))   # roll t superset ahno random nn.

print(random.intersection(roll_even)) #intersection varunna value.
print(roll.union(roll_odd)) 
print(random.isdisjoint(roll_even))

#properties of data type set:
# set support hetrogenous datatype
# cannot access data using index
# duplicate cannot allow
# mutable.
 


#*****************************************************#
#******DICTIONARY************************************#

#declare a set
# method 1
dict1= {}
#method 2
dict2 = {'key1':'value1','key2':'value2','key3':2027}
#method 3
dict3 = dict()
print(type(dict1)) 
print(type(dict2)) 
print(type(dict3))  

print(dict2)  # key value pair
print(type('key1')) # data type nokkiyath

sample_dict = {1:'one',0:'zero',1:'True',1:'ICT'}
print(sample_dict) # duplication vannal leatest value edukum
print(dict2['key2']) # key2 t corresponding value ahn varunnath,(index varum pole)key2 t value ahn


student_dict = {'name':'keerthi',
                'age':24,
                'university' : 'MGU',
                'district' : 'kottayam'}
#print whole the keys
print('whole_dictionary')
print(student_dict) # full dic ayitt print aaknm

#printing keys
print(student_dict.keys()) # head ayit kodukunne keys

print(student_dict.values()) # head t value

print(student_dict.items()) # key value pair list ,aakit tuples create aaki athint list

student_dict['university'] = 'kerala university'
print(student_dict) # university maati vere vech

personal_dict = {'name':'keerthi',
                'mobile_no':9633271574,
                'e-mail' : 'keerthisanthosh@gmail.com',
                'school' : 'Govt.hss kulashekaramangalm'}
print('whole_dictionary')
print(student_dict)


