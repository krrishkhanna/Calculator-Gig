# Advanced GUI Calculator and Simple CLI Calculator

This project contains two calculator implementations:
1.  An **Advanced GUI Calculator** (`gui_calculator.py`) with scientific functions and history.
2.  A **Simple Command-Line Expression Calculator** (`calculator.py`).

## 1. Advanced GUI Calculator (`gui_calculator.py`)

This is a desktop calculator application built with Python and Tkinter, providing a feature-rich graphical user interface.

### Features

- **Graphical User Interface (GUI)**: Interactive interface with themed buttons and clear displays.
- **Standard Operations**: Buttons for numbers `0-9`, decimal point `.`, addition `+`, subtraction `-`, multiplication `*`, division `/`.
- **Scientific Functions**:
    - Square Root (`√`)
    - Power (`xʸ` represented as `**`)
    - Logarithm base 10 (`log₁₀`)
    - Trigonometric functions: `sin`, `cos`, `tan` (input assumed in degrees, converted to radians for calculation).
- **Calculation History**: A scrollable panel displaying a list of recent calculations.
- **Input and Result Display**: A large, clear display for the current expression and results.
- **Controls**: 
    - `C`: Clear last entry/character.
    - `CE`: Clear entire current expression (resets to "0").
    - `=`: Evaluate the expression.
- **Error Handling**: Displays user-friendly messages like "Error: Div by 0" or "Error: Syntax" on the calculator screen for invalid operations.
- **Responsive Layout**: Buttons and displays are arranged for ease of use.

### How to Run the GUI Calculator

1.  Ensure you have Python installed (Tkinter is usually included).
2.  Navigate to the `simple-calculator` directory in your terminal.
3.  Run the application:
    ```bash
    python gui_calculator.py
    ```
4.  The calculator window will appear. Use the buttons to perform calculations.

### Screenshot Placeholder

(A screenshot of the GUI calculator in action would be placed here.)

```
-------------------------------------------
| Advanced Calculator                     |
|-----------------------------------------|
| [ Display: 123+sin(math.radians(45)) ]  |
|-----------------------------------------|
| [ History Scrollable Area:          ]   |
| [ 10+5 = 15                         ]   |
| [ 15*2 = 30                         ]   |
| [ ...                               ]   |
|-----------------------------------------|
| [ C ][CE][ √ ][ / ][ xʸ ]             |
| [ 7 ][ 8 ][ 9 ][ * ][log₁₀]             |
| [ 4 ][ 5 ][ 6 ][ - ][ sin ]             |
| [ 1 ][ 2 ][ 3 ][ + ][ cos ]             |
| [   0   ][ . ][ = ][ tan ]             |
-------------------------------------------
```

## 2. Simple Command-Line Expression Calculator (`calculator.py`)

This is a command-line calculator built in Python that can evaluate mathematical expressions entered as strings.

### Features

- Evaluates expressions involving: 
    - Addition (`+`)
    - Subtraction (`-`)
    - Multiplication (`*`)
    - Division (`/`)
    - Parentheses `()` for grouping
- Respects operator precedence.
- Basic input validation for allowed characters and error handling for invalid syntax or division by zero.

### How to Run the CLI Calculator

1.  Ensure you have Python installed.
2.  Navigate to the `simple-calculator` directory in your terminal.
3.  Run the calculator:
    ```bash
    python calculator.py
    ```
4.  Enter expressions at the prompt (e.g., `10 + 2 * (5 - 3)`).

### CLI Example

```
Advanced Calculator
Enter a mathematical expression (e.g., '10 + 2 * (5 - 3)') or type 'exit' to quit.
> 10 + 2 * (5 - 3)
14
> exit
Exiting Calculator. Goodbye!
```

## Dependencies (for both)

- Python 3.x
- Tkinter (for `gui_calculator.py`, usually comes with Python)
- `math` module (for scientific functions in `gui_calculator.py`, standard library)

**Note on `eval()`**: This calculator uses Python's built-in `eval()` function to parse and compute expressions. While input is validated to allow only numbers and basic mathematical operators/symbols, using `eval()` on un-sanitized input from untrusted sources can be a security risk. For this project's scope (a simple, local calculator), it's a straightforward way to achieve expression evaluation. 