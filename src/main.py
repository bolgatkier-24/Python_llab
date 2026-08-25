from utils import square, is_even, celsius_to_fahrenheit

def main():
    # Prompt the user for a number
    user_input = input("Enter a number: ")
    
    # Convert the input to a float so it handles decimals too
    number = float(user_input)
    
    # Calculate results using the imported functions
    sq = square(number)
    even_status = is_even(number)
    fahrenheit = celsius_to_fahrenheit(number)
    
    # Print the results
    print(f"\n--- Results for {number} ---")
    print(f"Square: {sq}")
    
    # Format the even/odd output nicely
    if even_status:
        print("Even/Odd: Even")
    else:
        print("Even/Odd: Odd")
        
    print(f"Fahrenheit equivalent: {fahrenheit}°F")

if __name__ == "__main__":
    main()

    from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    # Prompt the user for their name and a number
    name = input("Enter your name: ")
    print(greet(name))
    
    user_input = input("Enter a number: ")
    number = float(user_input)
    
    # Calculate results using the imported functions
    sq = square(number)
    even_status = is_even(number)
    fahrenheit = celsius_to_fahrenheit(number)
    
    # Print the results
    print(f"\n--- Results for {number} ---")
    print(f"Square: {sq}")
    
    if even_status:
        print("Even/Odd: Even")
    else:
        print("Even/Odd: Odd")
        
    print(f"Fahrenheit equivalent: {fahrenheit}°F")

if __name__ == "__main__":
    main()