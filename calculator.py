import re

def calculate_expression(expression):
    # Validate the expression to allow only numbers, operators, parentheses, and spaces
    if not re.match(r"^[0-9+\\-*/().\\s]*$", expression):
        return "Error: Invalid characters in expression."
    
    # Prevent empty or only whitespace expressions
    if not expression.strip():
        return "Error: Expression cannot be empty."

    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."
    except SyntaxError:
        return "Error: Invalid expression syntax. Ensure operators and parentheses are used correctly."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def main():
    print("\nAdvanced Calculator")
    print("Enter a mathematical expression (e.g., '10 + 2 * (5 - 3)') or type 'exit' to quit.")
    
    while True:
        expression = input("> ").strip()
        if expression.lower() == 'exit':
            print("Exiting Calculator. Goodbye!")
            break
        
        if not expression: # Handle empty input after strip
            continue
            
        result = calculate_expression(expression)
        print(result)

if __name__ == "__main__":
    main() 