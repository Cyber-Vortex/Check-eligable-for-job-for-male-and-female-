gender=input("Enter'M' for male and 'F' for Female=")
age=int(input("Enter your age"))
if gender=="F":
    if 18<=age<=28:
        print("You are eligible for job ")
    else:
        print("You are not eligible")
else:
    if 18<=age<=26:
        print("You are eligible for job")
    else:
        print("You are not eligible")
