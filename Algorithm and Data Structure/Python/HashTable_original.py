class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value

            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot] = value

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def hashfunction(self, key, size):
        return key % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        found = False
        stop = False
        pos = startslot
        while pos is not None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                # 回到了原点，表示找遍了没有找到
                if pos == startslot:
                    stop = True
        return data

    # 重载载 __getitem__ 和 __setitem__ 方法以允许使用 [] 访问
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)


if __name__ == '__main__':
    H = HashTable()
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
    print(H.data)  # ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
    print(H[20])  # 'chicken'
    H[20] = 'duck'
    print(H[20])  # duck
    print(H[99])  # None