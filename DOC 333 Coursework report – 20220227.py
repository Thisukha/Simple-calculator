def display_menu():
    print("")
    print("""                                  Wonder Calculator
                                  =================
                                     Main Menu

                              1. Enter positive Integer Numbers
                              2. Display Highest value
                              3. Display Lowest value
                              4. Display Average value
                              5. Display Even Numbers
                              6. Exit  """)

def get_positive_numbers(limit):
    numbers = []
    for _ in range(limit):
        while True:
            try:
                num = int(input("Please input a positive number: "))
                if num >= 0:
                    numbers.append(num)
                    break
                else:
                    print("The number must be positive. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
    return numbers

def display_highest_value(numbers):
    highest_value = max(numbers)
    print("The highest value is =", highest_value)

def display_lowest_value(numbers):
    lowest_value = min(numbers)
    print("The lowest value is =", lowest_value)

def display_average_value(numbers):
    average_value = sum(numbers) / len(numbers)
    print("The average value is =", average_value)

def display_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        print("Even numbers are:", even_numbers)
    else:
        print("There are no even numbers in the list!")

def main():
    display_menu()
    
    option = int(input("Please indicate your option: "))
    while option != 1:
        print("Please enter number 1 to continue.")
        option = int(input("Please indicate your option: "))
    
    num_count = int(input("How many numbers do you want to enter: "))
    while num_count > 10:
        print("Only 10 numbers are allowed.")
        num_count = int(input("How many numbers do you want to enter: "))
    
    numbers = get_positive_numbers(num_count)
    
    while True:
        print("")
        display_menu()
        print("")
        option = int(input("Please select the next option: "))
        
        if option == 2:
            display_highest_value(numbers)
        elif option == 3:
            display_lowest_value(numbers)
        elif option == 4:
            display_average_value(numbers)
        elif option == 5:
            display_even_numbers(numbers)
        elif option == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        
        decision = input("Do you want to continue [y/n]: ").lower()
        if decision != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
