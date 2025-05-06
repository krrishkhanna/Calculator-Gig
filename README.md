# Advanced Calculator

This is a command-line calculator built in Python that can evaluate mathematical expressions.

## Features

- Evaluates expressions involving: 
    - Addition (`+`)
    - Subtraction (`-`)
    - Multiplication (`*`)
    - Division (`/`)
    - Parentheses `()` for grouping
- Respects operator precedence (e.g., `*` and `/` before `+` and `-`).
- Basic input validation and error handling for invalid characters or syntax.

## How to Run

1.  Ensure you have Python installed on your system.
2.  Navigate to the `simple-calculator` directory in your terminal.
3.  Run the calculator using the command:
    ```bash
    python calculator.py
    ```

## Examples of Use

When you run the script, you will be prompted to enter a mathematical expression:

```
Advanced Calculator
Enter a mathematical expression (e.g., '10 + 2 * (5 - 3)') or type 'exit' to quit.
> 10 + 5
15
> 10 + 2 * 6
22
> (10 + 2) * 6
72
> 100 / (5 - 5)
Error! Division by zero.
> 10 + 2 * (5 - 3)
14
> 5 * -2
-10
> 5 / 2 + 1.5
4.0
> five plus ten
Error: Invalid characters in expression.
> 10 + * 5
Error: Invalid expression syntax. Ensure operators and parentheses are used correctly.
> exit
Exiting Calculator. Goodbye!
```

**Note on `eval()`**: This calculator uses Python's built-in `eval()` function to parse and compute expressions. While input is validated to allow only numbers and basic mathematical operators/symbols, using `eval()` on un-sanitized input from untrusted sources can be a security risk. For this project's scope (a simple, local calculator), it's a straightforward way to achieve expression evaluation. 