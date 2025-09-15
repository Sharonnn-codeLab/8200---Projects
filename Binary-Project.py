
def process_number():
    while True:
        try:
            Decimal_number = int(input("Enter a decimal number: "))
            if Decimal_number>0:
                break
        except ValueError:
            print("Only positive can be written.")

    while True:
        try:
            Memory_size = int(input("Enter the memory size: "))
            break
        except ValueError:
            print("Only numbers can enterd!")

    Binary_inverted = (~Decimal_number +1) & (2**Memory_size-1)
    Binary_number = format(Binary_inverted, f'0{Memory_size}b')

    print(f"The decimal number: {Decimal_number}, The memory size: {Memory_size}\nAfter inverted: {Binary_number}")

process_number()