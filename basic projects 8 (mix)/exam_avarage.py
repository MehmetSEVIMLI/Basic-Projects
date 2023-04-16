exam_1st=float(input("1st exam grade : "))
exam_2nd=float(input("2nd exam grade : "))

grade_average=(exam_1st+exam_2nd)/2

if grade_average<50:
    print("Failed")
else:
    print("Pass")