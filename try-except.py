try:
    num = int(input('type a number please:  '))

    if num > 0 and num % 2 == 0:
        print(f'your number "{num}" is positive-even number ')
    elif num > 0 and num % 2 != 0:
        print(f'your number "{num}" is positive-odd number ')
    elif num < 0 and num % 2 == 0:
        print(f'your number "{num}" is negative-even number ')
    elif num < 0 and num % 2 != 0:
        print(f'your number "{num}" is negative-odd number ')
    else:
        print('Zero is an even number but can\'t say positive or negative number.')




except ValueError:
    print("that was not a number")