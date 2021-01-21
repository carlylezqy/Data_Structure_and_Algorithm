class HashTable:
    def __init__(self, hashsize):
        self.size = hashsize
        self.slots = [None] * self.size
        self.hashtable = [None] * self.size
    
    def put(self, key, value):
        hashvalue = self.hash(key, self.size)
        if self.slots[hashvalue] is None: #New
            self.slots[hashvalue] = key
            self.hashtable[hashvalue] = value
        else: #exist
            if(self.slots[hashvalue] == key): #refresh
                self.hashtable[hashvalue] = value
            else:
                nextslot = self.rehash(hashvalue, self.size)
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, self.size)
                
                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.hashtable[nextslot] = value
                else:
                    self.hashtable[nextslot] = value
    
    def hash(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        init_pos = self.hash(key, self.size)
        pos = init_pos
        while pos is not None:
            if self.slots[pos] == key:
                return self.hashtable[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == init_pos:
                    break
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)


if __name__ == '__main__':
    H = HashTable(11)
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"

    print(H.slots)  # [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
    print(H.hashtable)  # ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
    print(H[20])  # 'chicken'
    H[20] = 'duck'
    print(H[20])  # duck
    print(H[99])  # None