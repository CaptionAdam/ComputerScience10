#Failed Code Attempt
#print("What Year Is it")
#year=input()
#print("So it is", year, "Already")
#print("Now you want to know when you will turn 100 \nFirst give me your name")
#name=input()
#print("Hello,",name, "\nNow what year were you born")
#birth=input()
#print(year - birth)
#Subtract = int(year) - int(birth)
#print(Subtract)

#Working Code
print("What Year Is it")
year=input()
print("Thank you, now I am able to tell you when you will turn 100 \nSo what is your name again")
name=input()
print("Why hello there",name,"Nice to meet you \nhow old are you if you dont mind me asking")
age=input()
print("So you are",age,"\nNow I will tell you when you will turn 100 \nOne minute please")
birth = int(year) - int(age)
old = int(birth) + 100
print("You will be 100 in the year",old)