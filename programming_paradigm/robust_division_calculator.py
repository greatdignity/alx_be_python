def safe_divide(numerator,denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please provide numeric values only."


print(safe_divide(10,2))
print(safe_divide(10,0))
print(safe_divide("seven","2"))