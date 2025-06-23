from Model.model import CalculatorModel
from View.view import CalculatorView
from Controller.controller import CalculatorController

def main():
    model = CalculatorModel()
    view = CalculatorView(None)  # Temporary None before controller exists
    controller = CalculatorController(model, view)
    view.controller = controller  # Now set the controller
    view.mainloop()

if __name__ == "__main__":
    main()