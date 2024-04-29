import random

def generate_unique_number():
    predefined_numbers = set(range(10000, 100000))  # Set of 5-digit numbers
    unique_number = random.sample(list(predefined_numbers), 1)[0]
    return unique_number

# Example usage
if __name__ == "__main__":
    unique_number = generate_unique_number()
    print(f"Generated Unique Number: {unique_number}")

