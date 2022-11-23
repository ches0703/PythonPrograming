# Hash Map

HashTableSize = 101


class SimpleHashMap:

    def __init__(self):
        self.hash_map = [None for h in range(HashTableSize)]

    def simple_hash(self, name):
        sum = 0
        for ch in name:
            sum += ord(ch)
        return sum % HashTableSize

    def put(self, name, tel_no):
        self.hash_map[self.simple_hash(name)] = tel_no

    def search(self, name):
        return self.hash_map[self.simple_hash(name)]

    def print_hash_map(self):
        for i in range(len(self.hash_map)):
            if self.hash_map[i] is not None:
                print("{}, {}".format(i, self.hash_map[i]))


if __name__ == "__main__":
    HashMap = SimpleHashMap()
    HashMap.put("Kim", 1234)
    HashMap.put("Park", 5678)
    HashMap.put("Yoon", 9988)

    HashMap.print_hash_map()

    print(HashMap.search("Kim"))
    print(HashMap.search("miK"))
    