mod:"(1, 99)"
A = int(input("Enter a number between 1 and 99: "))
if 1 <= A <= 99:
    reversed_number = 0
    while A > 0:
        digit = A % 10
        reversed_number = reversed_number * 10 + digit
        A = A // 10
    print("Reversed number:", reversed_number)
    
else:
    print("The number is out of the allowed range.")