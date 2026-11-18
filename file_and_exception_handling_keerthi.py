#1

def read_file():
    try:
        file = open("friends.txt","r")
        content = file.read()
        print(content)
        

    except FileNotFoundError:
        print("file not found")
    except TypeError:
        print("file name is wrong")

read_file()

#2
def create_file():
    try:
       with open("friend.txt","w")as file:
        #file="friend.txt"
        file.write("file create")
        print("\n")
        print("file create")
    except Exception as e:
        print("not created:",e)
create_file()

#3
def friend_name():
    with open("friend.txt",'a')as files:

        files.write(file1)
        print("\n")
        print(file1)
file1= input("best friend name")

friend_name()
     

           

    
    
        

