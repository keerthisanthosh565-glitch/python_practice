#*********************************************
#******ITERATIVE STATEMENT*********************
#**********************************************



#print your name 10 times
# for i in range (10): # we are giving number of iterations.
#     print(i, ' :keerthi') #iterative (repetitive) task.


# for i in range(0,10,2): # we are giving number of iterations.
#     print(i,': keerthi')

# print('using step operator')

# for i in range(10,2):
#     print(i,':keerthi')

# # range (start, end , step) # step is notmention , it takes step =1.

# for i in range (3,10,3):  # 3,6,9.
#     print(i,':keerthi')

# for i in range (3,10,):  # 3,6,9.
    # print(i,':keerthi')

# giving step as a negative value

# for i in range (10,3,-1):  
#     print(i,':keerthi') # 10,9,8,7,6,5,4

# # print odd number <50

# for i  in range (1,50,2):  # 0 kodthal even aavum, last even number kodkkanam
#     print(i,' : odd number')

#print odd number between 20 and 50
# for i  in range (21,50,2):
#     print(i,':odd number between 20 and 50') #i,: ath venda
#**********************************************************
#****** while loop*****************************************
#*********************************************************

# num =1
# while(num < 10):
#     print(num)
#     num = num +1

# print('end of while loop')

# num = 1
# while(num < 50): # odd number from 1 to 50
#     print(num)
#     num = num +2
  
# num = 21
# while (num < 20): # odd number
#     print(num)
#     num =num + 2

# print('odd number between 20 and 50')
# num2= 21
# while (num2< 50): #odd num kanan 21 to 49
#     print(num2)
#     num2 =num2 + 2
    
# print('\n','odd number between 20 and 50')
# num2= 21
# while (num2< 50):
#     print(num2,end = ',') # 21,23,24,25,.............49 varem
#     num2 =num2 + 2

# Logical operators in control flow statement
age = int(input('please enter our age :'))
vaild_id = input('do you have a valid id card (y/n):')
if(vaild_id == 'y'):
    vaild_id= true 
else:
    vaild_id = False

# verifying eligibility to vote
print(" we are checking your eligibility")

if(age >= 10):
    if(vaild_id):
        print('your eligibile to vote')
    else:
        print('your not eligibile to vote')
        print(' you need a valid id card to be eligible')
else:
    print('your not eligibile to vote')
    print('you should be 18or above to be eligible')

#('_____________________________________________________)
#doing the same process using logical operators 
if ( age >= 18) and (vaild_id):
    print('your eligibile to vote')
else:
    print('your not eligible to vote')





