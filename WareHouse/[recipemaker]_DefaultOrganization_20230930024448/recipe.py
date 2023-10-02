'''
This file contains the Recipe class.
'''
class Recipe:
    def __init__(self):
        self.name = ""
        self.ingredients = []
        self.instructions = ""
    def set_name(self, name):
        self.name = name
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    def set_instructions(self, instructions):
        self.instructions = instructions
    def get_name(self):
        return self.name
    def get_ingredients(self):
        return self.ingredients
    def get_instructions(self):
        return self.instructions