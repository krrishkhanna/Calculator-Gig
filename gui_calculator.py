import tkinter as tk
from tkinter import ttk, messagebox
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        # self.root.geometry("400x600") # Adjusted for more buttons
        self.root.resizable(False, False)

        self.current_expression = ""
        self.history_list = []

        # --- Styles ---
        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12), padding=10)
        style.configure("Display.TLabel", font=('Helvetica', 24, 'bold'), anchor='e', padding=(0, 5, 5, 5), background='white', borderwidth=2, relief='sunken')
        style.configure("History.TLabel", font=('Helvetica', 10), anchor='w', padding=2)
        style.configure("HistoryFrame.TFrame", background='lightgrey')

        # --- Display Frame (Current Expression & Result) ---
        display_frame = ttk.Frame(root, relief='sunken', borderwidth=2)
        display_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.display_var = tk.StringVar()
        display_label = ttk.Label(display_frame, textvariable=self.display_var, style="Display.TLabel", width=25) # Increased width
        display_label.pack(fill=tk.X, expand=True)

        # --- History Frame ---
        history_outer_frame = ttk.Frame(root, height=100, relief='groove', borderwidth=1)
        history_outer_frame.pack(fill=tk.X, padx=5, pady=5)
        history_outer_frame.pack_propagate(False) # Prevent resizing based on content

        history_canvas = tk.Canvas(history_outer_frame, background='lightgrey')
        history_scrollbar = ttk.Scrollbar(history_outer_frame, orient="vertical", command=history_canvas.yview)
        self.history_frame_inner = ttk.Frame(history_canvas, style="HistoryFrame.TFrame")

        self.history_frame_inner.bind(
            "<Configure>",
            lambda e: history_canvas.configure(
                scrollregion=history_canvas.bbox("all")
            )
        )

        history_canvas.create_window((0, 0), window=self.history_frame_inner, anchor="nw")
        history_canvas.configure(yscrollcommand=history_scrollbar.set)

        history_canvas.pack(side="left", fill="both", expand=True)
        history_scrollbar.pack(side="right", fill="y")
        
        self.update_history_display() # Initial empty history

        # --- Buttons Frame ---
        buttons_frame = ttk.Frame(root)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Button layout: (text, function, row, col, columnspan, rowspan, style)
        buttons = [
            ("C", lambda: self.clear_entry(), 0, 0), 
            ("CE", lambda: self.clear_all(), 0, 1),
            ("√", lambda: self.apply_func("math.sqrt("), 0, 2),
            ("/", lambda: self.append_operator("/"), 0, 3),

            ("7", lambda: self.append_operator("7"), 1, 0), 
            ("8", lambda: self.append_operator("8"), 1, 1),
            ("9", lambda: self.append_operator("9"), 1, 2), 
            ("*", lambda: self.append_operator("*"), 1, 3),

            ("4", lambda: self.append_operator("4"), 2, 0), 
            ("5", lambda: self.append_operator("5"), 2, 1),
            ("6", lambda: self.append_operator("6"), 2, 2), 
            ("-", lambda: self.append_operator("-"), 2, 3),

            ("1", lambda: self.append_operator("1"), 3, 0), 
            ("2", lambda: self.append_operator("2"), 3, 1),
            ("3", lambda: self.append_operator("3"), 3, 2), 
            ("+", lambda: self.append_operator("+"), 3, 3),

            ("0", lambda: self.append_operator("0"), 4, 0, 2), 
            (".", lambda: self.append_operator("."), 4, 2),
            ("=", lambda: self.calculate_result(), 4, 3, 1, 2, "Accent.TButton"), # Accent button style for '='
            
            # Scientific Functions
            ("xʸ", lambda: self.append_operator("**"), 0, 4),
            ("log₁₀", lambda: self.apply_func("math.log10("), 1, 4),
            ("sin", lambda: self.apply_func("math.sin(math.radians("), 2, 4), # Assuming degree input
            ("cos", lambda: self.apply_func("math.cos(math.radians("), 3, 4),
            ("tan", lambda: self.apply_func("math.tan(math.radians("), 4, 4)
        ]
        
        style.configure("Accent.TButton", font=('Helvetica', 12, 'bold'), background='orange')


        for i in range(5): # 5 rows for buttons
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(5): # 5 columns
            buttons_frame.grid_columnconfigure(i, weight=1)

        for btn_info in buttons:
            text, cmd, r, c = btn_info[0], btn_info[1], btn_info[2], btn_info[3]
            cs = btn_info[4] if len(btn_info) > 4 else 1
            rs = btn_info[5] if len(btn_info) > 5 else 1
            btn_style = btn_info[6] if len(btn_info) > 6 else "TButton"
            
            button = ttk.Button(buttons_frame, text=text, command=cmd, style=btn_style)
            button.grid(row=r, column=c, columnspan=cs, rowspan=rs, sticky="nsew", padx=2, pady=2)

        self.update_display_text("0") # Initial display

    def update_display_text(self, text):
        self.display_var.set(text[:25]) # Limit display length

    def append_operator(self, op):
        if self.current_expression == "0" and op not in ["."]: # Avoid leading zeros unless it's for a decimal
            self.current_expression = ""
        
        # Prevent multiple operators or leading operators (simple check)
        if op in ["+", "-", "*", "/", "**"] and (not self.current_expression or self.current_expression[-1] in ["+", "-", "*", "/", "**"]):
            if op == "-" and (not self.current_expression or self.current_expression[-1] in ["*", "/", "**", "+"]): # Allow negative numbers after operators
                 self.current_expression += op
            elif not self.current_expression and op == "-": # Allow leading negative
                 self.current_expression += op
            else:
                return # Don't add if invalid sequence

        self.current_expression += str(op)
        self.update_display_text(self.current_expression)

    def apply_func(self, func_str):
        # If there's an existing expression that's a number, wrap it. Otherwise, just start the func
        if self.current_expression and self.current_expression[-1].isdigit() or self.current_expression.endswith(")"):
            self.current_expression = func_str + self.current_expression + ")"
        else: # Start new expression with the function
             self.current_expression = func_str
        self.update_display_text(self.current_expression)


    def clear_entry(self):
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            if not self.current_expression:
                self.update_display_text("0")
            else:
                self.update_display_text(self.current_expression)
        else:
            self.update_display_text("0")

    def clear_all(self):
        self.current_expression = ""
        self.update_display_text("0")
        # Optionally clear history:
        # self.history_list = []
        # self.update_history_display()


    def calculate_result(self):
        if not self.current_expression:
            return
        
        # Sanitize for eval: basic check, more robust parsing might be needed for true security
        expression_to_eval = self.current_expression
        # Convert trig functions if they expect degrees but math lib uses radians
        # This is handled by appending math.radians() in apply_func
        
        try:
            result = eval(expression_to_eval)
            history_entry = f"{self.current_expression} = {result}"
            self.history_list.append(history_entry)
            if len(self.history_list) > 20: # Limit history size
                self.history_list.pop(0)
            
            self.update_history_display()
            self.update_display_text(str(result))
            self.current_expression = str(result) # Start new expression with the result
        except ZeroDivisionError:
            self.update_display_text("Error: Div by 0")
            self.current_expression = ""
        except SyntaxError:
            self.update_display_text("Error: Syntax")
            self.current_expression = ""
        except Exception as e:
            self.update_display_text("Error")
            print(f"Calculation error: {e}") # Log detailed error
            self.current_expression = ""

    def update_history_display(self):
        # Clear existing history labels
        for widget in self.history_frame_inner.winfo_children():
            widget.destroy()
        
        # Add new history labels (reversed, newest first)
        if not self.history_list:
            ttk.Label(self.history_frame_inner, text="Calculation history appears here...", style="History.TLabel", foreground="grey").pack(anchor="w", fill=tk.X)
        else:
            for item in reversed(self.history_list):
                ttk.Label(self.history_frame_inner, text=item, style="History.TLabel").pack(anchor="w", fill=tk.X)
        
        # Force canvas update for scrollregion
        self.history_frame_inner.update_idletasks() 
        self.history_frame_inner.master.configure(scrollregion=self.history_frame_inner.master.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop() 