#Python rectangle size finder
print("Hello there how wide is your Rectange? \n(In mm)")
lenght=input()
print("Ok, How tall is the Rectangle? \n(In mm)")
hight=input()
print("One Moment Please \nPRESS ENTER")
input()
area = int(lenght) * int(hight)
perimeter = int(lenght) + int(hight) * 2
#int(parimiter) * 2
print("Your Rectangle")
print(f"Has a width of {lenght}(mm) wide")
print(f"Has a hight of {hight}(mm)tall")
print(f"Has an area = {area}(mm^2)")
print(f"has a perimeter = {perimeter}(mm)")