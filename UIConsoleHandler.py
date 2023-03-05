from FileCreator import FileCreator

class UIConsoleHandler:

    component_name_choosing_output = "type your component name:"

    def __init__(self, components_names, depth, fileCreator):
        # will get set after the user is done giving components names (input)
        self.components_names = []
        # will get set to 1 or 2
        self.depth = 0 
        # will get set after the user is done giving components names (input)
        self.fileCreator = FileCreator(components_names)