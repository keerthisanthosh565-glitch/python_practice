string1 = 'i am  keerthi [and [from kottayam]]'

string2 = 'python' 
string3 = ' programming'

print(string1) # i am  keerthi [and [from kottayam]]'
print(string2) #python
print(string3) #programming
print('\n') # new line
print(string2, string3) # python programming

# by default python prints a new line at the end.

# changing the end string from '\n' to '&'
print(string2 , end='&') #python&
print(string3 , end='&') #programming&
print('\n', end='&') # new line&
print(string2, string3 , end='&') # python programming&

# \n new line
# \t new tab

print('\t','string2,string3')

print('**************************************')

print(string2,string3)

s1 = 'ICT'
s2 = 'Academy'
s3 = 'of'
s4 = 'kerala'
# string concatenation

print(s1+ s2 +s3 + s4) # ICTAcademyofkerala
print(s1, s2 ,s3 , s4) # ICT Academy of Kerala

combined_string  = s1 +''+ s2 +' '+ s3 +' '+ s4 
print(combined_string)   #ICT Academy of kerala

print('***************************************')

print(s1)               # ICT
print(s1+ s2 +s3 + s4)  # ICTICTICTICT
print(s1*5)             # ICTICTICTICT
print((s1 + '  ') * 5)  # ICT ICT ICT ICT 
print((s1 + '\t') * 5)  # ICT ICT ICT ICT ICT  # tab
print((s1 + '\n') * 5)   # new line

print('***********  index **********************')
print(string3)      # programming
print(string3[0])   # prints character value at 0th index
print(string3[5])   #
print(string3[10])  # last character
# print(string3[11])# we cannot go beyond the maximum index of a string.

string1 = 'i am  keerthi [and [from kottayam]]'
print(string1[-1])  # last index value.

#************************************************
#*********** slicing*****************************
#************************************************

s1 = 'TRIVANDRUM' 
print(s1[-4])  
print(s1[6])    # will display 7th character
print (s1[0:5]) # slicing start index= 0, end index =4 , 'TRIVA'
print(s1[6:10]) # slicing , 'DRUM'
print(s1[4:7])  # 'and'

print(s1[:5])  # satrt index till 5  'TRIVA'
print(s1[6:])  # from 6th index till index 'DRUM'

print(s1[:5:2])  # introducing step operator (step is 1) 'tia'
print(s1[0:8:3]) # "TVD" 1st T and take 3rd V then D.

string_demo = "join our offline programs in kerala's IT parks"

print(string_demo[5:])   # from 5th to end.
print(string_demo[5::2]) # 5th end then 2nd add cheyyth.
print(s1[::-1])          # reverse order.
# starting indx : end : step default 1

#*************************************************
#********** Functions*****************************
#*************************************************

print(s1)
print(s1.lower())      # convert string to lowercase
print(s1.upper())      # convert string to uppercase
print(s1.swapcase())   # switches case of each character in the string 'trivandrum'
print(s1.capitalize()) # first letter is upper and the rest will be lower Trivandrum'


