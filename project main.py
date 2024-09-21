s1 = int(input("Enter marks:"))
s2 = int(input("Enter marks:"))
s3 = int(input("Enter marks:"))
s4 = int(input("Enter marks:"))
s5 = int(input("Enter marks:"))
total = s1+s2+s3+s4+s5
avg = total/5
if avg>=91 and avg<=100:
    print("A grade")
elif avg>=81 and avg<=91:
    print("B grade")
elif avg>=71 and avg<=81:
    print("C grade")
elif avg>=61 and avg<=41:
    print("D grade")
else:
    print("E grade-fail")
