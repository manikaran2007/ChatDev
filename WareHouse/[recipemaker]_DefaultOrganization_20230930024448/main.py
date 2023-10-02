'''
This is the main file of the recipe maker application.
'''
from recipe import Recipe
from ingredient import Ingredient
from database import Database
from user_interface import UserInterface
import os
def main():
    # Create an instance of the Recipe class
    recipe = Recipe()
    # Create an instance of the Ingredient class
    ingredient = Ingredient()
    # Create an instance of the Database class
    database = Database()
    # Create an instance of the UserInterface class
    user_interface = UserInterface(recipe, ingredient, database)
    # Start the recipe maker application
    user_interface.start()
if __name__ == "__main__":
    # Check if running in a graphical environment
    if os.environ.get("DISPLAY") or os.name == "nt":
        main()
    else:
        print("Error: This application requires a graphical display to run.")