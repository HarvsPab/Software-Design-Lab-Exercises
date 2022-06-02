# deletion

def delete_element_by_value(self, x):
    if self.start_node is None:
        print("The list has no element to delete")
        return

    # Deleting first node
    if self.start_node.item == x:
        self.start_node = self.start_node.ref
        return

    n = self.start_node
    while n.ref is not None:
        if n.ref.item == x:
            break
        n = n.ref

    if n.ref is None:
        print("item not found in the list")

    else:
        n.ref = n.ref.ref
