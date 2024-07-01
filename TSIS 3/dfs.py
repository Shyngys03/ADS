class TreeNode:
    def __init__(self, val: int = 0, left = None, right = None) -> None:
        self.value = val
        self.left_child = left
        self.right_child = right

root = TreeNode('A')
root.left_child = TreeNode('B')
root.right_child = TreeNode('C')
root.left_child.left_child = TreeNode('D')
root.left_child.right_child = TreeNode('E')
root.right_child.left_child = TreeNode('F')
root.right_child.right_child = TreeNode('G')


def dfs(root: TreeNode) -> None:
    if root is None:
        return
    print(root.value, end=' ')
    dfs(root.left_child)
    dfs(root.right_child)

dfs(root)