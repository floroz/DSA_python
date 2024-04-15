class ArrayList:
    length = 0

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = list(None for _ in range(capacity))

    def push(self, value):
        if self.__should_increase_capacity():
            self.__increase_capacity()

        self.data[self.length] = value
        self.length += 1

    def pop(self):
        if self.__should_decrease_capacity():
            self.__decrease_capacity()

        deleted_value = self.data[self.length - 1]
        self.length -= 1
        return deleted_value

    def shift(self):
        if self.__should_decrease_capacity():
            self.__decrease_capacity()

        deleted_value = self.data[0]
        self.length -= 1

        # move all elements by one index
        for i in range(self.length):
            self.data[i] = self.data[i + 1]

        return deleted_value

    def unshift(self, value):
        if self.__should_increase_capacity():
            self.__increase_capacity()

        # move all elements by one index
        for i in range(self.length):
            self.data[i + 1] = self.data[i]

        self.data[0] = value
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return

        if self.__should_increase_capacity():
            self.__increase_capacity()

        # move all elements from the given index by one
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.length += 1

    def at(self, index):
        if index < 0 or index > self.length:
            return

        return self.data[index]

    def __should_increase_capacity(self):
        return self.length == self.capacity

    def __increase_capacity(self):
        self.capacity *= 2
        self.data = self.data + list(range(self.capacity))

    def __should_decrease_capacity(self):
        return self.length <= self.capacity // 4

    def __decrease_capacity(self):
        self.capacity //= 2
        self.data = self.data[:self.capacity]
