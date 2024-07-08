class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position <= 0 :
            print("Mutaa payale no negative index")
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    # Create a linked list
    ll = LinkedList()

    # Append some values
    ll.append(1)
    ll.append(24)
    ll.append(32)
    ll.append(44)
    ll.append(87)

    # Display the linked list
    print("Original Linked List:")
    ll.display()

    # Inserting a value at position 2
    ll.insert_at_position(-20, 5)

    # Display the modified linked list
    print("\nLinked List after inserting 5 at position 2:")
    ll.display()
