'''
This file contains the UserInterface class.
'''
import tkinter as tk
import os
class UserInterface:
    def __init__(self, recipe, ingredient, database):
        self.recipe = recipe
        self.ingredient = ingredient
        self.database = database
    def start(self):
        # Check if running in a graphical environment
        if os.environ.get("DISPLAY") or os.name == "nt":
            # Create the main window
            self.window = tk.Tk()
            self.window.title("Recipe Maker")
            # Create and pack the GUI elements
            self.create_name_entry()
            self.create_ingredient_entry()
            self.create_instructions_entry()
            self.create_save_button()
            self.create_share_button()
            # Start the main event loop
            self.window.mainloop()
        else:
            print("Error: This application requires a graphical display to run.")
    def create_name_entry(self):
        self.name_label = tk.Label(self.window, text="Recipe Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()
    def create_ingredient_entry(self):
        self.ingredient_label = tk.Label(self.window, text="Ingredients:")
        self.ingredient_label.pack()
        self.ingredient_entry = tk.Text(self.window, height=10, width=50)
        self.ingredient_entry.pack()
    def create_instructions_entry(self):
        self.instructions_label = tk.Label(self.window, text="Instructions:")
        self.instructions_label.pack()
        self.instructions_entry = tk.Text(self.window, height=10, width=50)
        self.instructions_entry.pack()
    def create_save_button(self):
        self.save_button = tk.Button(self.window, text="Save Recipe", command=self.save_recipe)
        self.save_button.pack()
    def create_share_button(self):
        self.share_button = tk.Button(self.window, text="Share Recipe", command=self.share_recipe)
        self.share_button.pack()
    def save_recipe(self):
        name = self.name_entry.get()
        if name.strip() == "":
            # Display an error message to the user
            error_message = "Please enter a recipe name."
            error_label = tk.Label(self.window, text=error_message, fg="red")
            error_label.pack()
            return
        ingredients = self.ingredient_entry.get("1.0", tk.END)
        instructions = self.instructions_entry.get("1.0", tk.END)
        # Create a new recipe object
        recipe = Recipe()
        recipe.set_name(name)
        recipe.set_instructions(instructions)
        # Split the ingredients by line and create ingredient objects
        ingredient_lines = ingredients.split("\n")
        for line in ingredient_lines:
            if line.strip() != "":
                ingredient = Ingredient()
                ingredient.set_name(line)
                recipe.add_ingredient(ingredient)
        # Add the recipe to the database
        self.database.add_recipe(recipe)
    def share_recipe(self):
        # Get the selected recipe from the database
        selected_recipe = self.database.get_recipes()[0]
        # Create a new window to display the recipe information
        recipe_window = tk.Toplevel(self.window)
        recipe_window.title("Shared Recipe")
        # Create labels to display the recipe information
        recipe_name_label = tk.Label(recipe_window, text="Recipe Name: " + selected_recipe.get_name())
        recipe_name_label.pack()
        ingredients_label = tk.Label(recipe_window, text="Ingredients:")
        ingredients_label.pack()
        for ingredient in selected_recipe.get_ingredients():
            ingredient_label = tk.Label(recipe_window, text=ingredient.get_name())
            ingredient_label.pack()
        instructions_label = tk.Label(recipe_window, text="Instructions:\n" + selected_recipe.get_instructions())
        instructions_label.pack()