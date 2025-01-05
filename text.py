def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    print("Temperature Converter")
    print("Enter the temperature value and its unit (C, F, K):")

    try:
        temperature = float(input("Temperature value: "))
        unit = input("Unit (C/F/K): ").strip().upper()

        if unit == "C":
            fahrenheit = celsius_to_fahrenheit(temperature)
            kelvin = celsius_to_kelvin(temperature)
            print(f"{temperature} °C = {fahrenheit:.2f} °F")
            print(f"{temperature} °C = {kelvin:.2f} K")

        elif unit == "F":
            celsius = fahrenheit_to_celsius(temperature)
            kelvin = fahrenheit_to_kelvin(temperature)
            print(f"{temperature} °F = {celsius:.2f} °C")
            print(f"{temperature} °F = {kelvin:.2f} K")

        elif unit == "K":
            celsius = kelvin_to_celsius(temperature)
            fahrenheit = kelvin_to_fahrenheit(temperature)
            print(f"{temperature} K = {celsius:.2f} °C")
            print(f"{temperature} K = {fahrenheit:.2f} °F")

        else:
            print("Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")

    except ValueError:
        print("Invalid input. Please enter a numerical value for the temperature.")

if __name__ == "__main__":
    main()
