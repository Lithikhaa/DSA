'''A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. 
This means that the last element added to the stack will be the first one to be removed

Push: Add an element to the top of the stack.
Pop: Remove the top element from the stack.
Peek/Top: Get the value of the top element without removing it.
IsEmpty: Check if the stack is empty.
Size: Get the number of elements in the stack.
eg - undo (bactracking mechanism)

Feature	                Stack	                                       List

Access Order	LIFO (Last In, First Out)	        Sequential access (can access any element)
Operations	    Push, Pop, Peek, IsEmpty	            Access, Insert, Remove, Append, Slice
Access Time	    Typically only top element	            Access any element by index '''

from collections import deque

class Stack:
    
    def __init__(self):
        self.stack1 = deque()
               
    def push(self,value):      
        self.stack1.append(value)   
    def pop(self):
        return self.stack1.pop()
    
    def peek(self):
        return self.stack1[-1]
        
    def empty(self):
        if len(self.stack1) == 0:
            print('The Stack is empty')
        else:
            print(len(self.stack1))
               
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.peek())
print(s1.pop())
s1.empty()


'''A queue is a linear data structure that follows the First In, First Out (FIFO) principle. 
This means that the first element added to the queue will be the first one to be removed.
Enqueue: Add an element to the end of the queue.
Dequeue: Remove the element from the front of the queue.
Front: Get the value of the front element without removing it.
IsEmpty: Check if the queue is empty.
Size: Get the number of elements in the queue. '''

from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())