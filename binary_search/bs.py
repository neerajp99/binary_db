class binarySearchDB:
    # Constructor method 
    def __init__(self):
        # self.data = data 
        self.list = [1, 10, 20, 220, 2200]
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
            # Get the nearest index to the right 
            index = self.search(value)

            # Call the insert helper method
            self.insert_helper(index, value, 5, len(self.list))
            print(self.list)
            

            
    # Helper method to insert value at a specific index 
    def insert_helper(self, index: int, value: dict , range: int):
        if index >= range:
            raise ValueError("Value index should be less than the length range of the list")
        val = value['createdAt']



    # Method to get the length of the list 
    def length(self):
        return len(self.list)    

    # Method to find the index using binary search 
    def search(self, value: dict, low: int = 0, high: int = None) -> int:
        value = value['createdAt']
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
                high = mid 
            else:
                low = mid + 1 
        return low 


X = binarySearchDB()
Y = binarySearchDB()
# X.insert()
Y.insert({'createdAt': 19})

    


