class FileCreator:

    component_base_template = 'const X = ({{}}:{{}}) =>     { return (); };  export default X;'

    def __init__(self, components_files_names):
        self.components_files_names = components_files_names
    
    def get_components_files_names(self):
        return self.components_files_names
    
    def set_components_files_names(self, new_names):
        self.components_files_names = new_names