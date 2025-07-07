import math

def calculate_trigonometric_functions():
    try:
        angle_degrees = float(input("Enter the angle in degrees"))
        angle_radians = math.radians(angle_degrees)

        sin = math.sin(angle_radians)
        cos = math.cos(angle_radians)
        tan = math.tan(angle_radians)

        print(f"\nTrigonometric values for {angle_degrees}")
        print(f"Sine: {sin}")
        print(f"Cosine: {cos}")
        print(f"Tangent: {tan}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the angle")

if __name__ == "__main__":
    calculate_trigonometric_functions()
