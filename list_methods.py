from rich import print
Students = [];
s1=input("Enter the Marks of Student 1: ");
Students.append(s1);
s2=input("Enter the Marks of Student 2: ");
Students.append(s2);
s3=input("Enter the Marks of Student 3: ");
Students.append(s3);
s4=input("Enter the Marks of Student 4: ");
Students.append(s4);
s5=input("Enter the Marks of Student 5: ");
Students.append(s5);
s6=input("Enter the Marks of Student 6: ");
Students.append(s6);
Students.sort()
print("[bold purple]Sorted Marks:[/bold purple]", Students)
