'''
This file contains the Ingredient class.
'''
class Ingredient:
    def __init__(self):
        self.name = ""
        self.quantity = ""
        self.unit = ""
    def set_name(self, name):
        self.name = name
    def set_quantity(self, quantity):
        self.quantity = quantity
    def set_unit(self, unit):
        self.unit = unit
    def get_name(self):
        return self.name
    def get_quantity(self):
        return self.quantity
    def get_unit(self):
        return self.unit