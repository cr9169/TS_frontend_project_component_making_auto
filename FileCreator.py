class FileCreator:

    component_base_template = "const X = ({{}}:{{}}) =>\n{\n return (); \n};\n  export default X;"

    def __init__(self, components_files_names):
        self.components_files_names = components_files_names
    
    def get_components_files_names(self):
        return self.components_files_names
    
    def set_components_files_names(self, new_names):
        self.components_files_names = new_names

    def adapt_component_base_template(self, component_name):
        adapted_component_base_template = FileCreator.component_base_template.replace("X", component_name)
        return adapted_component_base_template

    def create_jsx_file(self, component_name):
        with open(f"{component_name}.jsx", "w") as file:
            file.write(self.adapt_component_base_template(component_name)) 

    def create_scss_file(self, component_name):
        with open(f"{component_name}.scss", "w") as file:
            file.write("")