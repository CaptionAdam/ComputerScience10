#Python rectangle size finder
print("Hello there how wide is your Rectange? \n(In cm)")
lenght=input()
print("Ok, How tall is the Rectangle? \n(In cm)")
hight=input()
print("One Moment Please \nPRESS ENTER")
input()
area = int(lenght) * int(hight)
parimiter = int(lenght) + int(hight) * 2
#int(parimiter) * 2
print("Your Rectangle")
print("Has a width of", lenght,"(cm) wide")
print("Has a hight of", hight,"(cm)tall")
print("Has an area =",area,"(cm^2)")
print("has a parimiter =",parimiter,"(cm)")