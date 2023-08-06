from typing import List, Union

class HashTable:
    """
    Construct a Hash Table
    """

    # Initialize
    def __init__(self, size: int = 7) -> None:
        self.data_map = [None] * size

    # Hash values
    def __hash(self, key: str) -> int:
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            return my_hash

    # Set pairs
    def set_item(self, key: str, value: int) -> None:
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # Get pairs
    def get_item(self, key: str) -> Union[int, None]:
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map)):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    # Store values of Keys
    def keys(self) -> List[str]:
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    # Print Hash Table
    def print_table(self) -> None:
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

my_hash_table = HashTable()