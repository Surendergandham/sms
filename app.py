print("Welcome to student Management System")
print(" 1.Student Services \n 2.Teacher Service")
Userchoice=int(input("Enter the Appropriate Choice "))
if Userchoice==1:
    print(" 1. Attendance \n 2. Minor Marks \n 3. Hostel Services")
    innerchoice=int(input("enter the choice in subcategory "))
    if innerchoice==1:
        print("Your attendance details are :")
    if innerchoice==2:
        print("your minor marks are :")
    if innerchoice==3:
        print("Hostel Services")
if Userchoice==2:
    print(" 1. Upload Attendance \n 2. Upload Minor Marks")

