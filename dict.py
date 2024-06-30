std={}
# asking number of students from user
n=int(input("Enter the number of students: "))
for i in range(n):
    st=input("Enter the student name: ")
    std[st]=int(input("Enter his usn: "))
print(std)