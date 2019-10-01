# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.

class Node:
    def __init__(self):
        self.value = value
        self.right = right;
        self.left = left

def is_unvial(root):
    if root == null:
        return True
    if root.left != null and root.left.value != root.value:
        return False
    if root.right != null and root.right.value != root.value:
        return False
    if is_unvial(root.left) and is_unvial(root.right):
        return True
    return False

def count_univals(root):
    if root == null:
        return 0
    total_count = count_univals(root.left) + count_univals(root.right)
    if is_unival(root):
        total_count +=1
    return total_count
