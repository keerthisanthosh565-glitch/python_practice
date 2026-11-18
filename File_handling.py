#******************************************************#
#********file handling********************************


#
file = 'C:/PGP_DATA_SCIENCE_AIML/python/text_file.txt'
relative_file='text_file.txt'
file = open(file,'r')

content = file.read()    #1
# print(content) 
file . close()
file_1 = open(relative_file,'r') #2 relative file path vec open aakunth
content_1 =file_1.read()
print(content_1)
file_1 . close()
# we trying using reltive file path
def read_file_filepath():       # function define chyth read chyunth
    file_1=open(read_file_filepath,'r')
    content_1 = file_1.read()
    print(content_1)
    file_1 . close()
# file.read () will return all the value as a single string
#print (type(content_1)) # a ssingle string

# read single line
def read_line_by_line():
    file=open(relative_file,'r') # open akan,
    content = file.readline()   
    print(content)
file . close()
read_line_by_line()

# read single line       # vere method
def read_lines():
    file=open(relative_file,'r')
    content = file.readlines()
    print(content)
    print(type(content))
    file . close()
read_lines()

# read single line       # line by line varan
def read_lines():
    file=open(relative_file,'r')
    # read all lines and populates the list 'content'
    content= file.readlines()
    for line in content:
        print(line)
        print(type(content))
        file . close()

read_lines()
#*********************************************************
#write cheyyan oru txt file
write_path ='students.txt' 

def write_into_file():  # open a filein writing mode
    file =open(write_path,'w')  # if the file didn't exist earlier,now,it will be created
    file.write("gowtham")               # and opened in writing mode
    file.close()
write_into_file()                       # file is variable

def student_name():
    file = open(write_path,'w')
    file.write("keerthi\n")
    file.write("krishna\n")
    file.write("grasu\n")
    file.close()

student_name()

def append_file():
    file = open(write_path,'a')
    file.write('keerthi')
    file.close()

append_file()

#generic function to append a data to a function.
def append_data_new(i_filepath,i_name):
    with open(i_filepath,'a')as files:
        files.write('\n')
        files.write(i_name)
        

append_data_new('text_file.txt','airtel')







