from FileCreator import FileCreator
from Errors import *
import re

class UIConsoleHandler:

    component_name_choosing_output = "type your component name:"

    def __init__(self, components_names, depth, fileCreator):
        # will get set after the user is done giving components names (input)
        self.components_names = []
        # will get set to 1 or 2
        self.depth = 0 
        # will get set after the user is done giving components names (input)
        self.fileCreator = FileCreator(components_names)

    def get_components_names(self):
        return self.components_names
    
    def set_components_names(self, new_names):
        self.components_names = new_names
    
    def get_depth(self):
        return self.depth
    
    def set_depth(self, new_depth):
        self.depth = new_depth

    # Checks if a string is in Pascal case formatting and do not contain digits or whitespace
    def validate_user_input(user_input):
        return bool(re.match('^[A-Z][a-z]*([A-Z][a-z]*)*$', user_input)) and not re.search('[\d\s]', user_input)

    def get_user_input(self):

        print("Type component depth (1 / 2):")
        depth = input()

        if depth is None:
            raise NoneError("Depth can't be an empty string!")
        
        elif depth == 1: 
            print(UIConsoleHandler.component_name_choosing_output)
            component_name = input()
            if not self.validate_user_input(component_name):
                raise ValueError("User input isn't valid!")
            else:
                self.components_names.append(component_name)
            # // continue with folder and files creating

        elif depth == 2:
            return 
            # // change to mixed functionality with depth 1 and 2, loop, and file creating (has record in whatsapp)

        else: 
            raise ValueError("Depth has to be 1 or 2!")


    def console_handling():
        return
