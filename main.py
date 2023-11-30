class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0, item)

    def get(self):
        if self.isempty():
            raise QueueError("Queue error")
        return self.items.pop()


class SuperQueue(Queue):
    pass


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")