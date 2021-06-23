import json
from enum import Enum
import re


class Mode(Enum):
    FREE = 1
    INDEXED = 2


class MassDataBase:

    def __init__(self, mode=Mode.INDEXED):
        if mode not in Mode:
            print("Mode ", mode, " is not supported")
        self.__tab = dict()
        self.__alphabet = []
        self.__mode = mode

    # load from a file
    def load_from_json(self, f):
        data = json.load(f)
        self.__tab = data

    def add_mass(self, name, mass):
        self.__tab[name] = mass

    def find(self, name):
        if self.__mode == Mode.INDEXED:
            if name in self.__tab:
                return self.__tab[name]
            else:
                return None
        else:
            print("FREE mode not supported?")


class Calculator:
    def __init__(self, mass_table, mode=Mode.INDEXED):
        self.__mass_tab = mass_table
        self.__mode = mode

    def calculate(self, molecule):
        if self.__mode == Mode.INDEXED:
            return self.calculate_full_indexed_mode(molecule)
        else:
            print("FREE mode not supported yet")

    def calculate_full_indexed_mode(self, molecule):
        i = 0
        total_mass = 0.0
        while i < len(molecule):
            found = re.search(r'[A-Z]*', molecule[i:])
            if found is None:
                print("Syntax Error: Strange thing happened ")
                return None

            # the parsed string as element name
            element = found.group(0)

            # get the mass if the element in the data base
            mass = self.__mass_tab.find(element)

            # no mass found in the data base
            if mass is None:
                print(element, " is not registered for mass data, please check your data file")
                return None

            # continue
            i = i + len(element)

            # i should get the index here, but i'm out of index => syntax error
            if not i < len(molecule):
                print("Syntax Error: Any element should be followed by index, even the last one")
                return None

            # find the index
            found = re.search(r'[0-9]*', molecule[i:])
            if found is None:
                print("Syntax Error: Any element should be followed by index")
                return None
            index = int(found.group(0))
            i = i + len(found.group(0))

            # calculate mass
            total_mass = total_mass + mass * index

        return total_mass


if __name__ == '__main__':
    with open('mass_data_base.json') as f:
        database = MassDataBase()
        database.load_from_json(f)
    calculator = Calculator(database)
    mass = calculator.calculate("C1H4")
    print(mass)
