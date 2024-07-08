class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):       
        self.head = None           
            
    def add_at_front(self,data):
        new_data = Node(data,self.head)
        self.head = new_data
        print(self.head.data)
        
    def print(self):
        if self.head is None:
            print('empty')
            
    def add_at_end(self,data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            print(self.head.data)
        # else:
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_data
        print(self.head.data)
                
obj = Linkedlist()
obj.add_at_front(12)            
obj.add_at_front(14)
obj.add_at_end(16)

            
            
                 