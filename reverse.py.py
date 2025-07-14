A = int(input("Enter a number between 1 and 999: "))

if A < 1 or A > 999:
    print("The number is out of range (1-999).")
elif A < 10:
    # 1-digit number, same when reversed
    print("Reversed number:", A)
elif A < 100:
    # 2-digit number
    tens = A // 10
    ones = A % 10
    reversed_number = ones * 10 + tens
    print("Reversed number:", reversed_number)
else:
    # 3-digit number
    hundreds = A // 100
    tens = (A % 100) // 10
    ones = A % 10
    reversed_number = ones * 100 + tens * 10 + hundreds
    print("Reversed number:", reversed_number)