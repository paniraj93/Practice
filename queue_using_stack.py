class QueueUsingStack:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, data):
    self.stack1.append(data)

  def dequeue(self):
    if not self.stack2:
      while self.stack1:
        self.stack2.append(self.stack1.pop())
    return self.stack2.pop()

  def display(self):
    print(self.stack2[::-1])  # Reverse stack2 for FIFO order

# Create a queue object
queue = QueueUsingStack()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

# Display queue elements
queue.display()  # Output: [5, 4, 3, 2, 1] (correct FIFO order)

# Dequeue an element
queue.dequeue()

# Display queue elements again
queue.display()  # Output: [4, 3, 2, 1]
