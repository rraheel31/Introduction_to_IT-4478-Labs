#Write a python program to convert minutes into hours and minutes
#print both minutes and hours

Total_minutes = int(input("Enter the total minutes: "))
hours = Total_minutes // 60
minutes = Total_minutes % 60
print(f"{Total_minutes} minutes is equal to {hours} hours and {minutes} minutes.")