import uuid
import datetime 
from datetime import datetime, time
class binarySearchDB:
    # Constructor method 
    def __init__(self, id: str = str(uuid.uuid4())):
        # self.data = data 
        self.list = []
        self.dict = dict() 
        self.id = id

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
            # If index is greater than the length of the array
            if index >= len(self.list):
                self.list.append(value['createdAt'])
            else:
                # Call the insert helper method
                self.insert_helper(index, value, len(self.list))
        else:
            self.list.append(value['createdAt'])
            self.dict[self.id] = self.list
            
    # Helper method to insert value at a specific index 
    def insert_helper(self, index: int, value: dict , range: int):
        if index >= range:
            raise ValueError("Value index should be less than the length range of the list")
        val = value['createdAt']

        # Insert the value into the array 
        self.list.insert(index, val)

        # Update the dictionary values 
        self.dict[self.id] = self.list 


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


Y = binarySearchDB()
# message = {
#     'createdAt': datetime.now().time(),
#     'messageID': str(uuid.uuid4()),
#     'messageContent': 'Hello world!!'
# }
Y.insert({
    'createdAt': datetime.now().time(),
    'messageID': str(uuid.uuid4()),
    'messageContent': 'Hello world!!'
})
print(Y.id)
print(Y.dict)
Y.insert({
    'createdAt': datetime.now().time(),
    'messageID': str(uuid.uuid4()),
    'messageContent': 'Hello world 2!!'
})
Y.insert({
    'createdAt': datetime.now().time(),
    'messageID': str(uuid.uuid4()),
    'messageContent': 'Hello world 3!!'
})
print(Y.dict)
    


