color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i, x in enumerate(color):
    print(i, x)
    if i not in (0, 4, 5):
        print(color)
color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]
print(color)

