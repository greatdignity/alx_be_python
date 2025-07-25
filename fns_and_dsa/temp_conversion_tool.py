# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("=== Temperature Conversion Tool ===")
    temp_input = input["Enter the temperature to convert):"]
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted:.2f}°F")
    elif unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
