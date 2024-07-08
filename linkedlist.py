class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
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
    # def print_list(self):
    #     current = self.head
    #     while current:
    #         print(current.data,end= '--->')
    #         current = current.next
    def println(self):
        current = self.head
        while current:
            print(current.data, end='-->')
            current = current.next
        print()  # Add a new line after printing the linked list

        
    
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            
    
    def inserAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
       
li = linked_list()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.insertAtBegin(9)
li.inserAtEnd(111)
li.println()

