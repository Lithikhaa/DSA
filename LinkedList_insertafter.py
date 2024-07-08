class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next                     
        last_node.next = new_node
    
    def println(self):
        current = self.head
        while current:
            print(current.data, end='-->')
            current = current.next
        # print()  # Add a new line after printing the linked list

    def addfront(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
       
        new_node.next = self.head
        self.head = new_node
    def endatlast(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while (current.next):
            current = current.next
        current.next = new_node
    
    def insert_after(self, prev_node_data, data):
        new_node = Node(data)
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Node with data", prev_node_data, "not found.")
        
li = Linkedlist()
li.append(1)
li.append(2)
li.append(3)
li.addfront(4)
li.endatlast(5)
li.insert_after(3,3.5)
li.println()