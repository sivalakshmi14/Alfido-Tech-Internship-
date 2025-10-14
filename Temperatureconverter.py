# Task 3: Temperature Converter

print("=== Temperature Converter ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c}°C")

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    k = c + 273.15
    print(f"{c}°C = {k}K")

elif choice == 4:
    k = float(input("Enter temperature in Kelvin: "))
    c = k - 273.15
    print(f"{k}K = {c}°C")

else:
    print("Invalid choice. Please select a valid option.")
