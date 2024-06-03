class Calculator:
   
    def add(a: int, b: int) -> int:
        return a + b

   
    def subtract(a: int, b: int) -> int:
        return a - b

    
    def divide(a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    
    def multiply(a: int, b: int) -> int:
        return a * b

def main():
    calc = Calculator()

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in {'1', '2', '3', '4'}:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                if choice == '1':
                    print(f"The result is: {calc.add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {calc.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {calc.multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {calc.divide(num1, num2)}")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
