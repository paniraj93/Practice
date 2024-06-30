q = []
class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack2 = self.stack1.copy()
        self.stack1.clear()
        self.stack1.append(data)
        self.stack1 = self.stack1 + self.stack2

    def dequeue(self):
        if self.stack1:
            print("Queue is empty")
        else:
            return self.stack1.pop()

    def display(self):
        print(self.stack2[::-1])

# Create a queue object
queue = QueueUsingStack()