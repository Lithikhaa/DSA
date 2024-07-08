stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)
print(stack)
print(stack[2])
stack.pop(2)
print(len(stack))
print(not(stack))
# using a list method the stack is created
stack = []
def push_element():
    element = int(input('enter the element : ' ))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print('The stack is empty')
    else:
        removed_element =  stack.pop()
        print(removed_element)
        print(stack)
while True:
    choice = int(input())
    if choice == 1:
        push_element()
    elif choice == 2:
        pop_element()
    else:
        break
import collections
stack = collections.deque()
print(stack)      
stack.append(10)
stack.append(20)
stack.insert(1,30)
print(stack)
stack.pop()
print(stack)


# queue
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print(queue)
queue.pop(0)
print(queue)




#creating a node:
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None        
class Linkedlist:
    def __init__(self):
        self.head = None
    def checking(self):
        if self.head is None:
            print('empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
l = Linkedlist()
            
        
                            