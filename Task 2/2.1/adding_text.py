# adding a text
with open("Task 2/2.1/text_file1.txt" ,"w") as file :       # w overwrites.
    file.write("Adding text to this txt file using with statement. ")

with open("Task 2/2.1/text_file1.txt" ,"r") as file :
    content = file.read()

print(content)        


with open("Task 2/2.1/text_file1.txt" , "a") as file :      # a appends.
    file.write("\nAdiing another line of text to this file .")    # \n adds this text to the next(new) line.

with open("Task 2/2.1/text_file1.txt" , "r") as file :
        content1 = file.read()

print (content1)        
