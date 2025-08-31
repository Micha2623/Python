# Create a simple unit converter that converts between various units (e.g., length, weight, temperature).
# Gradually enhance it by adding a GUI using Tkinter, implementing a history feature to track previous
# conversions, and allowing customizable conversion categories.

print("Welcome to the Unit Converter")
print("Choose a conversion category:")
category = int(input("1. Length, 2. Weight, 3. Temperature"))


def length():
    meter = 1
    cm = 0.01
    inch = 0.0254
    km = 1000
    mile = 1609.34
    print("Lenght Converter")
    base_unit = int(
        input(
            "Chose the base unit: 1. Meter, 2. Centimeter, 3. Inch, 4. Kilometer, 5. Mile"
        )
    )
    conversor_unit = int(
        input(
            "Chose the unit to convert to: 1. Meter, 2. Centimeter, 3. Inch, 4. Kilometer, 5. Mile"
        )
    )
    value = float(input("Enter the value to convert: "))


def weight():
    kg = 1000
    g = 1
    lb = 453.592
    ounce = 28.3495
    print("Weight Converter")


if category == 1:
    print("You chose Length")
    length()
elif category == 2:
    print("You chose Weight")
    weight()
