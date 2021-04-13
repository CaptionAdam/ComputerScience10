#Python rectangle size finder
print("Hello there how wide is your Rectange? \n(In cm)")
lenght=input()
print("Ok, How tall is the Rectangle? \n(In cm)")
hight=input()
print("One Moment Please \nPRESS ENTER")
input()
area = int(lenght) * int(hight)
perimeter = int(lenght) + int(hight) * 2
#int(parimiter) * 2
print("Your Rectangle")
print(f"Has a width of {lenght}(cm) wide")
print(f"Has a hight of {hight}(cm)tall")
print(f"Has an area = {area}(cm^2)")
print(f"has a perimeter = {perimeter}(cm)")