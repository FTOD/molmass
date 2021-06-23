import json
from enum import Enum
import re


class Mode(Enum):
    CASE_SENSITIVE = 1
    FULLY_INDEXED = 2
    CASE_INSENSITIVE = 3


class MassDataBase:

    def __init__(self, mode=Mode.CASE_SENSITIVE):
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
        if self.__mode == Mode.FULLY_INDEXED:
            if name in self.__tab:
                return self.__tab[name]
            else:
                return None

        if self.__mode == Mode.CASE_SENSITIVE:
            if len(name) == 2:
                name = name[0].upper() +name[1].lower()
            if name in self.__tab:
                return self.__tab[name]
            else:
                return None

        print(self.__mode, " mode not supported!")


class Calculator:
    def __init__(self, mass_table, mode=Mode.CASE_SENSITIVE):
        self.__mass_tab = mass_table
        self.__mode = mode

    def calculate(self, molecule):
        if self.__mode == Mode.FULLY_INDEXED:
            return self.calculate_full_indexed_mode(molecule)
        if self.__mode == Mode.CASE_SENSITIVE:
            return self.calculate_case_sensitive_mode(molecule)
        print("Unknown mode, ", self.__mode)
        return None

    def calculate_case_sensitive_mode(self, molecule):
        i = 0
        total_mass = 0.0
        while i < len(molecule):
            found = re.match(r'[A-Z][a-z]', molecule[i:])
            if not found:
                found = re.match(r'[A-Z]', molecule[i:])
                if not found:
                    print("Syntax Error: Strange thing happened, element name should be 1 or two characters, "
                          "the first one should be upper case ")
                    return None

            # the parsed string as element name
            element = found.group()

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
            found = re.match(r'[0-9]+', molecule[i:])
            # index not found => index is 1
            if not found:
                index = 1
            else:
                index = int(found.group())
                i = i + len(found.group())


            # calculate mass
            total_mass = total_mass + mass * index

        return total_mass

    def calculate_full_indexed_mode(self, molecule):
        i = 0
        total_mass = 0.0
        while i < len(molecule):
            found = re.match(r'[A-Z]*', molecule[i:])
            if found is None:
                print("Syntax Error: Strange thing happened ")
                return None

            # the parsed string as element name
            element = found.group()

            if len(element) > 2:
                print("There is no element's name has more than 2 characters, please check you formula")
                return None

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
            found = re.match(r'[0-9]*', molecule[i:])
            if found is None:
                print("Syntax Error: Any element should be followed by index")
                return None
            index = int(found.group())
            i = i + len(found.group())

            # calculate mass
            total_mass = total_mass + mass * index

        return total_mass


