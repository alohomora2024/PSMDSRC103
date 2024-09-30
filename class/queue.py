class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue) == 0:
            return "The queue is empty"
        else:
            return self.queue.pop(0)