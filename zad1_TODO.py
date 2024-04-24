"""
Uzupełnij 2 funkcje poniżej oznaczone jako "TODO". 
Nie modyfikuj kodu, który już istnieje.
Można tworzyć własne funkcje pomocnicze.
Po zaimplementowaniu rozwiązania komendy `pass` powinny być usunięte.
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(node_values: List[str]):
    if (
            not node_values
            or len(node_values) == 0
            or node_values[0].strip() == ""
            or node_values[0] == "null"
    ):
        return None
    root = Node(int(node_values[0]))
    queue = [(root, 0)]
    while queue:
        current_node, idx = queue.pop()
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2
        if left_idx < len(node_values):  # left child
            value = node_values[left_idx]
            if value != "null":
                current_node.left = Node(int(value))
                if left_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.left, left_idx))

        if right_idx < len(node_values):  # right child
            value = node_values[right_idx]
            if value != "null":
                current_node.right = Node(int(value))
                if right_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.right, right_idx))

    return root


def merge_trees(root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
    if root1 and root2:
        root1.val += root2.val
        root1.left = merge_trees(root1.left, root2.left)
        root1.right = merge_trees(root1.right, root2.right)
    else:
        root1 = root2 if root1 is None else root1
    return root1


def display_preorder(root: Optional[Node]):
    if root is not None:
        print(root.val, end=" ")
        display_preorder(root.left)
        display_preorder(root.right)


# nie zmieniaj poniższego kodu
if __name__ == "__main__":
    trees = input().strip().split(";")
    node_values1 = trees[0].strip().split(" ")
    node_values2 = trees[1].strip().split(" ")
    root1 = create_binary_tree(node_values1)
    root2 = create_binary_tree(node_values2)
    output_root = merge_trees(root1, root2)
    display_preorder(output_root)
