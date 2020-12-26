import uuid
import datetime 
from datetime import datetime, time
import time 
class binarySearchDB:
    # Constructor method 
    def __init__(self, id: str = str(uuid.uuid4())):
        # self.data = data 
        self.list = []
        self.dict = dict() 
        self.id = id
        self.index = 0 

    # Method to get the length of the database 
    def length(self):
        return len(self.list)

    # Method to insert  multiple or single 
    def insert(self, values):
        if type(values) == list or type(values) == tuple:
            for value in values:
                self.insert_single(value)
        else:
            self.insert_single(values)

    # Method to insert into the database 
    def insert_single(self, value: dict = None) -> None:
        # Throw a exception if the value argument is None
        if value is None:
            raise TypeError("Insert method requires a value argument! Undefined value")
        if value['messageID'] not in self.dict:
            # Updated dictionary for the list    
            list_values = {
                    'createdAt': value['createdAt'],
                    'messageID': value['messageID'] 
            }
            if self.length() > 0:
                # Get the nearest index to the right
                checkStr = "createdAt" 
                index = self.search_nearest(value, checkStr)
                # If index is greater than the length of the array
                if index >= self.length():
                    self.list.append(list_values)
                    self.dict[value['messageID']] = value['messageContent']
                else:
                    # Call the insert helper method
                    self.insert_helper(index, value, list_values, self.length())
                    self.dict[value['messageID']] = value['messageContent']
            else:
                self.list.append(list_values)
                self.dict[value['messageID']] = value['messageContent']
        else:
            raise Exception(f'Duplicate entry! Entry already exist with message ID: {value}')
            
    # Helper method to insert value at a specific index 
    def insert_helper(self, index: int, value: dict, list_values: dict , range: int):
        if index >= range:
            raise ValueError("Value index should be less than the length range of the list")
        # Insert the value into the array 
        self.list.insert(index, list_values)

        # Update the dictionary values 
        self.dict[value['messageID']] = value['messageContent']

    # Method to get the length of the list 
    def length(self):
        return len(self.list)   

    # Fetch all the information in the database 
    def all(self):
        return self.list

    # Delete the database entries using message id 
    def deleteByMessageID(self, id: str) -> None:
        # Array for search 
        array = [i["messageID"] for i in self.list if "messageID" in i]
        # Get the index of the target message ID
        index = self.checkPos(array, id, "messageID", 0, self.length() - 1)
        if index != -1:
            # Remove the values from the list 
            self.list.pop(index)
            # Remove the message from the dictionary 
            self.dict.pop(id)
        else:
            raise Exception(f'Information not present in the database with the message ID: {id}')

    # Method to update an entry using message ID 
    def update(self, messageID: str, messageContent: str = None, newMessageID: str = None, createdAt: str = None) -> None:
        # Array for search 
        array = [i["messageID"] for i in self.list if "messageID" in i]
        # Check if the message entry exists or not 
        index = self.checkPos(array, messageID, "messageID", 0, self.length() - 1)
        print('INDEX', index)
        if index != -1:
            # Update new message content if any 
            if messageContent is not None:
                self.dict[messageID] = messageContent 
            
            # Update the array with message id, and update position accordingly 
            if newMessageID is not None:
                # Delete the current value at the index 
                self.list.pop(index)
                # Find the nearest index to insert 
                newobject = {
                    "createdAt": createdAt,
                    "messageID": newMessageID
                }
                checkStr = "createdAt" 
                newIndex = self.search_nearest(newObject, checkStr)
                # If index is greater than the length of the array
                if newIndex >= self.length():
                    self.list.append(newObject)
                    self.dict[newObject['messageID']] = newObject['messageContent']
                else:
                    # Call the insert helper method
                    updateObject = {
                    "createdAt": createdAt,
                    "messageID": newMessageID,
                    "messageContent": messageContent
                }
                    self.insert_helper(newIndex, newObject, updateObject, self.length())
                    self.dict[newObject['messageID']] = newObject['messageContent']
        else:
            raise  Exception('Information not present in the database with the message ID: %s' %messageID)

    # Clear the database 
    def clear(self):
        self.list = list()
        self.dict = ()

    # Method to check if the values exists or not 
    def checkPos(self, array: list, target: str, checkStr: str, low: int, high: int) -> int:
        if low > high:
            return -1 
        else:
            mid = (low + high) // 2 
            if target == array[mid]:
                return mid
            elif target < array[mid]:
                return self.checkPos(array, target, checkStr, low, mid - 1)
            else:
                return self.checkPos(array, target, checkStr, mid + 1, high)

    # Method to find the index using binary search 
    def search_nearest(self, value: dict, checkStr: str, low: int = 0, high: int = None) -> int:
        value = value[checkStr]

        # Array for search 
        array = [i[checkStr] for i in self.list if checkStr in i]
        # Edge cases
        if low < 0:
            raise ValueError('Lower index must be non-negative')
        if high is None:
            high = len(array)

        # Return low if the list is empty 
        if high == 0:
            return low 
        
        # Get the nearest index to the right
        while low < high:
            mid = (low + high) // 2 
            if value < array[mid]:
                high = mid 
            else:
                low = mid + 1 
        return low 


Y = binarySearchDB()
x = datetime.now().time()
Y.insert(
    [
        {
        'createdAt': datetime.now().time(),
        'messageID': 'akaka111',
        'messageContent': 'Hello world 1!!'
        },
        {
        'createdAt': datetime.now().time(),
        'messageID': 'akaka113',
        'messageContent': 'Hello world 1!!'
        },
    ]
)
# print(Y.id)
# print(Y.dict)
Y.insert({
    'createdAt': datetime.now().time(),
    'messageID': str(uuid.uuid4()),
    'messageContent': 'Hello world 2!!'
})
Y.insert({'createdAt': x, 
          'messageID': str(uuid.uuid4()), 
          'messageContent': 'Hello world 3!!'
})
print(Y.all())
print('\n\n')
# Y.deleteByMessageID('akaka113')
start_time = time.time()
Y.update("akaka113", "Namaste beta!!")
print("--- %s seconds ---" % (time.time() - start_time))
print(Y.all())
print(Y.dict)




