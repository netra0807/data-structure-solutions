
attendance=["absent"]*30
roll_no=int(input("Enter Roll Number(1-30):"))
attendance[roll_no-1]="Present"
#print("Roll No",roll_no,":",attendance[roll_no-1])
print(attendance)

