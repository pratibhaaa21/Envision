# adding a text
with open("Task 2/2.1/text_file1.txt" ,"w") as file :
    file.write("Adding text to this txt file using with statement. ")

with open("Task 2/2.1/text_file1.txt" ,"r") as file :
    content = file.read()

print(content)        
