
radius = float(input("Enter the value for the radius"))

print("Press 1: Calculate Area")
print("Press 2: Calculate Perimeter")

choice = int(input("Enter your choice(1 or 2): "))

if choice == 1:
    area = 3.14 * radius ** 2
    print("Area of the circle is: ", area, "cm-sqaure")
elif choice == 2:
    peri = 2 * 3.14 * radius
    print("Perimeter of the circle is: ", peri, "cm")
else:
    print("Wrong Choice: Please enter the correct choice ")