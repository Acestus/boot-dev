import copy

def css_styles(initial_styles):
    styles = copy.deepcopy(initial_styles)
    
    def add_style(selector, property_name, value):
        if selector not in styles:
            styles[selector] = {}
        styles[selector][property_name] = value
        return copy.deepcopy(styles)
    
    return add_style
