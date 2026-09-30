class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        self.stack2.pop()

    def put(self, value):
        self.stack1.append(value)


q = int(input())

queue = MyQueue()

for _ in range(q):
    values = input().split()

    query_type = int(values[0])

    if query_type == 1:
        queue.put(int(values[1]))

    elif query_type == 2:
        queue.pop()

    elif query_type == 3:
        print(queue.peek())