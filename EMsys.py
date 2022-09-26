def editEmp():
        pass
def dispAll():
        pass
def dispId():
        pass
def delEmp():
        pass



import sys
import os
file=open("data.txt","a+")
while True:
    os.system("cls")
    print("\n\t\t\tEmployee Management System\n ")
    print("1. Insert Employee Record")
    print("2. Edit Employee Record")
    print("3. Display All Employee Record")
    print("4. Display Employee Record By Employee Id")
    print("5. Delete  Employee Record")
    print("6. Exit")
    choice=int(input("\nEnter choice : "))
    if choice==1:
        file.write(input("Employee Id=")+"\n")
        file.write(input("Employee Name=")+"\n")
        file.write(input("Employee Department=")+"\n")
        file.write(input("Employee e-mail Id=")+"\n")
        file.write(input("Employee salary=")+"\n")
        file.close()
    elif choice==2:
        file=open("data.txt","r+")
        file.write(input("Employee Id=")+"\n")
        file.write(input("Employee Name=")+"\n")
        file.write(input("Employee Department=")+"\n")
        file.write(input("Employee e-mail Id=")+"\n")
        file.write(input("Employee salary=")+"\n")
        file.close()
    elif choice==3:
        file=open("data.txt","r")
        dis=file.read()
        print(dis)
        file.close()
    elif choice==4:
        id=input("Enter Employee Id=")
        data = file.readlines()
        for line in data:
                word = line.split()
                print(word)
                file.close()
    elif choice==5:
        delEmp()
    elif choice==6:
        sys.exit()
    else:
        print("Invaid choice....")
  
 
