class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Bind keyboard events
        self.view.bind('<Key>', self.on_key_press)
        self.view.display.bind('<Return>', lambda e: self.on_button_click('='))
        
    def on_button_click(self, button_text):
        current = self.model.current_value
        
        try:
            if button_text in '0123456789':
                if current == '0' or current in ['True', 'False']:
                    self.model.current_value = button_text
                else:
                    self.model.current_value += button_text
                self.view.update_display(self.model.current_value)
                
            elif button_text == '.':
                if '.' not in current and current not in ['True', 'False']:
                    self.model.current_value += '.'
                    self.view.update_display(self.model.current_value)
            
            elif button_text == 'C':
                self.model.reset()
                self.view.update_display(self.model.current_value)
            
            elif button_text in '+-*/':
                if self.model.operation is None:
                    self.model.previous_value = self.model.current_value
                    self.model.current_value = '0'
                else:
                    self.model.perform_calculation()
                self.model.operation = button_text
                self.view.update_display(self.model.current_value)
            
            elif button_text == '=':
                result = self.model.perform_calculation()
                self.view.update_display(result)
                self.model.operation = None
            
            elif button_text == 'M+':
                success = self.model.add_to_memory()
                if not success:
                    self.view.show_error("Valor no válido para memoria")
            
            elif button_text == 'Avg':
                result = self.model.calculate_average()
                self.view.update_display(result)
            
            elif button_text == 'Bin':
                result = self.model.to_binary()
                self.view.update_display(result)
            
            elif button_text == 'Primo':
                result = self.model.check_prime()
                self.view.update_display(result)
            
            elif button_text == 'Data':
                history = self.model.get_history()
                self.view.show_history(history)
        
        except Exception as e:
            self.view.show_error(f"Error: {str(e)}")
            self.model.reset()
            self.view.update_display('0')
    
    def on_key_press(self, event):
        key = event.char
        if key in '0123456789':
            self.on_button_click(key)
        elif key in '+-*/':
            self.on_button_click(key)
        elif key == '.':
            self.on_button_click('.')
        elif key == '\x08':  # Backspace
            self.on_button_click('C')
        elif key == '\r':  # Enter
            self.on_button_click('=')
    
    def on_close(self):
        self.view.destroy()