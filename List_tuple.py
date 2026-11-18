# # List is data type collection of value
# # since it is a combination of other data type(int,float
# #strng, bool), we call it as a derived data type

# # there is no restrictions in terms of data type


# # name =""
# # name ='keerthi'
# # print(type(name))  # strng


# # name1 = []
# # print(type(name1))   # list

# # name2 = ['vishnu','akash','ajith'] # list
# # print(type(name2)) 



# # fetching value using index from a list
# # print(name2[0])
# # print(name2[1])
# # print(name2[2])
# # print(name2[3]) # error

# # a list can contain various type of data.- heterogenos

# # list contain multiple of data type 

# # personal info as a list : name, age, graduation year, university, heigh
# amar_info = ['amar', 22, 2026, 'cusat', 172.5]
# print(type(amar_info))

# print(amar_info[0])
# print(type(amar_info[0]))

# print(amar_info[1])
# print(type(amar_info[1]))

# print(amar_info[2])
# print(type(amar_info[2]))

# print(amar_info[3])
# print(type(amar_info[3]))

# print(amar_info[4])
# print(type(amar_info[4])) # list, stng, int ahno nn mansilavum

# list1 = [1,2,3]
# list2 = [True, False, False]  # concatinate 
# print(list1 + list2)

# #*********************************************************
# list1 =list1 + list2

# list1 = [1,2,3]
list2 = [True, False, False]
# name2 = ['vishnu','akash','ajith']

# print(list1)   #unsort  
# list1.sort()
# print(list1) #sort 1,2,3

# print(name2)   #unsort
# name2.sort()
# print(name2) #sort

# list1.sort(reverse= True)  # sort the other way (descending)
# print(list1)                #[3,2,1]

# # name2 = ['ajith', 'akash', 'vishnu',3,2,1]

# name2.extend(list1)  # list extended with values of list1
# print(name2)

# name2 .append(list1) # list1 was added as the last value of list2
# print(name2)
# print(name2[3])

# list1 .append('A')
# print(list1)

# list1 .reverse()
# print(list1)  # reverse cheyth kitty

# print('the no of times false appear in the list= ',list2 .count(False)) #check the count of value 'false'
# print('the no of times true appear in the list= ',list2 .count(True))
# print("the no of times 'x' appear in the list= ",list2 .count('x'))




# #fetch number of items in the last   #-1 varathe knd pidikunth
# len(list2)
# print('total number of elements in', list2,'is', len(list2))



# #value at the last index
# print(list2[-1])
# print(list2[len(list2)-1])


# print('before clear')
# print(list2)

# list2 .clear()  # clears all value from the variables

# print('after clear')
# print(list2)

# #*****************************************************#

# print(list1) #[3,2,1,'A]
# #in order to do # [3,2,1,'A']-> [3,2,1,'A']
# # is inserting 100 at index 2
# list1 .insert(2,100) # inserting 100 at index 2   # 2 kodknm
# print('after inserting a value', list1)  #[3,2,1,'A']

# #***************************************************#

# print('before removing 3', list1)
# list1 .remove(3)
# print('after removing 3',list1) # value we waant to remove

# #**************************************************#

# list1 .pop()
# print(list1)  # last value remove aakan


#******************************************************#
#  TUPLE

tuple1 = ()
tuple2 = (2026,"nov",3.75, False,[8,True,9.8])
tuple3 = tuple()
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

print(tuple2 [2])  # index [] il ahn

print(tuple2.count('nov'))
print(tuple2 .index('nov'))  # modify chyyyan pattula

#once a tuple created, we cannot make any chnge to it:
# list -> mutable
#tuple -> immutable 
# del(tuple2) # deleting variable
# del(list2)   # deleting variable list2

print(tuple2)  # get an error saying that variable does not exist
print(list2) # get an error saying that variable does not exist











