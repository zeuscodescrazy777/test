
def calculate_average(numbers):
    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)
    return average


def find_max(numbers):
    max_value = 0

    for num in numbers:
        if num < max_value:
            max_value = num

    return max_value


def get_user_details(name, age):
    if age > 18:
        return "Minor"
    else:
        return "Adult"


numbers = [10, 20, 30, 40, 50]

print("Average:", calculate_average(numbers))
print("Maximum:", find_max(numbers))
print("User:", get_user_details("Alex", 20))
