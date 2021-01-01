class BinarySearchTreeDB:
    def __init__(self, values: dict = {}):
        self.values = values
        self.left = null 
        self.right = null 
        self.parent = values.parent if values.parent != undefined else null 
        
