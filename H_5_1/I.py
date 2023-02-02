class Queue():
    def __init__(self) -> None:
        self.stek = []

    def push(self, item):
        self.stek.append(item)

    def pop(self):
        out = self.stek[0]
        self.stek = self.stek[1:]
        return out

    def is_empty(self):
        return not self.stek


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")
