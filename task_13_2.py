class SmallQueue:
    def __init__(self):
        self.queue = []

    def add(self, number):
        self.queue.append(number)

    def append(self, number):
        self.queue.insert(0, number)

    def get_last(self):
        if self.queue:
            return self.queue.pop()
        else:
            return None

    def get_first(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def reverse(self):
        self.queue.reverse()


queue = SmallQueue()

queue.add(5)
queue.append(6)
queue.append(9)
queue.reverse()
queue.add(7)

print(queue.get_last())
print(queue.get_first())
print(queue.get_last())
print(queue.get_first())