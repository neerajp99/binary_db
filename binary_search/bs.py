class binarySearchDB:
    # Constructor method 
    def __init__(self):
        # self.data = data 
        self.list = list()
        self.dict = dict() 

    # Method to get the length of the database 
    def length(self):
        return len(self.list)

    # Method to insert into the database 
    def insert(self, value: dict = None) -> None:
        # Throw a exception if the value argument is None
        if value is None:
            raise TypeError("Insert method requires a value argument! Undefined value")

        if self.length() > 0:
            pass 

    # Method to find the index using binary search 
    def search(self, value: dict, low: int = 0, high: int = None) -> int:
        # Edge cases
        if low < 0:
            raise ValueError('Lower index must be non-negative')
        if high is None:
            high = len(self.list)

        # Return low if the list is empty 
        if high == 0:
            return low 
        
        # Get the nearest index to the right
        while low < high:
            mid = (low + high) // 2 
            if value < self.list[mid]:
                high = mid - 1 
            else:
                low = mid + 1 
        return low 


X = binarySearchDB()
Y = binarySearchDB()
X.insert()
Y.insert({'x':19})

    


