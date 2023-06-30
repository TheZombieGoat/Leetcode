"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.
"""

#Only used standard operations of stack
from collections import deque
class MyQueue:

    def __init__(self):
        self.front = deque([])
        self.back = deque([])

    def push(self, x: int) -> None:
        if len(self.back) > 0:
            while len(self.back) > 0:
                self.front.append(self.back.pop())
            self.front.append(x)
        else:
            self.front.append(x)

    def pop(self) -> int:
        self.peek()
        return self.back.pop()

    def peek(self) -> int:
        if len(self.back) > 0:
            return self.back[-1]
        else:
            while len(self.front) > 0:
                self.back.append(self.front.pop())
            return self.back[-1]

    def empty(self) -> bool:
        if len(self.front) > 0 or len(self.back) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
