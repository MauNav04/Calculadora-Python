import math
from datetime import datetime

class CalculatorModel:
    def __init__(self):
        self.current_value = '0'
        self.previous_value = None
        self.operation = None
        self.memory = []
        self.MAX_MEMORY = 10
        self.history_file = "Bitacora.txt"
        
    def reset(self):
        self.current_value = '0'
        self.previous_value = None
        self.operation = None
        
    def add_to_history(self, operation, result):
        with open(self.history_file, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {operation} = {result}\n")
    
    def perform_calculation(self):
        if self.operation and self.previous_value is not None:
            try:
                a = float(self.previous_value)
                b = float(self.current_value)
                
                if self.operation == '+':
                    result = a + b
                elif self.operation == '-':
                    result = a - b
                elif self.operation == '*':
                    result = a * b
                elif self.operation == '/':
                    if b == 0:
                        return "Error: División por cero"
                    result = a / b
                
                self.previous_value = str(result)
                self.current_value = str(result)
                self.add_to_history(f"{a} {self.operation} {b}", result)
                return str(result)
            except ValueError:
                return "Error"
        return self.current_value
    
    def add_to_memory(self):
        try:
            value = float(self.current_value)
            if len(self.memory) >= self.MAX_MEMORY:
                self.memory.pop(0)
            self.memory.append(value)
            self.add_to_history(f"M+ {value}", "Memoria actualizada")
            return True
        except ValueError:
            return False
    
    def calculate_average(self):
        if not self.memory:
            return "Error: Memoria vacía"
        avg = sum(self.memory) / len(self.memory)
        self.current_value = str(avg)
        self.add_to_history(f"Avg {' '.join(map(str, self.memory))}", avg)
        return str(avg)
    
    def to_binary(self):
        try:
            num = int(float(self.current_value))
            binary = bin(num)[2:]
            self.current_value = binary
            self.add_to_history(f"Binario {num}", binary)
            return binary
        except ValueError:
            return "Error"
    
    def check_prime(self):
        try:
            num = int(float(self.current_value))
            if num < 2:
                self.current_value = "False"
                self.add_to_history(f"Primo {num}", False)
                return "False"
            
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    self.current_value = "False"
                    self.add_to_history(f"Primo {num}", False)
                    return "False"
            
            self.current_value = "True"
            self.add_to_history(f"Primo {num}", True)
            return "True"
        except ValueError:
            return "Error"
    
    def get_history(self):
        try:
            with open(self.history_file, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "No hay historial disponible"