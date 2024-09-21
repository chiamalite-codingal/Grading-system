s1 = int(input("Enter marks:"))
s2 = int(input("Enter marks:"))
s3 = int(input("Enter marks:"))
s4 = int(input("Enter marks:"))
s5 = int(input("Enter marks:"))
total = s1+s2+s3+s4+s5
avg = total/5
if avg>=80 and avg<=90:
    print("A grade")
elif avg>=70 and avg<=80:
    print("B grade")
elif avg>=60 and avg<=70:
    print("C grade")
elif avg>=50 and avg<=30:
    print("D grade")
else:
    print("E grade-fail")
