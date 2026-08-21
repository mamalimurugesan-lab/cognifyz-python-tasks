# Cognifyz Task 4 - Temperature Converter

print("=" * 45)
print("         TEMPERATURE CONVERTER")
print("=" * 45)

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose conversion (1 or 2): ").strip()

try:
    temperature = float(input("Enter the temperature: "))

    if choice == "1":
        fahrenheit = (temperature * 9 / 5) + 32
        print(f"{temperature:.2f}°C = {fahrenheit:.2f}°F")

    elif choice == "2":
        celsius = (temperature - 32) * 5 / 9
        print(f"{temperature:.2f}°F = {celsius:.2f}°C")

    else:
        print("Invalid choice. Please select 1 or 2.")

except ValueError:
    print("Please enter a valid number.")

print("=" * 45)
