# Program to print whether a given character is an uppercase, loercase, digit aor anu other character

ch = input("Enter a single character: ")

if ch >= 'A' and ch <= 'Z':
    print("You have entered an uppercase character.")
elif ch >= 'a' and ch <= 'z':
    print("You have entered a lowercase character.")
elif ch >= '0' and ch <= '9':
    print("You have entered a digit.")
else:
    print("You have entered a special character.")