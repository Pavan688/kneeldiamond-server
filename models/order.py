class Order():
    """Class that defines the properties for a order object"""

    # Write the __init__ method here
    def __init__(self, id, metal_id, size_id, style_id):
        self.id = id
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.metal = None
        self.style = None
        self.size = None
