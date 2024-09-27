while True:
    decimal_num = int(input("decimal: "))
    binary_num = []

    while decimal_num > 0:
        if decimal_num % 2 == 1:
            decimal_num //= 2
            binary_num.append(1)
        else:
            decimal_num //= 2
            binary_num.append(0)

    binary_num.reverse()
    result = ''.join(str(i) for i in binary_num)

    print(f"Binary: {result}")