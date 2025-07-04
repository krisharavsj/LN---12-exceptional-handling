def get_age():
    while True:
        try:
            s = input("Enter your age").strip()
            age = float(s)
            return age
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g. 45 or 67.2).")

def analyze_age(age):
    # Unusual if decimal part non-zero
    if age != int(age):
        print(f"Unusual age detected: {age} (contains decimal part)")
    else:
        age_int = int(age)
        if age_int < 0 or age_int > 150:
            print(f"That age ({age_int}) seems out of realistic range.")
        else:
            # Even/odd only makes sense for integers :contentReference[oaicite:8]{index=8}
            if age_int % 2 == 0:
                print(f"{age_int} is even.")
            else:
                print(f"{age_int} is odd.")

def main():
    age = get_age()
    analyze_age(age)

if __name__ == "__main__":
    main()
