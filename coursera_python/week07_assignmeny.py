largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        i = int(num)
        if largest is None :
            largest = i
        if smallest is None :
            smallest = i
        if i > largest :
            largest = i
        if i < smallest :
            smallest = i
    except:
        if num == 'done':
            break
        print(num, "Invalid Input")

print("Maximum is", largest)
print("Minimum is", smallest)
