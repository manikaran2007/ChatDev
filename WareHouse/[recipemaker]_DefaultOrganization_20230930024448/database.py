'''
This file contains the Database class.
'''
class Database:
    def __init__(self):
        self.ingredients = []
        self.recipes = []
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
    def get_ingredients(self):
        return self.ingredients
    def get_recipes(self):
        return self.recipes