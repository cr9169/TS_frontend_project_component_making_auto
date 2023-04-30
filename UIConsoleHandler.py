from FileCreator import FileCreator
from Errors import *
import re
import os

class UIConsoleHandler:

    component_name_choosing_output = "type your component name:"

    def __init__(self, components_names=[], depth=0):
        # will get set after the user is done giving components names (input)
        self.components_names = components_names
        # will get set to 1 or 2
        self.depth = depth
        # will get set after the user is done giving components names (input)
        self.file_creator = FileCreator(components_names)

    def get_components_names(self):
        return self.components_names
    
    def set_components_names(self, new_names):
        self.components_names += new_names
    
    def initiate_components_names(self):
        self.components_names = [] 
    
    def get_depth(self):
        return self.depth
    
    def set_depth(self, new_depth):
        self.depth = new_depth

    # Checks if a string is in Pascal case formatting and do not contain digits or whitespace
    def validate_user_input(self, user_input):
        return bool(re.match('^[A-Z][a-z]*([A-Z][a-z]*)*$', user_input)) and not re.search('[\d\s]', user_input)

    def create_component_folder(self, component_name):
        if not self.validate_user_input(component_name):
            raise ValueError("User input isn't valid!")
        else:
            self.set_components_names([component_name])
            # Create folder if it doesn't exist
            if not os.path.exists(component_name):
                os.makedirs(component_name)
                print(f"Folder '{component_name}' created successfully.")
            
            # Create JSX and SCSS files in folder
            os.chdir(component_name)
            self.file_creator.create_jsx_file(component_name)
            self.file_creator.create_scss_file(component_name)

    def console_handling(self):

        depth = input("Type component depth (1 / 2): \n")

        if depth is None:
            raise NoneError("Depth can't be an empty string!")
        
        elif depth == "1": 
            component_name = input(self.component_name_choosing_output + "\n")
            self.set_components_names([component_name])
            self.create_component_folder()

        elif depth == "2": 
            component_name = input(self.component_name_choosing_output + "\n")
            self.set_components_names([component_name])
            self.create_component_folder(component_name)
            self.initiate_components_names()

            while True:
                component_name = input(self.component_name_choosing_output + "\n")
                if component_name not in self.components_names:
                    self.set_components_names([component_name])
                else:
                    print(f"Folder '{component_name}' already exists.")

                choice = input("Do you want to enter another string? (y / n) \n")
                if choice.lower() != 'y':
                    break

            for component_name in self.components_names:
                self.create_component_folder(component_name)
                os.chdir("..")

        else: 
            raise ValueError("Depth has to be 1 or 2!")