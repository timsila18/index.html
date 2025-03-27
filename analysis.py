#core concepts of the analysis
# 1. File streams
# 2. File the modes
# 3. File pointer


#Opening a file
#f = open('data.txt','r')
#f = open('data.txt','w')
#opening file is done using the open() function
takes the file name and the mode as the arguments
Reading methods - read() reads the entire content of the file as a string
readline() reads a single line from the file as a single string
readline() reads a single line from the file and readlines() reads all lines from the file and returns them as a list of reads

File Context Managers
using with statements ensures files are properly closed after its suite finishes
with open("file.txt", "r") as f:
    data = f.read() # read the entire file; brackets becauses its a method
print(data)

Writing data from python to a file
with open("file.txt", "w") as f:
    f.write("Hello, World!")

    File Types
    text files -  they contain plain text
    csv files - they store tabular data in plain text; comma separated values
    json files - they store data in json format
    #json files are used to store data in a structured way and are easy to read and write and are used for web development
    #json files separated by commas
    #curly braces are used to define objects
    #square brackets are used to define arrays
    Binary files - they store data in the form of bytes. Store data in binary format which is not human readable
    #binary files are used to store data in a compact format
    #binary files are faster to read and write compared to text files
    #binary files are used to store images, videos, executables, etc    
    #binary files are opened in binary mode
Kaggle - a platform for data science and machine learning
    

# Data analysis in base python

