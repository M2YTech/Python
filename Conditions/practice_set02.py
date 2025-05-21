subject1 = int(input("Enter your marks: "))
subject2 = int(input("Enter your marks: "))
subject3 = int(input("Enter your marks: "))

total_percentage = (100*(subject1 + subject2 + subject3))/300;

if(total_percentage>=40 and subject1>=33 and subject2>=33 and subject3>=33):
    print("Your are passed: ", total_percentage)
else:
    print("Sorry! you are fail: ", total_percentage)