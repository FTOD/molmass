from core import MassDataBase, Calculator

with open('mass_data_base.json') as f:
    database = MassDataBase()
    database.load_from_json(f)
calculator = Calculator(database)
mass = calculator.calculate("CH4")
print(mass)
