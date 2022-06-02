# insertion

from creation import Node
def insert_after_item(self, x, data):

    n = self.start_node
    print(n.ref)

    while n is not None:
        if n.item == x:
            break
        n = n.ref
    if n is None:
        print("item not in the list")

    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node
