start = int(input("Enter the start Date : "))
end = int(input("Enter the end Date : "))
ly = []
l= []
while start < end:
    if start % 4 == 0 or start % 400 ==0:
        ly.append(start)
    else:
        l.append(start)
    start += 1
print("Leap years are:",ly)
print("Not a Leap year:",l)
if start >= end:4
    print("Check your year input again.")

