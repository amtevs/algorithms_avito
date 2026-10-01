class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.table = [[] for i in range(size)]

    def _get_index(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._get_index(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1
        if self.count / self.size > 0.75:
            self.resize()

    def search(self, key):
        index = self._get_index(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._get_index(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.count -= 1
                return True
        return False

    def resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for pair in bucket:
                self.insert(pair[0], pair[1])

    def show(self):
        for index in range(self.size):
            print(index, self.table[index])