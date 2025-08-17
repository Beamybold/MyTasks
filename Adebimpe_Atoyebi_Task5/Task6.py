week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(week)
person = ("John", 25, "Nigeria")
name, age, country = person

Months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(Months)
print("Kindly enter your details")
name = input("enter your name: ")
gender = input("enter your gender: ")
currentMonthNumber = int(input("enter your current month no: "))
currentDayNumber = int(input("enter your current day number: "))
print(f"Name: \t\t{name}\nGender:\t\t{gender}\nCurrent Month\t({Months[currentMonthNumber -1]}\nCurrent Day\t{week[currentDayNumber -1]}")














