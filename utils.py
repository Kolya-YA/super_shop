def ask_int(prompt, max_value=100, min_value=0):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                raise ValueError
            return value
        except ValueError:
            print(f"Invalid input. Please enter an integer between {min_value} and {max_value}.")

def ask_float(prompt, max_value=100, min_value=0):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or value > max_value:
                raise ValueError
            return value
        except ValueError:
            print(f"Invalid input. Please enter a float between {min_value} and {max_value}.")


def ask_str(prompt, min_length=3, max_length=64):
    while True:
        value = input(prompt)
        if len(value) < min_length or len(value) > max_length:
            print(f"Invalid input. Please enter a string between {min_length} and {max_length} characters.")
            continue
        else:
            return value

def separator(length = 30):
    print("—" * length)
