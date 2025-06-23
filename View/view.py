import tkinter as tk
from tkinter import messagebox, simpledialog

class CalculatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Calculadora MVC")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg='#f0f0f0')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.display = tk.Entry(
            self, textvariable=self.display_var, font=('Arial', 24), 
            bd=10, insertwidth=2, width=14, borderwidth=4, justify='right'
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('M+', 5, 1), ('Avg', 5, 2), ('Bin', 5, 3),
            ('Primo', 6, 0), ('Data', 6, 1)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            button = tk.Button(
                self, text=text, padx=20, pady=20, font=('Arial', 18),
                command=lambda t=text: self.controller.on_button_click(t)
            )
            button.grid(row=row, column=col, sticky='nsew')
        
        # Configure grid weights
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
    
    def update_display(self, value):
        self.display_var.set(value)
    
    def show_history(self, history):
        history_window = tk.Toplevel(self)
        history_window.title("Bitácora de Operaciones")
        history_window.geometry("500x400")
        
        text = tk.Text(history_window, wrap=tk.WORD)
        text.pack(expand=True, fill='both')
        text.insert(tk.END, history)
        text.config(state='disabled')
        
        scrollbar = tk.Scrollbar(history_window, command=text.yview)
        scrollbar.pack(side='right', fill='y')
        text.config(yscrollcommand=scrollbar.set)
    
    def show_error(self, message):
        messagebox.showerror("Error", message)