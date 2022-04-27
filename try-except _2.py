try:
    numerator =int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by:  "))
    result = numerator/denominator

except ZeroDivisionError as e:
    print("you can not divide by zero!")
    print(e)
except ValueError as e:
    print("enter only numbers pls")
    print(e)
except Exception as e:
    print("something went wrong")
    print(e)
else:
    print(result)
finally:
    print("this will always execute")