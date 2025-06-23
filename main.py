from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

def main():
    model = CalculatorModel()
    view = CalculatorView(None)  # Temporary None before controller exists
    controller = CalculatorController(model, view)
    view.controller = controller  # Now set the controller
    view.mainloop()

if __name__ == "__main__":
    main()