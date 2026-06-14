#!/usr/bin/env python3
"""
GUI Calculator using tkinter
A graphical interface for basic arithmetic operations
"""

import tkinter as tk
from tkinter import font

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Variable to store the expression
        self.expression = ""
        
        # Create GUI elements
        self.create_display()
        self.create_buttons()
    
    def create_display(self):
        """Create the display screen"""
        # Create a frame for the display
        display_frame = tk.Frame(self.root, bg="#34495e")
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        # Create the display entry
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 24, "bold"),
            borderwidth=2,
            relief=tk.SUNKEN,
            justify=tk.RIGHT,
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        self.display.pack(fill=tk.BOTH, ipady=20, padx=5, pady=5)
    
    def create_buttons(self):
        """Create all calculator buttons"""
        # Create button frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Define button layout
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('÷', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('×', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('−', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
            ('C', 4, 0), ('←', 4, 1), ('√', 4, 2), ('%', 4, 3),
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            self.create_button(button_frame, text, row, col)
    
    def create_button(self, parent, text, row, col):
        """Create individual button with styling"""
        button_font = font.Font(family="Arial", size=14, weight="bold")
        
        # Different colors for different button types
        if text == "=":
            bg_color = "#27ae60"
            fg_color = "white"
            hover_color = "#229954"
        elif text == "C":
            bg_color = "#e74c3c"
            fg_color = "white"
            hover_color = "#c0392b"
        elif text in ("÷", "×", "−", "+"):
            bg_color = "#3498db"
            fg_color = "white"
            hover_color = "#2980b9"
        else:
            bg_color = "#95a5a6"
            fg_color = "#2c3e50"
            hover_color = "#7f8c8d"
        
        button = tk.Button(
            parent,
            text=text,
            font=button_font,
            bg=bg_color,
            fg=fg_color,
            activebackground=hover_color,
            activeforeground="white",
            border=0,
            cursor="hand2",
            command=lambda: self.on_button_click(text)
        )
        
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", ipady=20)
        
        # Configure grid weights for uniform sizing
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char == "C":
            self.expression = ""
            self.update_display()
        elif char == "←":
            self.expression = self.expression[:-1]
            self.update_display()
        elif char == "=":
            self.calculate()
        elif char == "√":
            self.sqrt()
        elif char == "%":
            self.percentage()
        else:
            # Convert symbols to operators
            if char == "÷":
                char = "/"
            elif char == "×":
                char = "*"
            elif char == "−":
                char = "-"
            
            self.expression += str(char)
            self.update_display()
    
    def update_display(self):
        """Update the display screen"""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
    
    def calculate(self):
        """Perform the calculation"""
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.update_display()
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""
    
    def sqrt(self):
        """Calculate square root"""
        try:
            result = float(self.expression) ** 0.5
            self.expression = str(result)
            self.update_display()
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""
    
    def percentage(self):
        """Calculate percentage"""
        try:
            result = float(self.expression) / 100
            self.expression = str(result)
            self.update_display()
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""


def main():
    """Main function to run the calculator"""
    root = tk.Tk()
    calc = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
